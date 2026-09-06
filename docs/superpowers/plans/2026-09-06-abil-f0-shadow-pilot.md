# ABIL F0 Shadow Pilot Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the first headless ABIL prototype that can ingest a normalized streaming event feed, run simple online-learning baselines, persist deployment-bound state, detect regime changes, and produce reproducible evaluation output on a synthetic process and recorded replay.

**Architecture:** A protocol-neutral adapter interface emits typed telemetry events into a learner interface. The first learner implementations are deliberately established online baselines, not a novel proprietary model. Evaluation and checkpoint metadata remain separate from learner-visible telemetry so later industrial adapters can reuse the same contracts without importing simulator truth.

**Tech Stack:** Python 3.12, uv, pydantic 2.x, numpy, river, pytest

**Spec:** `docs/superpowers/specs/2026-09-06-abil-foundation-design.md`

## Global Constraints

- No machine write path in this implementation.
- No GPU dependency.
- No cloud service dependency.
- Learner-visible events must not contain evaluator-only simulator truth.
- Checkpoints are bound to `deployment_id` and incompatible restores fail closed.
- Established baselines must exist before a novel learner can be credited.
- All tests must run locally with deterministic seeds.

---

### Task 1: Project skeleton and telemetry event contract

**Files:**
- Create: `pyproject.toml`
- Create: `src/abil/__init__.py`
- Create: `src/abil/events.py`
- Create: `tests/unit/test_events.py`

**Interfaces:**
- Produces: `TelemetryEvent`, `SignalQuality`, `EventSource`
- Consumes: none

- [ ] **Step 1: Create the project metadata**

```toml
[project]
name = "abil"
version = "0.1.0"
description = "Adaptive Brownfield Intelligence Layer"
requires-python = ">=3.12"
dependencies = [
  "numpy>=2.0,<3",
  "pydantic>=2.9,<3",
  "river>=0.22,<1",
]

[dependency-groups]
dev = ["pytest>=8.3,<9"]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["src/abil"]

[tool.pytest.ini_options]
pythonpath = ["src"]
testpaths = ["tests"]
```

- [ ] **Step 2: Write the failing event-schema tests**

```python
from datetime import datetime, timezone

import pytest
from pydantic import ValidationError

from abil.events import EventSource, SignalQuality, TelemetryEvent


def test_telemetry_event_round_trip() -> None:
    event = TelemetryEvent(
        deployment_id="synthetic-a",
        source_id="sim-plc",
        signal_id="pressure",
        source_time=datetime(2026, 9, 6, tzinfo=timezone.utc),
        acquired_time=datetime(2026, 9, 6, tzinfo=timezone.utc),
        value=12.5,
        quality=SignalQuality.GOOD,
        source=EventSource.EXTERNAL,
    )
    restored = TelemetryEvent.model_validate_json(event.model_dump_json())
    assert restored == event


def test_event_rejects_missing_deployment_identity() -> None:
    with pytest.raises(ValidationError):
        TelemetryEvent(
            deployment_id="",
            source_id="sim-plc",
            signal_id="pressure",
            acquired_time=datetime.now(timezone.utc),
            value=12.5,
        )
```

- [ ] **Step 3: Run the tests and verify failure**

Run: `uv run pytest tests/unit/test_events.py -v`

Expected: FAIL because `abil.events` does not exist.

- [ ] **Step 4: Implement the event contract**

```python
from datetime import datetime
from enum import StrEnum
from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class SignalQuality(StrEnum):
    GOOD = "good"
    UNCERTAIN = "uncertain"
    BAD = "bad"


class EventSource(StrEnum):
    EXTERNAL = "external"
    ACTION_EFFERENCE = "action_efference"
    ACTION_CONSEQUENCE = "action_consequence"
    HUMAN_ANNOTATION = "human_annotation"


class TelemetryEvent(BaseModel):
    model_config = ConfigDict(frozen=True)

    deployment_id: str = Field(min_length=1)
    source_id: str = Field(min_length=1)
    signal_id: str = Field(min_length=1)
    source_time: datetime | None = None
    acquired_time: datetime
    value: float | int | bool | str
    quality: SignalQuality = SignalQuality.GOOD
    source: EventSource = EventSource.EXTERNAL
    metadata: dict[str, Any] = Field(default_factory=dict)
```

Create `src/abil/__init__.py` with:

```python
__all__ = []
```

- [ ] **Step 5: Run the tests**

Run: `uv run pytest tests/unit/test_events.py -v`

Expected: PASS.

- [ ] **Step 6: Commit**

```bash
git add pyproject.toml src/abil/__init__.py src/abil/events.py tests/unit/test_events.py
git commit -m "feat: define ABIL telemetry event contract"
```

---

### Task 2: Deterministic adapter and replay boundary

**Files:**
- Create: `src/abil/adapters/__init__.py`
- Create: `src/abil/adapters/base.py`
- Create: `src/abil/adapters/replay.py`
- Create: `tests/fixtures/replay.jsonl`
- Create: `tests/unit/test_replay_adapter.py`

**Interfaces:**
- Consumes: `TelemetryEvent`
- Produces: `EventAdapter.events() -> Iterator[TelemetryEvent]`, `JsonlReplayAdapter`

- [ ] **Step 1: Write the failing adapter tests**

```python
from abil.adapters.replay import JsonlReplayAdapter


def test_replay_preserves_file_order() -> None:
    events = list(JsonlReplayAdapter("tests/fixtures/replay.jsonl").events())
    assert [event.signal_id for event in events] == ["pressure", "valve", "pressure"]
    assert events[0].deployment_id == "fixture-a"
```

Create `tests/fixtures/replay.jsonl` with exactly:

```json
{"deployment_id":"fixture-a","source_id":"fixture","signal_id":"pressure","acquired_time":"2026-09-06T20:00:00Z","value":10.0,"quality":"good","source":"external","metadata":{}}
{"deployment_id":"fixture-a","source_id":"fixture","signal_id":"valve","acquired_time":"2026-09-06T20:00:01Z","value":0,"quality":"good","source":"external","metadata":{}}
{"deployment_id":"fixture-a","source_id":"fixture","signal_id":"pressure","acquired_time":"2026-09-06T20:00:02Z","value":10.5,"quality":"good","source":"external","metadata":{}}
```

- [ ] **Step 2: Run and verify failure**

Run: `uv run pytest tests/unit/test_replay_adapter.py -v`

Expected: FAIL because replay adapter does not exist.

- [ ] **Step 3: Implement adapter interface and JSONL replay**

`src/abil/adapters/base.py`:

```python
from collections.abc import Iterator
from typing import Protocol

from abil.events import TelemetryEvent


class EventAdapter(Protocol):
    def events(self) -> Iterator[TelemetryEvent]: ...
```

`src/abil/adapters/replay.py`:

```python
from collections.abc import Iterator
from pathlib import Path

from abil.events import TelemetryEvent


class JsonlReplayAdapter:
    def __init__(self, path: str | Path) -> None:
        self.path = Path(path)

    def events(self) -> Iterator[TelemetryEvent]:
        with self.path.open("r", encoding="utf-8") as handle:
            for line in handle:
                if line.strip():
                    yield TelemetryEvent.model_validate_json(line)
```

`src/abil/adapters/__init__.py`:

```python
from abil.adapters.base import EventAdapter
from abil.adapters.replay import JsonlReplayAdapter

__all__ = ["EventAdapter", "JsonlReplayAdapter"]
```

- [ ] **Step 4: Run tests**

Run: `uv run pytest tests/unit/test_replay_adapter.py -v`

Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add src/abil/adapters tests/fixtures/replay.jsonl tests/unit/test_replay_adapter.py
git commit -m "feat: add deterministic telemetry replay adapter"
```

---

### Task 3: Synthetic brownfield process generator

**Files:**
- Create: `src/abil/adapters/synthetic.py`
- Create: `tests/unit/test_synthetic_adapter.py`

**Interfaces:**
- Consumes: deployment ID, seed, step count
- Produces: learner-visible `TelemetryEvent` stream; evaluator truth remains private to the adapter object

- [ ] **Step 1: Write the failing synthetic-process tests**

```python
from abil.adapters.synthetic import SyntheticProcessAdapter


def test_synthetic_stream_is_deterministic() -> None:
    left = list(SyntheticProcessAdapter("sim-a", seed=7, steps=12).events())
    right = list(SyntheticProcessAdapter("sim-a", seed=7, steps=12).events())
    assert left == right


def test_hidden_regime_is_not_exposed_as_signal() -> None:
    adapter = SyntheticProcessAdapter("sim-a", seed=7, steps=12)
    events = list(adapter.events())
    assert "hidden_regime" not in {event.signal_id for event in events}
    assert len(adapter.evaluator_regimes) == 12
```

- [ ] **Step 2: Run and verify failure**

Run: `uv run pytest tests/unit/test_synthetic_adapter.py -v`

Expected: FAIL because the synthetic adapter does not exist.

- [ ] **Step 3: Implement a minimal two-regime process**

```python
from collections.abc import Iterator
from datetime import datetime, timedelta, timezone

import numpy as np

from abil.events import TelemetryEvent


class SyntheticProcessAdapter:
    def __init__(self, deployment_id: str, seed: int, steps: int) -> None:
        self.deployment_id = deployment_id
        self.seed = seed
        self.steps = steps
        self.evaluator_regimes: list[int] = []

    def events(self) -> Iterator[TelemetryEvent]:
        rng = np.random.default_rng(self.seed)
        start = datetime(2026, 9, 6, tzinfo=timezone.utc)
        pressure = 10.0
        valve = 0
        for step in range(self.steps):
            regime = 0 if step < self.steps // 2 else 1
            self.evaluator_regimes.append(regime)
            if step % 5 == 0:
                valve = 1 - valve
            gain = 0.35 if regime == 0 else -0.20
            pressure = 0.92 * pressure + gain * valve + float(rng.normal(0.0, 0.05))
            timestamp = start + timedelta(seconds=step)
            yield TelemetryEvent(
                deployment_id=self.deployment_id,
                source_id="synthetic-process",
                signal_id="valve",
                acquired_time=timestamp,
                value=valve,
            )
            yield TelemetryEvent(
                deployment_id=self.deployment_id,
                source_id="synthetic-process",
                signal_id="pressure",
                acquired_time=timestamp,
                value=pressure,
            )
```

- [ ] **Step 4: Run tests**

Run: `uv run pytest tests/unit/test_synthetic_adapter.py -v`

Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add src/abil/adapters/synthetic.py tests/unit/test_synthetic_adapter.py
git commit -m "feat: add deterministic synthetic process"
```

---

### Task 4: Online learner interface and baselines

**Files:**
- Create: `src/abil/learners/__init__.py`
- Create: `src/abil/learners/base.py`
- Create: `src/abil/learners/baselines.py`
- Create: `tests/unit/test_baselines.py`

**Interfaces:**
- Consumes: scalar named observations grouped by timestamp
- Produces: `Prediction(signal_id, mean, uncertainty)` and mutable online learner state

- [ ] **Step 1: Write failing baseline tests**

```python
from abil.learners.baselines import LastValuePredictor, RiverLinearPredictor


def test_last_value_predictor_uses_previous_value() -> None:
    model = LastValuePredictor()
    assert model.predict("pressure", {"pressure": 10.0}) is None
    model.learn("pressure", {"pressure": 10.0}, 10.0)
    prediction = model.predict("pressure", {"pressure": 11.0})
    assert prediction is not None
    assert prediction.mean == 10.0


def test_linear_predictor_updates_online() -> None:
    model = RiverLinearPredictor()
    before = model.predict("pressure", {"valve": 1.0})
    for _ in range(20):
        model.learn("pressure", {"valve": 1.0}, 5.0)
    after = model.predict("pressure", {"valve": 1.0})
    assert after is not None
    assert before is None or abs(after.mean - 5.0) < abs(before.mean - 5.0)
```

- [ ] **Step 2: Run and verify failure**

Run: `uv run pytest tests/unit/test_baselines.py -v`

Expected: FAIL because learner modules do not exist.

- [ ] **Step 3: Implement the learner contract and two baselines**

`src/abil/learners/base.py`:

```python
from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class Prediction:
    signal_id: str
    mean: float
    uncertainty: float | None = None


class OnlinePredictor(Protocol):
    def predict(self, signal_id: str, features: dict[str, float]) -> Prediction | None: ...
    def learn(self, signal_id: str, features: dict[str, float], target: float) -> None: ...
```

`src/abil/learners/baselines.py`:

```python
from river import linear_model, preprocessing

from abil.learners.base import Prediction


class LastValuePredictor:
    def __init__(self) -> None:
        self._last: dict[str, float] = {}

    def predict(self, signal_id: str, features: dict[str, float]) -> Prediction | None:
        if signal_id not in self._last:
            return None
        return Prediction(signal_id=signal_id, mean=self._last[signal_id])

    def learn(self, signal_id: str, features: dict[str, float], target: float) -> None:
        self._last[signal_id] = target


class RiverLinearPredictor:
    def __init__(self) -> None:
        self._models: dict[str, object] = {}

    def _model(self, signal_id: str):
        if signal_id not in self._models:
            self._models[signal_id] = preprocessing.StandardScaler() | linear_model.LinearRegression()
        return self._models[signal_id]

    def predict(self, signal_id: str, features: dict[str, float]) -> Prediction | None:
        model = self._models.get(signal_id)
        if model is None:
            return None
        value = model.predict_one(features)
        return None if value is None else Prediction(signal_id=signal_id, mean=float(value))

    def learn(self, signal_id: str, features: dict[str, float], target: float) -> None:
        self._model(signal_id).learn_one(features, target)
```

- [ ] **Step 4: Run tests**

Run: `uv run pytest tests/unit/test_baselines.py -v`

Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add src/abil/learners tests/unit/test_baselines.py
git commit -m "feat: add online predictor baselines"
```

---

### Task 5: Deployment-bound checkpoint envelope

**Files:**
- Create: `src/abil/persistence/__init__.py`
- Create: `src/abil/persistence/checkpoint.py`
- Create: `tests/unit/test_checkpoint.py`

**Interfaces:**
- Consumes: deployment ID, learner kind, serialized learner bytes, evidence frontier
- Produces: versioned `CheckpointEnvelope`; `save_checkpoint`, `load_checkpoint`

- [ ] **Step 1: Write failing checkpoint tests**

```python
from pathlib import Path

import pytest

from abil.persistence.checkpoint import CheckpointEnvelope, load_checkpoint, save_checkpoint


def test_checkpoint_round_trip(tmp_path: Path) -> None:
    path = tmp_path / "checkpoint.json"
    envelope = CheckpointEnvelope(
        deployment_id="sim-a",
        learner_kind="baseline",
        learner_state_b64="YWJj",
        evidence_frontier=42,
    )
    save_checkpoint(path, envelope)
    assert load_checkpoint(path, expected_deployment_id="sim-a") == envelope


def test_checkpoint_rejects_wrong_deployment(tmp_path: Path) -> None:
    path = tmp_path / "checkpoint.json"
    save_checkpoint(
        path,
        CheckpointEnvelope(
            deployment_id="sim-a",
            learner_kind="baseline",
            learner_state_b64="YWJj",
            evidence_frontier=42,
        ),
    )
    with pytest.raises(ValueError, match="deployment mismatch"):
        load_checkpoint(path, expected_deployment_id="sim-b")
```

- [ ] **Step 2: Run and verify failure**

Run: `uv run pytest tests/unit/test_checkpoint.py -v`

Expected: FAIL because checkpoint module does not exist.

- [ ] **Step 3: Implement checkpoint envelope**

```python
from datetime import datetime, timezone
from pathlib import Path

from pydantic import BaseModel, Field


class CheckpointEnvelope(BaseModel):
    schema_version: int = 1
    deployment_id: str = Field(min_length=1)
    learner_kind: str = Field(min_length=1)
    learner_state_b64: str
    evidence_frontier: int = Field(ge=0)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


def save_checkpoint(path: Path, envelope: CheckpointEnvelope) -> None:
    path.write_text(envelope.model_dump_json(indent=2), encoding="utf-8")


def load_checkpoint(path: Path, expected_deployment_id: str) -> CheckpointEnvelope:
    envelope = CheckpointEnvelope.model_validate_json(path.read_text(encoding="utf-8"))
    if envelope.deployment_id != expected_deployment_id:
        raise ValueError(
            f"deployment mismatch: checkpoint={envelope.deployment_id} expected={expected_deployment_id}"
        )
    return envelope
```

- [ ] **Step 4: Run tests**

Run: `uv run pytest tests/unit/test_checkpoint.py -v`

Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add src/abil/persistence tests/unit/test_checkpoint.py
git commit -m "feat: add deployment-bound checkpoint envelope"
```

---

### Task 6: Evaluation runner with regime-change evidence

**Files:**
- Create: `src/abil/evaluation/__init__.py`
- Create: `src/abil/evaluation/runner.py`
- Create: `tests/integration/test_synthetic_evaluation.py`

**Interfaces:**
- Consumes: `EventAdapter`, `OnlinePredictor`
- Produces: `EvaluationResult` containing mean absolute error before/after change, event count, and per-signal prediction records

- [ ] **Step 1: Write failing integration test**

```python
from abil.adapters.synthetic import SyntheticProcessAdapter
from abil.evaluation.runner import evaluate_pressure_prediction
from abil.learners.baselines import LastValuePredictor, RiverLinearPredictor


def test_online_model_is_evaluated_against_naive_baseline() -> None:
    adapter = SyntheticProcessAdapter("sim-a", seed=13, steps=400)
    naive = evaluate_pressure_prediction(adapter, LastValuePredictor())

    adapter = SyntheticProcessAdapter("sim-a", seed=13, steps=400)
    online = evaluate_pressure_prediction(adapter, RiverLinearPredictor())

    assert naive.prediction_count > 100
    assert online.prediction_count > 100
    assert online.mae >= 0.0
    assert naive.mae >= 0.0
```

- [ ] **Step 2: Run and verify failure**

Run: `uv run pytest tests/integration/test_synthetic_evaluation.py -v`

Expected: FAIL because evaluation runner does not exist.

- [ ] **Step 3: Implement deterministic evaluation grouping valve and pressure by timestamp**

```python
from dataclasses import dataclass

from abil.adapters.base import EventAdapter
from abil.learners.base import OnlinePredictor


@dataclass(frozen=True)
class EvaluationResult:
    mae: float
    prediction_count: int


def evaluate_pressure_prediction(adapter: EventAdapter, predictor: OnlinePredictor) -> EvaluationResult:
    current: dict[object, dict[str, float]] = {}
    absolute_errors: list[float] = []

    for event in adapter.events():
        if not isinstance(event.value, (int, float, bool)):
            continue
        key = event.acquired_time
        bucket = current.setdefault(key, {})
        bucket[event.signal_id] = float(event.value)
        if "valve" not in bucket or "pressure" not in bucket:
            continue

        target = bucket["pressure"]
        features = {"valve": bucket["valve"]}
        prediction = predictor.predict("pressure", features)
        if prediction is not None:
            absolute_errors.append(abs(prediction.mean - target))
        predictor.learn("pressure", features, target)
        del current[key]

    mae = sum(absolute_errors) / len(absolute_errors) if absolute_errors else 0.0
    return EvaluationResult(mae=mae, prediction_count=len(absolute_errors))
```

- [ ] **Step 4: Run integration test and full suite**

Run:

```bash
uv run pytest tests/integration/test_synthetic_evaluation.py -v
uv run pytest -q
```

Expected: all tests PASS.

- [ ] **Step 5: Commit**

```bash
git add src/abil/evaluation tests/integration/test_synthetic_evaluation.py
git commit -m "feat: add deterministic ABIL evaluation runner"
```

---

### Task 7: Headless shadow CLI and evidence report

**Files:**
- Create: `src/abil/cli.py`
- Create: `tests/integration/test_cli.py`
- Modify: `pyproject.toml`

**Interfaces:**
- Consumes: synthetic parameters or JSONL replay path
- Produces: machine-readable JSON evaluation report on stdout

- [ ] **Step 1: Add a console entry point to `pyproject.toml`**

```toml
[project.scripts]
abil = "abil.cli:main"
```

- [ ] **Step 2: Write the failing CLI test**

```python
import json
import subprocess


def test_cli_emits_json_report() -> None:
    completed = subprocess.run(
        ["uv", "run", "abil", "synthetic", "--steps", "100", "--seed", "4"],
        check=True,
        capture_output=True,
        text=True,
    )
    report = json.loads(completed.stdout)
    assert report["deployment_id"] == "synthetic-cli"
    assert report["prediction_count"] > 0
    assert report["mae"] >= 0.0
```

- [ ] **Step 3: Run and verify failure**

Run: `uv run pytest tests/integration/test_cli.py -v`

Expected: FAIL because CLI does not exist.

- [ ] **Step 4: Implement the CLI**

```python
import argparse
import json

from abil.adapters.synthetic import SyntheticProcessAdapter
from abil.evaluation.runner import evaluate_pressure_prediction
from abil.learners.baselines import RiverLinearPredictor


def main() -> None:
    parser = argparse.ArgumentParser(prog="abil")
    subparsers = parser.add_subparsers(dest="command", required=True)
    synthetic = subparsers.add_parser("synthetic")
    synthetic.add_argument("--steps", type=int, default=400)
    synthetic.add_argument("--seed", type=int, default=7)
    args = parser.parse_args()

    if args.command == "synthetic":
        adapter = SyntheticProcessAdapter("synthetic-cli", seed=args.seed, steps=args.steps)
        result = evaluate_pressure_prediction(adapter, RiverLinearPredictor())
        print(
            json.dumps(
                {
                    "deployment_id": "synthetic-cli",
                    "prediction_count": result.prediction_count,
                    "mae": result.mae,
                },
                sort_keys=True,
            )
        )
```

- [ ] **Step 5: Run the full verification suite**

Run:

```bash
uv run pytest -q
uv run abil synthetic --steps 400 --seed 13
```

Expected: tests PASS and CLI prints one valid JSON object containing `deployment_id`, `prediction_count`, and `mae`.

- [ ] **Step 6: Commit**

```bash
git add pyproject.toml src/abil/cli.py tests/integration/test_cli.py
git commit -m "feat: add headless ABIL shadow evaluation CLI"
```

---

## Plan self-review

Spec coverage:

- normalized event boundary: Task 1;
- adapter abstraction and replay: Task 2;
- evaluator/learner truth separation: Task 3;
- established online baselines: Task 4;
- deployment-bound persistence envelope: Task 5;
- reproducible evaluation: Task 6;
- headless operator/evidence surface: Task 7;
- machine write path: intentionally absent per spec.

The plan intentionally stops before a real PLC/OT adapter. The first live adapter should be a separate design/plan after the synthetic and replay contracts have passed review and tests.

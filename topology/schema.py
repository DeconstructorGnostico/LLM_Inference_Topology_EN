from dataclasses import dataclass, field
from typing import Any


@dataclass
class InputState:
    text: str
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class IntentState:
    objective: str | None = None
    constraints: list[str] = field(default_factory=list)
    variables: dict[str, Any] = field(default_factory=dict)


@dataclass
class ContextState:
    messages: list[dict[str, str]] = field(default_factory=list)
    token_estimate: int = 0
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class InferenceState:
    model: str | None = None
    provider: str | None = None
    prompt: str | None = None
    response: str | None = None
    latency_ms: float | None = None
    input_tokens: int | None = None
    output_tokens: int | None = None


@dataclass
class ValidationState:
    valid: bool = False
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


@dataclass
class OutputState:
    text: str | None = None
    format: str = "text"
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class TopologyState:
    input: InputState
    intent: IntentState = field(default_factory=IntentState)
    context: ContextState = field(default_factory=ContextState)
    inference: InferenceState = field(default_factory=InferenceState)
    validation: ValidationState = field(default_factory=ValidationState)
    output: OutputState = field(default_factory=OutputState)

    def to_dict(self) -> dict[str, Any]:
        return {
            "input": self.input.__dict__,
            "intent": self.intent.__dict__,
            "context": self.context.__dict__,
            "inference": self.inference.__dict__,
            "validation": self.validation.__dict__,
            "output": self.output.__dict__,
        }

from dataclasses import dataclass, field


@dataclass
class ModelDescriptor:

    name: str
    provider: str
    architecture: str = "unknown"
    parameters: int | None = None
    context_length: int | None = None
    quantization: str | None = None
    metadata: dict = field(
        default_factory=dict
    )

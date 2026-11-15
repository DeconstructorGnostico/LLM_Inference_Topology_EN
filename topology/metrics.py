from statistics import mean
from typing import Iterable


def token_throughput(
    output_tokens: int | None,
    latency_ms: float | None,
) -> float | None:

    if (
        output_tokens is None
        or latency_ms is None
    ):
        return None

    if latency_ms <= 0:
        return None

    return (
        output_tokens /
        (latency_ms / 1000)
    )


def latency_summary(
    latencies_ms: Iterable[float]
) -> dict:

    values = list(latencies_ms)

    if not values:

        return {
            "count": 0,
            "mean_ms": None,
            "min_ms": None,
            "max_ms": None,
        }

    return {
        "count": len(values),
        "mean_ms": mean(values),
        "min_ms": min(values),
        "max_ms": max(values),
    }

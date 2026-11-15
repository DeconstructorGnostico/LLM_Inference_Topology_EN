import json

from topology.graph import (
    default_topology
)

from topology.inference import (
    MockBackend
)

from topology.schema import (
    InputState,
    TopologyState
)

from topology.validation import (
    validate_state
)

from topology.metrics import (
    token_throughput
)


def run():

    topology = default_topology()

    topology_errors = (
        topology.validate()
    )

    if topology_errors:

        raise RuntimeError(
            topology_errors
        )

    backend = MockBackend()

    state = TopologyState(
        input=InputState(
            text=(
                "Describe the "
                "inference topology."
            )
        )
    )

    state.inference = (
        backend.generate(
            state.input.text
        )
    )

    state = validate_state(
        state
    )

    return {
        "topology_valid":
            not topology_errors,

        "state_valid":
            state.validation.valid,

        "latency_ms":
            state.inference.latency_ms,

        "throughput_tokens_s":
            token_throughput(
                state.inference.output_tokens,
                state.inference.latency_ms,
            ),
    }


if __name__ == "__main__":

    print(
        json.dumps(
            run(),
            indent=2
        )
    )

import argparse
import json

from .graph import default_topology
from .inference import (
    MockBackend,
    OllamaBackend,
)
from .schema import (
    InputState,
    TopologyState,
)
from .validation import validate_state


def build_parser():

    parser = argparse.ArgumentParser(
        description=(
            "LLM Inference Topology "
            "experimental runner"
        )
    )

    parser.add_argument(
        "text",
        nargs="?",
        default=(
            "Analyze this architecture."
        ),
    )

    parser.add_argument(
        "--backend",
        choices=[
            "mock",
            "ollama"
        ],
        default="mock",
    )

    parser.add_argument(
        "--model",
        default="llama3.2",
    )

    parser.add_argument(
        "--topology",
        action="store_true",
        help="Print topology graph.",
    )

    return parser


def main():

    args = build_parser().parse_args()

    topology = default_topology()

    if args.topology:

        print(
            json.dumps(
                topology.as_dict(),
                indent=2,
                ensure_ascii=False,
            )
        )

        return

    errors = topology.validate()

    if errors:

        raise RuntimeError(
            "Topology validation failed: "
            + str(errors)
        )

    if args.backend == "ollama":

        backend = OllamaBackend(
            model=args.model
        )

    else:

        backend = MockBackend()

    state = TopologyState(
        input=InputState(
            text=args.text
        )
    )

    state.inference = (
        backend.generate(
            args.text
        )
    )

    state = validate_state(
        state
    )

    print(
        json.dumps(
            state.to_dict(),
            indent=2,
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()

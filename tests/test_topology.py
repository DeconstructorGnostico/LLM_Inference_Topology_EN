from topology.graph import (
    Edge,
    InferenceTopology,
    Node,
    default_topology,
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


def test_default_topology_is_valid():

    topology = default_topology()

    assert topology.validate() == []

    assert len(
        topology.nodes
    ) == 5

    assert len(
        topology.edges
    ) > 0


def test_unknown_edge_is_rejected():

    topology = InferenceTopology()

    topology.add_node(
        Node(
            id="A",
            layer=0,
            name="A",
            type="test",
        )
    )

    try:

        topology.add_edge(
            Edge(
                source="A",
                target="UNKNOWN",
                relation="test",
            )
        )

    except ValueError:

        return

    raise AssertionError(
        "Unknown node should raise ValueError"
    )


def test_mock_inference():

    backend = MockBackend()

    result = backend.generate(
        "hello"
    )

    assert result.response is not None

    assert (
        result.provider
        == "local-mock"
    )

    assert (
        result.latency_ms
        is not None
    )


def test_state_validation():

    backend = MockBackend()

    state = TopologyState(
        input=InputState(
            text="hello"
        )
    )

    state.inference = (
        backend.generate(
            "hello"
        )
    )

    result = validate_state(
        state
    )

    assert (
        result.validation.valid
        is True
    )

    assert (
        result.output.text
        is not None
    )

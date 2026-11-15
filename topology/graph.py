from dataclasses import dataclass, field


@dataclass
class Node:
    id: str
    layer: int
    name: str
    type: str


@dataclass
class Edge:
    source: str
    target: str
    relation: str


@dataclass
class InferenceTopology:
    nodes: list[Node] = field(default_factory=list)
    edges: list[Edge] = field(default_factory=list)

    def add_node(self, node: Node) -> None:
        if any(n.id == node.id for n in self.nodes):
            raise ValueError(f"Node already exists: {node.id}")

        self.nodes.append(node)

    def add_edge(self, edge: Edge) -> None:
        ids = {n.id for n in self.nodes}

        if edge.source not in ids:
            raise ValueError(
                f"Unknown source node: {edge.source}"
            )

        if edge.target not in ids:
            raise ValueError(
                f"Unknown target node: {edge.target}"
            )

        self.edges.append(edge)

    def validate(self) -> list[str]:
        errors = []

        ids = {n.id for n in self.nodes}

        for edge in self.edges:
            if edge.source not in ids:
                errors.append(
                    f"Unknown source: {edge.source}"
                )

            if edge.target not in ids:
                errors.append(
                    f"Unknown target: {edge.target}"
                )

        layers = {n.layer for n in self.nodes}

        if not layers:
            errors.append(
                "Topology contains no nodes."
            )

        if min(layers, default=0) < 0:
            errors.append(
                "Layer cannot be negative."
            )

        return errors

    def as_dict(self) -> dict:
        return {
            "nodes": [
                n.__dict__
                for n in self.nodes
            ],
            "edges": [
                e.__dict__
                for e in self.edges
            ],
        }


def default_topology() -> InferenceTopology:

    topology = InferenceTopology()

    nodes = [
        Node(
            "L0",
            0,
            "Compute substrate",
            "hardware"
        ),
        Node(
            "L1",
            1,
            "Model inference",
            "model"
        ),
        Node(
            "L2",
            2,
            "Policy and control",
            "control"
        ),
        Node(
            "L3",
            3,
            "Context orchestration",
            "orchestration"
        ),
        Node(
            "L4",
            4,
            "Application interface",
            "interface"
        ),
    ]

    for node in nodes:
        topology.add_node(node)

    topology.add_edge(
        Edge(
            "L4",
            "L3",
            "request"
        )
    )

    topology.add_edge(
        Edge(
            "L3",
            "L2",
            "context_to_control"
        )
    )

    topology.add_edge(
        Edge(
            "L2",
            "L1",
            "controlled_inference"
        )
    )

    topology.add_edge(
        Edge(
            "L1",
            "L0",
            "computation"
        )
    )

    topology.add_edge(
        Edge(
            "L0",
            "L1",
            "execution_result"
        )
    )

    topology.add_edge(
        Edge(
            "L1",
            "L2",
            "model_output"
        )
    )

    topology.add_edge(
        Edge(
            "L2",
            "L3",
            "validated_output"
        )
    )

    topology.add_edge(
        Edge(
            "L3",
            "L4",
            "render"
        )
    )

    return topology

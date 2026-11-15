from topology.graph import (
    default_topology
)


def main():

    topology = default_topology()

    errors = topology.validate()

    print(
        "NODES:",
        len(topology.nodes)
    )

    print(
        "EDGES:",
        len(topology.edges)
    )

    if errors:

        print(
            "STATUS: FAIL"
        )

        for error in errors:
            print(
                "-",
                error
            )

        raise SystemExit(1)

    print(
        "STATUS: PASS"
    )


if __name__ == "__main__":
    main()

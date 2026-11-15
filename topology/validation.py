from .schema import TopologyState


def validate_state(
    state: TopologyState
) -> TopologyState:

    errors = []
    warnings = []

    if not state.input.text.strip():

        errors.append(
            "Input text is empty."
        )

    if state.inference.response is None:

        errors.append(
            "Inference response is missing."
        )

    if state.inference.model is None:

        warnings.append(
            "No model identifier was recorded."
        )

    state.validation.errors = errors
    state.validation.warnings = warnings

    state.validation.valid = (
        len(errors) == 0
    )

    if state.inference.response is not None:

        state.output.text = (
            state.inference.response
        )

    return state

import json
import time
import urllib.request
import urllib.error

from .schema import InferenceState


class InferenceBackend:

    def generate(
        self,
        prompt: str
    ) -> InferenceState:
        raise NotImplementedError


class MockBackend(InferenceBackend):

    def __init__(
        self,
        model: str = "mock"
    ):
        self.model = model

    def generate(
        self,
        prompt: str
    ) -> InferenceState:

        start = time.perf_counter()

        response = (
            "[MOCK INFERENCE] "
            f"Input received: {prompt}"
        )

        latency = (
            time.perf_counter() - start
        ) * 1000

        return InferenceState(
            model=self.model,
            provider="local-mock",
            prompt=prompt,
            response=response,
            latency_ms=latency,
            input_tokens=len(prompt.split()),
            output_tokens=len(response.split()),
        )


class OllamaBackend(InferenceBackend):

    def __init__(
        self,
        model: str = "llama3.2",
        host: str = "http://127.0.0.1:11434",
    ):
        self.model = model
        self.host = host.rstrip("/")

    def generate(
        self,
        prompt: str
    ) -> InferenceState:

        payload = json.dumps({
            "model": self.model,
            "prompt": prompt,
            "stream": False,
        }).encode("utf-8")

        request = urllib.request.Request(
            f"{self.host}/api/generate",
            data=payload,
            headers={
                "Content-Type": "application/json"
            },
            method="POST",
        )

        start = time.perf_counter()

        try:

            with urllib.request.urlopen(
                request,
                timeout=120
            ) as response:

                data = json.loads(
                    response
                    .read()
                    .decode("utf-8")
                )

        except urllib.error.URLError as exc:

            raise RuntimeError(
                f"Ollama unavailable at "
                f"{self.host}: {exc}"
            ) from exc

        latency = (
            time.perf_counter() - start
        ) * 1000

        text = data.get(
            "response",
            ""
        )

        return InferenceState(
            model=self.model,
            provider="ollama",
            prompt=prompt,
            response=text,
            latency_ms=latency,
            input_tokens=data.get(
                "prompt_eval_count"
            ),
            output_tokens=data.get(
                "eval_count"
            ),
        )


def run_inference(
    text: str,
    backend: InferenceBackend
) -> InferenceState:

    return backend.generate(text)

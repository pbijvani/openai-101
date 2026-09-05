import unittest

from config import normalize_endpoint


class FoundryEndpointTests(unittest.TestCase):
    def test_foundry_endpoint_keeps_openai_v1_suffix(self):
        endpoint = "https://foundry-pb.services.ai.azure.com/openai/v1"
        self.assertEqual(normalize_endpoint(endpoint), endpoint)

    def test_azure_resource_endpoint_strips_openai_v1_suffix(self):
        endpoint = "https://demo-resource.openai.azure.com/openai/v1"
        self.assertEqual(normalize_endpoint(endpoint), "https://demo-resource.openai.azure.com")

    def test_foundry_endpoint_detected_with_openai_suffix(self):
        endpoint = "https://foundry-pb.services.ai.azure.com/openai/v1"
        self.assertTrue(endpoint.endswith("/openai/v1"))

    def test_stream_response_ignores_empty_choices(self):
        class FakeDelta:
            content = "Hello"

        class FakeChoice:
            def __init__(self, delta=None):
                self.delta = delta

        class FakeChunk:
            def __init__(self, choices):
                self.choices = choices

        chunks = [
            FakeChunk([]),
            FakeChunk([FakeChoice(FakeDelta())]),
        ]

        outputs = []
        for chunk in chunks:
            choices = getattr(chunk, "choices", None) or []
            if not choices:
                continue
            for choice in choices:
                delta = getattr(choice, "delta", None)
                if delta is None:
                    continue
                content = getattr(delta, "content", None)
                if content:
                    outputs.append(content)

        self.assertEqual(outputs, ["Hello"])


if __name__ == "__main__":
    unittest.main()

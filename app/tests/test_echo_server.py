import unittest
from flask import json
from echo_server import app


class EchoServerTest(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_post_echo_valid(self):
        response = self.client.post("/echo", json={"message": "Hello from POST"})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["message"], "Hello from POST")

    def test_post_echo_exceeds_length(self):
        long_message = "A" * 1001
        response = self.client.post("/echo", json={"message": long_message})
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", json.loads(response.data))

    def test_post_echo_invalid_characters(self):
        invalid_message = '<script>alert("xss")</script>'
        response = self.client.post("/echo", json={"message": invalid_message})
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", json.loads(response.data))


if __name__ == "__main__":
    unittest.main()

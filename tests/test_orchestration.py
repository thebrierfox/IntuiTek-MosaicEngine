import unittest
import requests

class TestOrchestration(unittest.TestCase):
    def test_mosaic_endpoint(self):
        url = "http://localhost:5000/mosaic"
        payload = {"sample": "data"}
        try:
            response = requests.post(url, json=payload, timeout=5)
            self.assertEqual(response.status_code, 200)
        except Exception as e:
            self.fail(f"Request failed: {e}")

if __name__ == '__main__':
    unittest.main()

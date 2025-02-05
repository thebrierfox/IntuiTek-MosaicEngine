import unittest
from monitoring.monitoring import monitor_endpoint

class TestMonitoring(unittest.TestCase):
    def test_monitor_endpoint(self):
        status, info = monitor_endpoint("https://www.google.com")
        self.assertTrue(status)

if __name__ == '__main__':
    unittest.main()

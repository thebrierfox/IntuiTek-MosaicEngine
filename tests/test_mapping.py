import unittest
import json
from mapping.module_mapping import map_components

class TestMapping(unittest.TestCase):
    def test_map_components(self):
        sample_concept = {
            "modules": [
                {"name": "task_manager"},
                {"name": "client_crm"}
            ]
        }
        result = map_components(sample_concept)
        self.assertIn("task_manager", result)
        self.assertIn("client_crm", result)

if __name__ == '__main__':
    unittest.main()

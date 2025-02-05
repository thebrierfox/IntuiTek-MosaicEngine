import unittest
import json
from ingestion.concept_ingestion import analyze_concept

class TestIngestion(unittest.TestCase):
    def test_analyze_concept(self):
        sample_text = "This concept includes a task manager and a client CRM."
        result = analyze_concept(sample_text)
        self.assertIn("modules", result)
        self.assertIsInstance(result["modules"], list)

if __name__ == '__main__':
    unittest.main()

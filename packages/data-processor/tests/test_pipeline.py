import unittest
import sys
from pathlib import Path

# Add parent directory to path to allow imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.data_processor.pipeline import Record, transform, filter_empty

class TestPipeline(unittest.TestCase):
    def test_transform(self):
        records = [
            Record(index=1, value="hello"),
            Record(index=2, value="world")
        ]
        expected = [
            {"index": 1, "value": "HELLO"},
            {"index": 2, "value": "WORLD"}
        ]
        self.assertEqual(transform(records), expected)

    def test_filter_empty(self):
        records = [
            Record(index=1, value="hello"),
            Record(index=2, value="  "),
            Record(index=3, value="world"),
            Record(index=4, value="")
        ]
        result = filter_empty(records)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].index, 1)
        self.assertEqual(result[1].index, 3)

if __name__ == "__main__":
    unittest.main()

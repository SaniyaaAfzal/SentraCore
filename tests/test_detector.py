
import unittest

from src.detector import detect_event


class TestSentraCoreDetector(unittest.TestCase):
    def test_normal_event(self):
        event = {"connection_count": "3"}
        self.assertEqual(detect_event(event), "NORMAL")

    def test_count_above_threshold(self):
        event = {"connection_count": "25"}
        self.assertEqual(detect_event(event), "ALERT")

    def test_count_at_threshold(self):
        event = {"connection_count": "20"}
        self.assertEqual(detect_event(event), "ALERT")

    def test_count_below_threshold(self):
        event = {"connection_count": "19"}
        self.assertEqual(detect_event(event), "NORMAL")

    def test_invalid_count(self):
        event = {"connection_count": "invalid"}
        with self.assertRaises(ValueError):
            detect_event(event)

    def test_custom_threshold(self):
        event = {"connection_count": "10"}
        self.assertEqual(detect_event(event, threshold=10), "ALERT")


if __name__ == "__main__":
    unittest.main()

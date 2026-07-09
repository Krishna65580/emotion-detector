"""
Unit tests for the emotion_detector function.
"""

import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """Test cases for the emotion_detector function."""

    def test_emotion_detector(self):
        """Verify that each statement returns the expected dominant emotion."""
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result["dominant_emotion"], "joy")

        result = emotion_detector("I am so angry with you")
        self.assertEqual(result["dominant_emotion"], "anger")

        result = emotion_detector("I am disgusted by your behavior")
        self.assertEqual(result["dominant_emotion"], "disgust")

        result = emotion_detector("I am so sad about this")
        self.assertEqual(result["dominant_emotion"], "sadness")

        result = emotion_detector("I am fearful of the dark")
        self.assertEqual(result["dominant_emotion"], "fear")


if __name__ == "__main__":
    unittest.main()

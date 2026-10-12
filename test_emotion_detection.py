"""Unit tests for the EmotionDetection package."""

import unittest
from unittest.mock import Mock, patch

from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Tests for successful responses and error handling."""

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_successful_response_and_dominant_emotion(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "emotionPredictions": [
                {
                    "emotion": {
                        "anger": 0.01,
                        "disgust": 0.02,
                        "fear": 0.03,
                        "joy": 0.90,
                        "sadness": 0.04,
                    }
                }
            ]
        }
        mock_post.return_value = mock_response

        result = emotion_detector("I am very happy")
        self.assertEqual(result["dominant_emotion"], "joy")
        self.assertEqual(result["anger"], 0.01)
        self.assertEqual(result["disgust"], 0.02)
        self.assertEqual(result["fear"], 0.03)
        self.assertEqual(result["joy"], 0.90)
        self.assertEqual(result["sadness"], 0.04)

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_http_400_returns_none(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 400
        mock_post.return_value = mock_response

        self.assertIsNone(emotion_detector("invalid service request"))

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_blank_text_returns_none_without_request(self, mock_post):
        self.assertIsNone(emotion_detector("   "))
        mock_post.assert_not_called()

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_dominant_emotion_is_anger(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "emotionPredictions": [
                {
                    "emotion": {
                        "anger": 0.80,
                        "disgust": 0.05,
                        "fear": 0.05,
                        "joy": 0.05,
                        "sadness": 0.05,
                    }
                }
            ]
        }
        mock_post.return_value = mock_response

        result = emotion_detector("I am furious")
        self.assertEqual(result["dominant_emotion"], "anger")


if __name__ == "__main__":
    unittest.main()


import unittest

from src.validation import validate_preferences
from src.evaluation import evaluate_recommendations


class TestReliability(unittest.TestCase):

    def setUp(self):
        self.preferences = {
            "genre": "pop",
            "mood": "happy",
            "energy": 0.8
        }

        self.recommendations = [
            (
                {
                    "title": "Song A",
                    "genre": "pop",
                    "mood": "happy",
                    "energy": 0.9
                },
                3.9,
                "genre match; mood match"
            ),
            (
                {
                    "title": "Song B",
                    "genre": "rock",
                    "mood": "happy",
                    "energy": 0.7
                },
                1.9,
                "mood match"
            ),
            (
                {
                    "title": "Song C",
                    "genre": "pop",
                    "mood": "calm",
                    "energy": 0.8
                },
                3.0,
                "genre match"
            )
        ]

    def test_valid_preferences(self):
        self.assertTrue(
            validate_preferences(self.preferences)
        )

    def test_invalid_energy(self):
        with self.assertRaises(ValueError):
            validate_preferences({
                "genre": "pop",
                "mood": "happy",
                "energy": 5
            })

    def test_recommendation_metrics(self):
        metrics = evaluate_recommendations(
            self.recommendations,
            self.preferences
        )

        self.assertAlmostEqual(
            metrics["genre_match_rate"],
            2 / 3
        )

        self.assertAlmostEqual(
            metrics["mood_match_rate"],
            2 / 3
        )

        self.assertTrue(
            metrics["quality_check_passed"]
        )

    def test_incorrect_recommendation_count(self):
        with self.assertRaises(ValueError):
            evaluate_recommendations(
                self.recommendations[:2],
                self.preferences
            )


if __name__ == "__main__":
    unittest.main()

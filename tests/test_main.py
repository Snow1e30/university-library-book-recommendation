"""Unit tests for the University Library Book Recommendation System."""

import unittest
import main


class RecommendationTests(unittest.TestCase):
    def setUp(self):
        self.requirements = {
            "programme": "B.Com",
            "semester": "Semester 4",
            "subject": "Advanced Corporate Accounting",
            "topic": "Consolidation",
            "level": "Intermediate",
            "purpose": "Reference",
        }

    def test_maximum_score_is_17(self):
        book = next(item for item in main.LIBRARY if item["book_id"] == "B001")
        self.assertEqual(main.calculate_score(book, self.requirements), 17)

    def test_case_insensitive_subject_matching(self):
        requirements = dict(self.requirements)
        requirements["subject"] = "advanced corporate accounting"
        book = next(item for item in main.LIBRARY if item["book_id"] == "B001")
        self.assertGreaterEqual(main.calculate_score(book, requirements), 5)

    def test_unavailable_book_does_not_get_availability_point(self):
        book = next(item for item in main.LIBRARY if item["book_id"] == "B003")
        score = main.calculate_score(book, self.requirements)
        self.assertLessEqual(score, 16)

    def test_recommendation_categories(self):
        self.assertEqual(main.recommendation_category(17), "Highly Recommended")
        self.assertEqual(main.recommendation_category(12), "Recommended")
        self.assertEqual(main.recommendation_category(8), "Moderately Relevant")
        self.assertEqual(main.recommendation_category(3), "Low Relevance")
        self.assertEqual(main.recommendation_category(0), "Not Relevant")

    def test_catalogue_has_at_least_20_books(self):
        self.assertGreaterEqual(len(main.LIBRARY), 20)

    def test_book_ids_are_unique(self):
        ids = [book["book_id"] for book in main.LIBRARY]
        self.assertEqual(len(ids), len(set(ids)))


if __name__ == "__main__":
    unittest.main()

import unittest

from app.services.calculator import (
    calculate_total,
    calculate_average,
    most_expensive_day,
    category_share,
)

EXPENSES = [
    {"day": 1, "category": "еда", "amount": 540},
    {"day": 1, "category": "транспорт", "amount": 260},
    {"day": 1, "category": "жильё", "amount": 1800},
    {"day": 2, "category": "еда", "amount": 720},
    {"day": 2, "category": "транспорт", "amount": 180},
    {"day": 2, "category": "жильё", "amount": 1800},
    {"day": 3, "category": "еда", "amount": 430},
    {"day": 3, "category": "транспорт", "amount": 95},
    {"day": 3, "category": "жильё", "amount": 1800},
    {"day": 3, "category": "еда", "amount": 275},
]


class TestCalculator(unittest.TestCase):

    def test_total(self):
        self.assertEqual(calculate_total(EXPENSES), 7900)

    def test_average(self):
        self.assertAlmostEqual(calculate_average(EXPENSES), 790.00, places=2)

    def test_most_expensive_day(self):
        self.assertEqual(most_expensive_day(EXPENSES), (2, 2700))

    def test_category_share_food(self):
        self.assertAlmostEqual(category_share(EXPENSES, "еда"), 24.87, places=2)

    def test_category_share_housing(self):
        self.assertAlmostEqual(category_share(EXPENSES, "жильё"), 68.35, places=2)

    def test_empty_list_total(self):
        self.assertEqual(calculate_total([]), 0)

    def test_empty_list_average(self):
        with self.assertRaises(ValueError):
            calculate_average([])

    def test_empty_list_most_expensive_day(self):
        with self.assertRaises(ValueError):
            most_expensive_day([])

    def test_empty_list_category_share(self):
        with self.assertRaises(ValueError):
            category_share([], "еда")

    def test_unknown_category(self):
        with self.assertRaises(ValueError):
            category_share(EXPENSES, "развлечения")


if __name__ == "__main__":
    unittest.main()
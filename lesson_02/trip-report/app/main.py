"""Точка входа: данные, вызовы расчётов, печать отчёта."""

from app.services.calculator import (
    calculate_total,
    calculate_average,
    most_expensive_day,
    category_share,
)
from app.utils.formatter import render_report

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


def main():
    total = calculate_total(EXPENSES)
    average = calculate_average(EXPENSES)
    expensive_day = most_expensive_day(EXPENSES)
    food_share = category_share(EXPENSES, "еда")
    housing_share = category_share(EXPENSES, "жильё")

    render_report(EXPENSES, total, average, expensive_day, food_share, housing_share)


if __name__ == "__main__":
    main()
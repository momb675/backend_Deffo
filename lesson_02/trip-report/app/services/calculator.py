"""Расчёты по расходам поездки. Ничего не печатает, только возвращает значения."""


def calculate_total(expenses):
    """Сумма всех трат."""
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total


def calculate_average(expenses):
    """Средняя трата. На пустом списке — ValueError."""
    if not expenses:
        raise ValueError("список расходов пуст")
    return calculate_total(expenses) / len(expenses)


def most_expensive_day(expenses):
    """Номер дня с самой большой суммой и сама сумма. На пустом списке — ValueError."""
    if not expenses:
        raise ValueError("список расходов пуст")

    totals_by_day = {}
    for expense in expenses:
        day = expense["day"]
        totals_by_day[day] = totals_by_day.get(day, 0) + expense["amount"]

    best_day = max(totals_by_day, key=totals_by_day.get)
    return best_day, totals_by_day[best_day]


def category_share(expenses, category):
    """Доля категории в общих тратах, в процентах. ValueError на пустом списке
    и на отсутствующей категории."""
    if not expenses:
        raise ValueError("список расходов пуст")

    total = calculate_total(expenses)
    category_total = 0
    found = False
    for expense in expenses:
        if expense["category"] == category:
            category_total += expense["amount"]
            found = True

    if not found:
        raise ValueError(f"категория не найдена: {category}")

    return category_total / total * 100
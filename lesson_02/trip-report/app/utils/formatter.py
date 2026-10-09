"""Оформление отчёта через Rich. Не считает — только рисует таблицу."""

from rich.console import Console
from rich.table import Table


def render_report(expenses, total, average, expensive_day, food_share, housing_share):
    """Печатает отчёт таблицей Rich."""
    console = Console()

    console.print("[bold]ОТЧЁТ ПО ПОЕЗДКЕ[/bold]")

    summary = Table(title="Сводка")
    summary.add_column("Показатель")
    summary.add_column("Значение", justify="right")
    summary.add_row("Записей", str(len(expenses)))
    summary.add_row("Всего потрачено", f"{total} ₽")
    summary.add_row("Средняя трата", f"{average:.2f} ₽")
    summary.add_row("Самый дорогой день", f"день {expensive_day[0]}, {expensive_day[1]} ₽")
    summary.add_row("Доля «еда»", f"{food_share:.2f} %")
    summary.add_row("Доля «жильё»", f"{housing_share:.2f} %")
    console.print(summary)
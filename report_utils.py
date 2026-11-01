import datetime as dt
from tabulate import tabulate


def monthly_report(expenses):

    current_month = dt.datetime.now().month
    current_year = dt.datetime.now().year

    monthly_expenses = []

    for expense in expenses:
        expense_date = dt.datetime.strptime(
            expense['date'], "%Y-%m-%d"
        )

        if expense_date.month == current_month and expense_date.year == current_year:
            monthly_expenses.append(expense)

    return monthly_expenses


def display_report(expenses, total, categories):

    print("\n===== MONTHLY EXPENSE REPORT =====")

    table = []

    for expense in expenses:
        table.append([
            expense['ref_id'],
            expense['date'],
            expense['description'],
            expense['category'],
            round(expense['amount'], 2)
        ])

    print(tabulate(
        table,
        headers=["Reference ID", "Date", "Description", "Category", "Amount"],
        tablefmt="grid"
    ))

    print("\nTotal Spending:", total)

    print("\nCategory-wise Spending:")

    for category, amount in categories.items():
        print(category, ":", amount)

    print("\nReport Month:", dt.datetime.now().strftime("%B %Y"))
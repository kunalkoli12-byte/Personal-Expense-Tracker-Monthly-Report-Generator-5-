import datetime
import random
import os
import expense_utils as eu
from report_utils import monthly_report, display_report


expenses = []


def add_expenses():

    n = int(input("Enter number of expenses: "))

    for i in range(n):

        description = input("\nEnter description: ")
        category = input("Enter category: ")

        while True:
            amount = float(input("Enter amount: "))

            if eu.validate_expense(amount):
                break
            else:
                print("Amount must be greater than zero.")

        while True:
            date = input("Enter date (YYYY-MM-DD, blank for today): ")

            if date == "":
                date = datetime.date.today().strftime("%Y-%m-%d")
                break

            try:
                datetime.datetime.strptime(date, "%Y-%m-%d")
                break
            except ValueError:
                print("Invalid date format. Try again.")

        ref_id = "EXP-" + str(random.randint(100000, 999999))

        expenses.append({
            'ref_id': ref_id,
            'description': description,
            'category': category,
            'amount': amount,
            'date': date
        })

        print("Reference ID:", ref_id)


def save_report(report_text):

    file_path = os.path.join(".", "monthly_report.txt")

    if os.path.exists(file_path):
        choice = input("Report already exists. Replace it? (yes/no): ")

        if choice.lower() != "yes":
            print("Report not saved.")
            return

    with open(file_path, "w") as file:
        file.write(report_text)

    print("Report saved successfully.")


def run_program():

    add_expenses()

    current_expenses = monthly_report(expenses)

    total = eu.calculate_total(current_expenses)

    categories = eu.category_total(current_expenses)

    display_report(current_expenses, total, categories)

    choice = input("\nDo you want to save the report? (yes/no): ")

    if choice.lower() == "yes":

        report_text = ""

        for expense in current_expenses:
            report_text += (
                f"{expense['ref_id']} | {expense['date']} | "
                f"{expense['description']} | {expense['category']} | "
                f"{expense['amount']}\n"
            )

        report_text += f"\nTotal Spending: {total}\n"

        for category, amount in categories.items():
            report_text += f"{category}: {amount}\n"

        save_report(report_text)


run_program()
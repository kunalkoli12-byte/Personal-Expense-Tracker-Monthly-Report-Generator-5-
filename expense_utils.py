import math

def validate_expense(amount):
    if amount <= 0 or not math.isfinite(amount):
        return False
    return True


def calculate_total(expenses):
    total = 0

    for expense in expenses:
        total += expense['amount']

    return round(total, 2)


def category_total(expenses):

    categories = {}

    for expense in expenses:
        category = expense['category']
        amount = expense['amount']

        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount

    for category in categories:
        categories[category] = round(categories[category], 2)

    return categories
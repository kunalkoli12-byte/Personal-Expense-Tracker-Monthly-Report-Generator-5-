from tabulate import tabulate

data = [
    ["Aman", "Food", 500],
    ["Riya", "Travel", 300]
]

print(tabulate(data, headers=["Name", "Category", "Amount"], tablefmt="grid"))
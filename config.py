budget_data = {}
budget_t = {}

def update_monthly_income(income):
    budget_t["monthly income"] = income

def calculate_totals():
    if "monthly income" not in budget_t or not budget_t["monthly income"].isdigit():
        print("Income not set or invalid")
        return

    total_expenses = sum(int(value) for value in budget_data.values() if value.isdigit())
    total_savings = int(budget_t["monthly income"]) - total_expenses
    budget_t["total expenses"] = total_expenses
    budget_t["total savings"] = total_savings
    print_budget_details()

def print_budget_details():
    details = {}
    for key, value in budget_data.items():
        details[key] = value
    for key, value in budget_t.items():
        details[key] = value
    return details




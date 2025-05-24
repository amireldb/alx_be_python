monthly_income = input("Enter your monthly income: ")
monthly_expenses = input("Enter your total monthly expenses: ")
monthly_savings = int(monthly_income) - int(monthly_expenses)
Projected_Savings = int(monthly_savings) * 12 + int(monthly_savings) * 12 * 0.05
print("Your monthly savings are $",monthly_savings)
print("Projected savings after one year, with interest, is: $",Projected_Savings)

# Personal Income Tax Calculator
income = float(input("Please input your annual income in thalers: "))
if income <= 85528:
    tax = income * 0.18 - 556.02
else:
    tax = 14839.02 + (income - 85528) * 0.32
# Ensure tax is not negative
if tax < 0:
    tax = 0
# Round to the nearest full thaler
tax = round(tax)
print("Your annual tax deduction is:", tax, "thalers")

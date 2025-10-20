print("Simple and Compound Interest Calculator")

# Input values
p = float(input("Enter principal amount: "))
r = float(input("Enter annual interest rate (%): "))
t = float(input("Enter time (in years): "))
n = int(input("Enter number of times interest is compounded per year: "))

# Convert rate to decimal
r = r / 100

# Simple Interest
simple_interest = p * r * t
print("Simple Interest:", simple_interest)

# Compound Interest
amount = p * (1 + r / n) ** (n * t)
compound_interest = amount - p
print("Compound Interest:", compound_interest)


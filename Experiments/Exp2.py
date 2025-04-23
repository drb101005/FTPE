#2.1
#Gross Salary
# Prompt the user to input the basic salary
basic_salary = float(input("Enter the basic salary (BS): "))
# Calculate allowances
dearness_allowance = 0.70 * basic_salary # 70% of basic salary
travel_allowance = 0.30 * basic_salary # 30% of basic salary
house_rent_allowance = 0.10 * basic_salary # 10% of basic salary
# Calculate gross salary
gross_salary = basic_salary + dearness_allowance + travel_allowance
+ house_rent_allowance
# Display the results
print("\n--- Salary Details ---")
print(f"Basic Salary (BS): {basic_salary}")
print(f"Dearness Allowance (DA): {dearness_allowance}")
print(f"Travel Allowance (TA): {travel_allowance}")
print(f"House Rent Allowance (HRA): {house_rent_allowance}")
print(f"Gross Salary: {gross_salary}")

#2.2
#Basic Arithmetic
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
# Perform arithmetic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
modulus = num1 % num2
# Display the results
print(f"Addition: {num1} + {num2} = {addition}")
print(f"Subtraction: {num1} - {num2} = {subtraction}")
print(f"Multiplication: {num1} * {num2} = {multiplication}")
print(f"Division: {num1} / {num2} = {division}")
print(f"Modulus: {num1} % {num2} = {modulus}")
# Ex034 - Salary Increase
# This program calculates the new salary of an employee based on their current salary.
# If the salary is less than or equal to R$1250, the increase is 15%.

salario = float(input("Enter the employee's salary: "))

# If the salary is greater than R$1250, the increase is 10%.

if salario <= 1250:
    aumento = salario * 0.15 # 15% increase
else:
    aumento = salario * 0.10 # 10% increase
novo_salario = salario + aumento

# Output the new salary

print(f"New salary: R$ {novo_salario:.2f}")
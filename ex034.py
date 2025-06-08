salario = float(input("Enter the employee's salary: "))
if salario <= 1250:
    aumento = salario * 0.15 # 15% increase
else:
    aumento = salario * 0.10 # 10% increase
novo_salario = salario + aumento
print(f"New salary: R$ {novo_salario:.2f}")
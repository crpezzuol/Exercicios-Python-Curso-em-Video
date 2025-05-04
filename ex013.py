salario = float(input("\nDigite o salário do funcionário: "))
aumento = float(input("Digite o percentual de aumento: "))
novo_salario = salario + (salario * aumento / 100)
print(f"\nUm funcionário que ganhava R$ {salario}, com {aumento:.2f}% de aumento, passa a ser: R$ {novo_salario:.2f}\n")
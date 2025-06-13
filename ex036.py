casa = int(input('Qual o valor da casa?: R$ '))
salario = int(input('Qual o salário do comprador?: R$ '))
anos = int(input('Em quantos anos pretende pagar?: '))
prestacao = casa / (anos * 12)  
if prestacao > (salario * 0.3):
    print(F'Empréstimo negado! A prestação de R$ {prestacao:.2f} ultrapassa 30% do seu salário.')
print('\n') # Início do exercício
# Exercício 036: Gerenciador de Pagamentos
print('=-' * 20 + ' Gerenciador de Pagamentos ' + '-=' * 20)
casa = int(input('Qual o valor da casa?: R$ '))
salario = int(input('Qual o salário do comprador?: R$ '))
anos = int(input('Em quantos anos pretende financiar?: '))
prestacao = casa / (anos * 12)
print('-' * 100)
print(f'Para pagar uma casa de R$ {casa:.2f} em {anos} anos, a prestação mensal será de R$ {prestacao:.2f}')
if prestacao > (salario * 0.3):
    print(F'Empréstimo negado! A prestação de R$ {prestacao:.2f} ultrapassa 30% do seu salário.')
else:
    print(F'Empréstimo aprovado! A prestação de R$ {prestacao:.2f} está dentro do limite de 30% do seu salário.')
print('-' * 100)
print('\n')
# Fim do exercício
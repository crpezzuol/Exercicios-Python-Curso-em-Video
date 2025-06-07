# Peça para o usuário digitar três números e mostre qual é o maior deles
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número: "))
maior = a 
if b > maior:
    maior = b
if c > maior:
    maior = c

print(f'O maior número é {maior}')
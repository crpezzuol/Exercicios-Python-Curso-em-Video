# Exemplo de código para verificar se uma frase é um palíndromo
import os

os.system('cls' if os.name == 'nt' else 'clear')

frase = input('Digite uma frase: ').replace(' ', '').upper()
print(f'O inverso de {frase} é {frase[::-1].upper()}')
# Verifica se a frase é um palíndromo
# A frase é um palíndromo se for igual à sua versão invertida
if frase == frase[::-1]:
    print('A frase é um palíndromo!')
else:
    print('A frase não é um palíndromo.')

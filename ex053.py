# Exemplo de código para verificar se uma frase é um palíndromo
# Exemplo de palindromos "A sadaca da casa" ou "A mala nada na lama"
# Exemplo de palíndromos "Apos a sopa" ou "A torre da derrota"
# Exemplo de palíndromos "A cara rajada da cara" ou "Anotava a data da avó"
# Exemplo de palíndromos "O lobo ama o bolo" ou "Anotaram a data da Maratona"

import os

os.system('cls' if os.name == 'nt' else 'clear')

frase = input('Digite uma frase: ').replace(' ', '').upper()
print(f'O inverso de {frase} é {frase[::-1].upper()}')
# Verifica se a frase é um palíndromo
# A frase é um palíndromo se for igual à sua versão invertida
if frase == frase[::-1]:
    print('A frase digitada é um palíndromo!')
else:
    print('A frase digitada não é um palíndromo.')

from random import randint
computador = randint(0, 5) # computador sorteia um número entre 0 e 5
print('-=-' * 20)
print('| Vou pensar em um número entre 0 e 5.  Tente adivinhar... |')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? (0 a 5): ')) # jopgador tenta adivinhar o número
if jogador < 0 or jogador > 5:
    print('Número inválido! Tente novamente.')

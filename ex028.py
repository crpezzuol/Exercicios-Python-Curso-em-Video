from random import randint
computador = randint(0, 5) # computador sorteia um número entre 0 e 5
print('-=-' * 20)
print('| Vou pensar em um número entre 0 e 5.  Tente adivinhar... |')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? (0 a 5): ')) # jopgador tenta adivinhar o número
if jogador == computador:
    print('Parabéns! Você conseguiu me vencer!')
else:
    print(f'Ganhei! Eu pensei no número {computador} e não no {jogador}.')


from random import randint
from time import sleep 
computador = randint(0, 5) # computador sorteia um número entre 0 e 5
print('-=-' * 20)
print('| Vou pensar em um número entre 0 e 5.  Tente adivinhar... |')
print('-=-' * 20,'\n')
jogador = int(input('Em que número eu pensei? (0 a 5): ')) # jopgador tenta adivinhar o número
print('\nPROCESSANDO...')
sleep(2) # espera 2 segundos para mostrar o resultado
if jogador == computador:
    print('\nParabéns! Você conseguiu me vencer!\n')
    print(f'Eu pensei no número {computador} e você acertou!\n')
else:
    print(f'\nGanhei! Eu pensei no número {computador} e não no {jogador}.\n')

from random import randint
computador = randint(0, 5) # sorteia um número entre 0 e 5
jogador = int(input('Tente adivinhar o número que estou pensando entre 0 e 5: '))
if jogador < 0 or jogador > 5:
    print('Número inválido! Tente novamente.')

# aula14
'''
for c in range(1, 10):
    print(c)
print('Fim do loop')
'''

'''c  = 1
while c < 10:
    print(c)
    c += 1
print('Fim do loop')
'''

'''
for n in range(1, 5):
    n = int(input('Digite um número: '))
print('Fim')
'''

'''
n = 1
while n != 0:
    n = int(input('Digite um número: '))
print('Fim')
'''

'''
r = 's'
while r == 's':
    n = int(input('Digite um número: '))
    r = str(input('Quer continuar? [S/N] ')).strip().lower()
print('Fim')
'''


n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um número (0 para sair): '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares e {impar} números ímpares')
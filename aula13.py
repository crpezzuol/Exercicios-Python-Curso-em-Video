# imprimindo uma mensagem 6 vezes
print('\n')
print('imprimindo uma mensagem 6 vezes')
for c in range (0, 6):
    print('Oi!', c)
print('Fim')

# imprimindo uma mensagem 5 vezes
print('\n')
print('imprimindo uma mensagem 5 vezes')
for c in range (1, 6):
    print('Oi!', c)
print('Fim')

# imprimindo uma mensagem 6 vezes de trás para frente
print('\n')
print('imprimindo uma mensagem 6 vezes de trás para frente')
for c in range (6, 0, -1):
    print('Oi!', c)
print('Fim')

# imprimindo uma mensagem pulando de 2 em 2
print('\n')
print('imprimindo uma mensagem pulando de 2 em 2')
for c in range (0, 7, 2):
    print('Oi!', c)
print('Fim')

# imprimindo uma mensagem com números digitados pelo usuário
print('\n')
print('imprimindo uma mensagem com números digitados pelo usuário')
i = int(input('Digite o início: '))
f = int(input('Digite o fim: '))
p = int(input('Digite o passo: '))
if i > f:
    p = -p  # se o início for maior que o fim, o passo será negativo
for c in range(i, f+1 , p):
    print(c)

# imprimindo a somatória de números digitados pelo usuário
print('\n')
print('imprimindo a somatória de números digitados pelo usuário')
s = 0
for c in range(1, 4):
    n = int(input(f'Digite o {c}º número: '))
    s += n  # s = s + n
print(f'A soma dos números digitados é: {s}')


print('\n' * 3)


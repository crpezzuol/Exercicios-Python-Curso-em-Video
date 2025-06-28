# ex049
print('\n' * 3)
print('\033[1;31]=' * 20, 'TABUADA', '=' * 20)
print('\n')
num = int(input('Digite um número para ver sua tabuada: '))
print('\n')
for c in range(1, 11):
    print(f'{num} x {c:2} = {num * c:3}')
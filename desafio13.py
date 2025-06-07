# Peça para o usuário digitar um número e diga se ele é primo.
numero = int(input("Digite um número: "))
def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
if eh_primo(numero):
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")

# solução alternativa
    num = int(input('Digite um número: '))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(f'{num} não é primo.')
            break
    else:
        print(f'{num} é primo.')
else:
    print('Números menores ou iguais a 1 não são primos.')
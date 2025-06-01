frase = input('Digite uma Frase: ')
print(frase)
print(frase[9])  # Imprime o caractere na posição 9
print(frase[9:13])  # Imprime os caracteres da posição 9 até a 12
print(frase[9:13:2])  # Imprime os caracteres da posição 9 até a 12, pulando de 2 em 2  
print(frase[9::3])  # Imprime os caracteres da posição 9 até o final, pulando de 3 em 3
print(frase[:5])  # Imprime os caracteres do início até a posição 4
print(frase[15:])  # Imprime os caracteres da posição 15 até o final
print(frase[9::])  # Imprime os caracteres da posição 9 até o final
print(frase[9:13:2])  # Imprime os caracteres da posição 9 até a 12, pulando de 2 em 2
print(frase.count('o'))  # Conta quantas vezes o caractere 'o' aparece na frase
print(frase.count('o', 0, 13))  # Conta quantas vezes o caractere 'o' aparece na frase do início até a posição 12
print(frase.find('deo'))  # Encontra a posição da substring 'deo' na frase
print(frase.find('Android'))  # Retorna -1 se a substring não for encontrada
print('Curso' in frase)  # Verifica se a substring 'Curso' está presente na frase
print(frase.replace('Python', 'Android'))  # Substitui 'Python' por 'Android' na frase
print(frase.upper())  # Converte toda a frase para maiúsculas
print(frase.lower())  # Converte toda a frase para minúsculas
print(frase.capitalize())  # Converte a primeira letra da frase para maiúscula
print(frase.title())  # Converte a primeira letra de cada palavra para maiúscula
print(frase.strip())  # Remove espaços no início e no final da frase
print(frase.rstrip())  # Remove espaços no final da frase
print(frase.lstrip())  # Remove espaços no início da frase
print(frase.split())  # Divide a frase em uma lista de palavras
print('-'.join(frase))  # Junta os caracteres da frase com '-' entre eles
dividido = frase.split()
print(dividido)  # Imprime a lista de palavras resultante da divisão da frase
print(dividido[0])  # Imprime a primeira palavra da lista
print(dividido[1])  # Imprime a segunda palavra da lista
print(dividido[2] [2])  # Imprime o terceiro caractere da terceira palavra da lista
print(dividido[2][2:5])  # Imprime os caracteres da terceira palavra da lista, da posição 2 até a 4
print(dividido[2][2:5:2])  # Imprime os caracteres da terceira palavra da lista, da posição 2 até a 4, pulando de 2 em 2

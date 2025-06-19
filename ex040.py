import os   

os.system('cls' if os.name == 'nt' else 'clear')

print('\033[34m<>\033[m' * 30)
print('\n')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
print('\n')
media = (nota1 + nota2) / 2
print(f'Tirando {nota1} e {nota2}, a média do aluno é {media}')

if media < 5:
    print('O Aluno está \033[1;31mREPROVADO!\033[m')
elif media < 7:
    print('O Aluno está de \033[1;33mRECUPERAÇÃO!\033[m')
else:
    print('O Aluno está \033[1;32mAPROVADO!\033[m')

print('\n')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print(f'Tirando {nota1} e {nota2}, a média do aluno é {media}')

if media < 5:
    print('O Aluno está \033[1;31mREPROVADO!\033[m')
elif media < 6.9:
    print('O Aluno está de \033[1;33mRECUPERAÇÃO!\033[m')
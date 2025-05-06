from random import choice
n1 = input("\nDigite o nome do aluno 1: ")
n2 = input("Digite o nome do aluno 2: ")
n3 = input("Digite o nome do aluno 3: ")
n4 = input("Digite o nome do aluno 4: ")
lista = [n1, n2, n3, n4]
aluno = choice(lista)
print(f"\nOs alunos são: {n1}, {n2}, {n3} e {n4}.")
print(f"O aluno escolhido foi: {aluno}.\n")

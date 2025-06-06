# Peça para o usuário digitar uma nota de 0 a 10 e informe se ele foi aprovado (nota maior ou igual a 6) ou reprovado
nota = float(input("Digite uma nota de 0 a 10: "))
if nota >= 6:
    print("Aprovado")
else:
    print("Reprovado")
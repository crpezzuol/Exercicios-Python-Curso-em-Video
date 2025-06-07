# Peça para o usuário digitar um ano e informe se ele é bissexto ou não.
ano = int(input("Digite um ano: "))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"{ano} é um ano bissexto.")
else:
    print(f"{ano} não é um ano bissexto.")
'''Essa condição em Python é usada para determinar se um ano é bissexto ou não. Vamos destrinchar:
- ano % 4 == 0 → O ano deve ser divisível por 4.
- ano % 100 != 0 → Se for divisível por 100, não é bissexto (exceção).
- ano % 400 == 0 → Se for divisível por 400, é bissexto, independentemente da regra anterior.
Ou seja, um ano é bissexto se:
- For divisível por 4, mas não por 100, ou
- For divisível por 400.
Exemplos:
- 2024 → Bissexto (divisível por 4 e não por 100).
- 1900 → Não bissexto (divisível por 4, mas também por 100 e não por 400).
- 2000 → Bissexto (divisível por 400).'''

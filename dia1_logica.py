# dia1_logica.py
# Trilha de Analista de Dados — Dia 1
# 🐍 Tema: Lógica de Programação com Python

print("=== DIA 1 — LÓGICA EM PYTHON ===\n")

# 1️⃣ Verifica se um número é par ou ímpar
def par_ou_impar():
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        print("🔢 O número é par.")
    else:
        print("🔢 O número é ímpar.")

# par_ou_impar()


# 2️⃣ Encontra o maior entre três números
def maior_de_tres():
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))
    c = int(input("Digite o terceiro número: "))
    if a >= b and a >= c:
        maior = a
    elif b >= a and b >= c:
        maior = b
    else:
        maior = c
    print(f"🏆 O maior número é: {maior}")

# maior_de_tres()


# 3️⃣ Calculadora simples
def calculadora():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação (+, -, *, /): ")

    if operacao == "+":
        print(f"🧮 Resultado: {num1 + num2}")
    elif operacao == "-":
        print(f"🧮 Resultado: {num1 - num2}")
    elif operacao == "*":
        print(f"🧮 Resultado: {num1 * num2}")
    elif operacao == "/":
        if num2 != 0:
            print(f"🧮 Resultado: {num1 / num2}")
        else:
            print("🚫 Erro: divisão por zero!")
    else:
        print("❌ Operação inválida.")

# calculadora()


# 4️⃣ Tabuada de um número
def tabuada():
    numero = int(input("Digite um número para ver a tabuada: "))
    print(f"📚 Tabuada de {numero}")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# tabuada()


# 5️⃣ Verifica se o número é primo
def numero_primo():
    num = int(input("Digite um número: "))
    if num < 2:
        print("❌ Não é primo.")
        return
    primo = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            primo = False
            break
    print("✅ É primo!" if primo else "❌ Não é primo.")

# numero_primo()
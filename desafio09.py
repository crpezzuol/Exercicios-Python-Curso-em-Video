# Peça para o usuário digitar uma senha e informe se ela está correta (por exemplo, a senha correta é "python123").
senha_correta = "python123"
senha_usuario = str(input("Digite a senha: "))
if senha_usuario == senha_correta:
    print("Senha correta!") 
else:
    print("Senha incorreta! Você tem mais 2 chances tente novamente.")
    senha_usuario = str(input("Digite a senha: "))
    if senha_usuario == senha_correta:
        print("Senha correta!")
    else:
        print("Senha incorreta! Você tem mais 1 chance tente novamente.")
        senha_usuario = str(input("Digite a senha: "))
        if senha_usuario == senha_correta:
            print("Senha correta!")
        else:
            print("Senha incorreta! Você não tem mais chances.")
            print("Acesso negado.")
            print("A senha correta é:", senha_correta)
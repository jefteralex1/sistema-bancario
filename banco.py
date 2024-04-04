menu = """
[c] Criar conta
[e] Entrar na conta
[d] Depositar
[s] Sacar
[x] Extrato
[q] Sair
[v] Verificar saldo

=> """
conta = ""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "c":
        conta = input("Digite seu CPF para criar a sua conta: ")
        print("Conta criada com sucesso!")

    elif opcao == "e":
        cpf = input("Digite o seu CPF: ")
        if cpf == conta:
            print("Login bem-sucedido!")
        else:
            print("CPF incorreto! Por favor, tente novamente.")

    elif opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "x":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
    
    elif opcao == "v":
        print(f"Seu saldo atual é: R$ {saldo:.2f}")

    elif opcao == "q":
        print("Sessão encerrada.")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

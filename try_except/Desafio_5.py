while True:
    try:
        Saldo = float(input("Digite o seu saldo: "))
        saque = float(input("Digite o valor do saque: "))
        if saque > Saldo:
            print("Saldo insuficiente para realizar o saque.")
        else:
            Saldo -= saque
            print(f"Saque realizado com sucesso! Novo saldo: R${Saldo:.2f}")
        break
    except:
        print("Erro: Digite apenas valores numericos!")
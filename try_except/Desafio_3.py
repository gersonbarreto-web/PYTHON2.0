while True :
    try:
        numero = int(input("Digite um número pra ver a tabuada: "))
        for i in range(1, 11):
            resultado = numero * i
            print(f"{numero} x {i} = {resultado}")
        break
    except:
        print("Erro: Digite apenas numeros!")
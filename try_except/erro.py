
while True: 
    try:   
    
        idade = int(input("Digite sua idade: "))
        if (idade>=18):
            print("Você é maior de idade.")
            break
        else:
            print("Você é menor de idade.")
        break
    except:
        print("Ocorreu um erro. Por favor, insira um número válido para a idade.")
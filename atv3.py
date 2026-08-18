# Criando a variável temperatura (pode testar com valores decimais ou inteiros)
temperatura = int(input("Digite a temperatura atual: "))

# Estrutura condicional
if temperatura < 15:
    print("Está frio")
elif 15 <= temperatura <= 25:
    print("Está agradável")
else:
    print("Está quente")
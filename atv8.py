# Solicita os dois números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Solicita a operação desejada
print("\nEscolha a operação:")
print("+ : Adição")
print("- : Subtração")
print("* : Multiplicação")
print("/ : Divisão")
operacao = input("Digite o símbolo da operação (+, -, * ou /): ")

# Estrutura condicional para executar a operação correta
if operacao == "+":
    resultado = num1 + num2
    print(f"\nResultado: {num1} + {num2} = {resultado}")

elif operacao == "-":
    resultado = num1 - num2
    print(f"\nResultado: {num1} - {num2} = {resultado}")

elif operacao == "*":
    resultado = num1 * num2
    print(f"\nResultado: {num1} * {num2} = {resultado}")

elif operacao == "/":
    # Tratamento para evitar divisão por zero
    if num2 != 0:
        resultado = num1 / num2
        print(f"\nResultado: {num1} / {num2} = {resultado}")
    else:
        print("\nErro: Não é possível dividir por zero!")

else:
    print("\nOperação inválida! Por favor, escolha +, -, * ou /.")
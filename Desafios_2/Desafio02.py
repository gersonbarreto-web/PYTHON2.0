lista =[]

for x in range(5):
    produto = input(f"Digite o nome do {x+1} produto :")
    lista.append(produto)

print("Produtos cadastrados:")
for produto in lista:
    print(produto)
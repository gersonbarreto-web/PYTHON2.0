lista = []


for i in range(6):
    n = int(input(f"Digite o {i+1}º número: "))
    lista.append(n)


lista.sort()


soma = sum(lista)
maior = max(lista)
menor = min(lista)


print(f"\nNúmeros em ordem crescente: {lista}")
print(f"Soma de todos os números: {soma}")
print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")
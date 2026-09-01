
lista = []


while True:
    nomes = input("Digite um nome (ou 'fim' para encerrar): ")

   
    if nomes.lower() == "fim":
        break
    else:
        
        lista.append(nomes)


lista.sort()



quantidades = len(lista)


print(f"\nLista de nomes em ordem alfabética: {lista}")
print(f"A quantidade de nomes digitados é {quantidades}")
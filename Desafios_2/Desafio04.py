numeros = [12,7,9, 20, 31, 44, 18, 5]

par = []
impar = []

for numero in numeros:
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

print(f"Números pares: {par}")
print(f"Números ímpares: {impar}")
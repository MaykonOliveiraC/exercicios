# Inicializamos duas listas vazias para os valores pares e ímpares
numeros_pares = []
numeros_impares = []

# Iteramos para receber 7 números
for _ in range(7):
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)

# Combinamos as listas de pares e ímpares
numeros = numeros_pares + numeros_impares

print("Lista de números pares:", numeros_pares)
print("Lista de números ímpares:", numeros_impares)
print("Lista completa:", numeros)

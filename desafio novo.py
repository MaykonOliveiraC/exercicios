soma = 0
for i in range(10):
    numero = int(input("Digite um número inteiro: "))
    if numero % 2 != 0:
        soma += numero
print(f"A soma de todos os números impares são: {soma}")

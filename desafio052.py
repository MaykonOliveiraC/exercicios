ponto_de_parada = 0
soma = 0
contador = 0
while ponto_de_parada != 999:
    ponto_de_parada = int(input("Digite um número: "))
    if ponto_de_parada == 999:
        break
    contador += 1
    soma += ponto_de_parada
print(f"Você digitou {contador} numeros, e a soma entre eles foi {soma}")








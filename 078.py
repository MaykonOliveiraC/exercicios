valores = list()
for cont in range(0, 5):
    valores.append(int(input("digite um valor: ")))
valor_max = max(valores)
valor_min = min(valores)
indice_max = valores.index(valor_max)
indice_min = valores.index(valor_min)
print(f"O maior de sua lista foi {valor_max} e está na posição {indice_max}")
print(f"O menor de sua lista foi {valor_min} e está na posição {indice_min}")

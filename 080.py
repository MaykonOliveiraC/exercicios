valores = list()

for _ in range(0, 5):
    contagem = int(input("Digite um valor: "))

    for i in range(len(valores)):
        if contagem < valores[i]:
            valores.insert(i, contagem)
            break
    else:
        valores.append(contagem)

print(f"A lista final em ordem é {valores}")




preço_mais_alto = 0
cond = 'S'
soma = 0
contagem_preço = 0
preço_mais_baixo = 10000000000
while cond == 'S':
    nome_produto = str(input("Qual nome do produto?: "))
    preço_produto = float(input("Preço do produto: R$ "))
    soma += preço_produto
    cond = str(input("Deseja continuar? [S/N]"))
    if preço_produto < preço_mais_baixo:
        preço_mais_baixo = preço_produto
        nome_mais_barato = nome_produto
    if preço_produto > 1000:
        preço_mais_alto += 1
    if cond != 'S':
        break
print(f"O total gasto na compra foi {soma}.")
print(f"{contagem_preço} produtos custam mais que 1000$.")
print(f"O produto mais barato foi {nome_mais_barato} e custou {preço_mais_baixo}.")
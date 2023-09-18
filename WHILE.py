preço_mais_alto = 0
cond = 'S'
soma = 0
contagem_preço = 0
preç

while cond == 'S':
    nome_produto = str(input("Qual nome do produto?: "))
    preço_produto = int(input("Preço do produto: R$ "))
    soma += preço_produto
    cond = str(input("Deseja continuar? [S/N]"))
    if preço_produto > 1000:
        preço_mais_alto += 1

    if cond != 'S':
        break

print(f"O total gasto na compra foi R$ {soma}.")
print(f"{preço_mais_alto} produtos custam mais que R$ 1000.")

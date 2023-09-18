preço = float(input("Qual o preço do produto? R$"))
desconto = 5
valor_desconto = preço * desconto / 100
total = preço - valor_desconto
print(f"O novo preço será de {total} $.")
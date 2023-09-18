valor_casa = float(input("Qual o valor da casa?"))
valor_salario = float(input("Qual o valor do seu sálario?"))
anos_parcela = int(input("Em quantos anos irá pagar a casa?"))
valor_mensal = valor_casa / (anos_parcela * 12)
limite = valor_salario * 30 / 100

if valor_mensal <= limite:
    print(f"Empréstimo aprovado!")
    print(f"Prestação mensal: {valor_mensal: .3f} R$")
else:
    print("Empréstimo negado pois a prestação excede 30% do seu sálario.")
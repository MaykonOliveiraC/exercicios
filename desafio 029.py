velocidade = int(input("Qual a velocidade do carro?: "))
multa = 0
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f"Você foi multado!")
    print(f"Você deve pagar uma multa de {multa: .2f}.")
else:
    print(f"Você está dirigindo conforme a lei, parabéns!")

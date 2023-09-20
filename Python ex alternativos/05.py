altura = float(input("Digite sua altura pequeno gafanhoto: "))
sexo = input("Digite seu sexo: [M/F]")
if sexo == 'M' or sexo == 'm':
    peso_ideal = (72.7 * altura) - 58
if sexo == 'F' or sexo == 'f':
    	peso_ideal = (62.1 * altura) - 44.7
print(f"Seu peso ideal é {peso_ideal:.2f}")


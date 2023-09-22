salario = int(input("Qual seu salário?: "))
aumento_percentual = 10
valor_aumentado = salario * (1 + aumento_percentual / 100)
segundo_aumento = 15
valor2_aumentado = salario * (1+ segundo_aumento / 100)
if salario > 1250:
    print(f"Seu salário com 10% de aumento será: {valor_aumentado: .2f}")
else:
    print(f"Seu salário com 15% de aumento será: {valor2_aumentado: .2f}")

\033[0;33;44m]



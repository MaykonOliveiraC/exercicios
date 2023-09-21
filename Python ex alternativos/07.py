salario_hora = int(input("Quanto você ganha por hora? R$: "))
horas_mes = int(input("Quantas horas você trabalha por Mês. "))
salario_bruto = salario_hora * horas_mes 
imposto_de_renda = salario_bruto * (11 / 100)
inss = salario_bruto * (8 / 100)
sindicato = salario_bruto * (5 / 100)
descontos = imposto_de_renda + inss + sindicato
salario_liquido = salario_bruto - descontos

print(f"Seu sálario bruto é R$ {salario_bruto}.")
print(f"O valor descontado do INSS é R$ {inss}.")
print(f"O valor descontado pelo sindicato é {sindicato}")
print(f"O valor líquido de seu sálario é {salario_liquido} ")
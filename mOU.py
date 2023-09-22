trimestre1 = float(input("Qual sua nota do primeiro trimestre?: "))
trimestre2 = float(input("Qual sua nota do segundo trimestre?: "))
trimestre3 = float(input("Qual sua nota do terceito trimestre?: "))
resultado = float ((trimestre1 + trimestre2 + trimestre3) /3)
if resultado >= 6.0:
    print(f"VOCÊ TEM {resultado: .2f} DE MÉDIA E ESTÁ APROVADO. ")

else:
    print(f"VOCÊ TEM {resultado: .2f} DE MÉDIA E ESTÁ REPROVADO.  ")





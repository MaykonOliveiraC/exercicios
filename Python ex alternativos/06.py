peso_peixe = float(input("Digite o valor em pesos de peixe adquiridos: "))
limite = 50
taxa_por_kg_extra = 4
if peso_peixe > limite:
    peso_extra = peso_peixe - limite
    taxa_total = peso_extra * taxa_por_kg_extra 
    print(f"Foi aplicada uma multa de {taxa_total}")
else:
    print("não foi aplicada nenhuma multa.")


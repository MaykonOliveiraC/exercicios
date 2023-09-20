notas = []
for i in range (4):
    nota = float(input(f"Digite a {i + 1}a nota. "))
    notas.append(nota)
soma_notas = sum(notas)
media_notas = soma_notas / 4
print(f"A média entre as notas nos 4 bimestres são: {media_notas}")
    
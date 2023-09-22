distancia = int(input("Qual é a distancia da viagem em km?: "))
km = 0.50
km_longos = 0.45
passagem = distancia * km
passagem_longa = distancia * km_longos
if passagem <= 200:
    print(f" você está prestes a começar uma viagem de {distancia}Km.")
    print(f" E pagará {passagem: .2f}")
else:
    print(f"Você está prestes a começar uma viagem de {distancia}Km.")
    print(f"E irá pagar {passagem_longa: .2f} .")



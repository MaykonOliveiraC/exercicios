valores = list()
continuar = True
while continuar:
    valores.append(int(input("Digite um valor: ")))
    resposta = input('Se deseja continuar, digite >sim<: ').lower()
    if resposta != 'sim':
        continuar = False
if resposta in valores:
    valores.pop()
print(f'{valores.sort()}')



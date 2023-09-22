lista_precos = [500, 1500, 2000, 100, 25]
nova_lista2 = [preco * 0.5 for preco in lista_precos if preco > 1000]
print(nova_lista2)
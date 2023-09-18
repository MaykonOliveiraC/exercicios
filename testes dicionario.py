produtos = {"iphone": 7000, "ipad": 11000, "airpod": 2500}
novos_produtos = {"Celular": 3000,"Monitor": 5000}
produtos = produtos | novos_produtos
for produto in produtos:
    print(produtos[produto])


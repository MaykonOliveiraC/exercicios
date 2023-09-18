nome = str(input("Digite seu nome completo: "))
nomes = nome.split()
if len(nomes) > 0:
    primeiro_nome = nomes [0]
    ultimo_nome = nomes [-1]
    print(f"Muito prazer em te conhecer! ")
    print(f"Seu primeiro nome é {primeiro_nome}. ")
    print(f"Seu último nome é {ultimo_nome}. ")
else:
    print(f"Nome Inválido. ")

# Inicializa a lista de pessoas
pessoas = []

# Pede ao usuário para inserir as informações das pessoas
while True:
    nome = input("Digite o nome da pessoa: ")
    peso = float(input("Digite o peso da pessoa em kg: "))

    # Adiciona o nome e peso como uma lista dentro da lista 'pessoas'
    pessoas.append([nome, peso])

    continuar = input("Deseja adicionar outra pessoa? (s/n): ")
    if continuar.lower() != 's':
        break

# Encontra o peso máximo e mínimo
peso_maximo = max(pessoa[1] for pessoa in pessoas)
peso_minimo = min(pessoa[1] for pessoa in pessoas)

# Exibe a lista de pessoas
print("\nLista de pessoas:")
for pessoa in pessoas:
    print(f"Nome: {pessoa[0]}, Peso: {pessoa[1]} kg")

# Imprime o número de pessoas cadastradas
print(f"\nForam cadastradas {len(pessoas)} pessoas.")

# Lista os nomes das pessoas mais pesadas e mais leves
print("\nPessoas mais pesadas:")
for pessoa in pessoas:
    if pessoa[1] == peso_maximo:
        print(pessoa[0])

print("\nPessoas mais leves:")
for pessoa in pessoas:
    if pessoa[1] == peso_minimo:
        print(pessoa[0])

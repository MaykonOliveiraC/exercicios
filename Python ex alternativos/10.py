perguntas = [
    'Telefonou para a vítima?',
    'Esteve no local do crime?',
    'Mora perto da vítima?',
    'Devia para a vítima?',
    'Já trabalhou com a vítima?'
]
respostas = []
for pergunta in perguntas:
    resposta = input(pergunta + '(sim/não):')
    respostas.append(resposta)
print('respostas registradas: ')
for i, resposta in enumerate(respostas):
        print(f"Pergunta {i+1}: {resposta}")
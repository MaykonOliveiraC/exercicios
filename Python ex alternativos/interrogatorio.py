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
positivas = respostas.count('sim')
if positivas < 2:
    classificacao = 'Inocente'
elif positivas == 2:
     classificacao = 'Suspeito'
elif 3 <= positivas <= 4:
     classificacao = 'Cumplice'
elif positivas == 5:
     classificacao = 'Assasino'
print(f"Segundo os metódos de análise você é considerado um {classificacao}")
print(positivas)

nome = str(input("Qual seu nome todo? "))
nome_maiusculo = nome.upper()
nome_minusculo = nome.lower()
contador_de_letras = len([caractere for caractere in nome if caractere.isalpha()])
primeira_palavra = nome.split()
primeiro_nome = primeira_palavra[0]
quantidade_letras = len(primeiro_nome)
print(f"{nome_maiusculo} \n{nome_minusculo} \n{contador_de_letras} \n{quantidade_letras}.")


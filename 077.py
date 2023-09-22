tupla = ('lapis', 'borracha', 'caneta', 'bag', 'seda', 'piteira')
vogais = ['a', 'e','i', 'o', 'u']
for palavra in tupla:
    print(f'Vogais em "{palavra}": ')
    for letra in palavra:
        if letra.lower() in vogais:
            print(letra)










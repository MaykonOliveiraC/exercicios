frase = str(input("digite uma frase: ")).upper()
letra = "A"
quantidade_a = frase.count(letra)
if quantidade_a > 0:
    primeira_posição = frase.index("A") + 1
    ultima_posiçao = frase.rfind("A")
    print(f"A letra A aparece {quantidade_a} vezes na frase. ")
    print(f"A primeira letra A apareceu na posição {primeira_posição}. ")
    print(f"A ultima letra A apareceu na posição {ultima_posiçao}. ")
else:
    print(f"A letra {letra} não aparece na frase. ")





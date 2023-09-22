import random
numero_usuario = int(input("Digite um número de 0 a 5: "))
if random.randint(0,6) == numero_usuario:
    print(f"Você Acertou!")
else:
    print(f"Você Errou!")




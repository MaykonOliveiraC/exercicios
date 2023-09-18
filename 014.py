num_total = int(input("Digíte um numero inteiro: "))
unidade = num_total % 10
dezena = (num_total // 10) % 10
centena = (num_total // 100) % 10
milhar = num_total // 1000
print(f"milhar: {milhar}")
print(f"centena: {centena}")
print(f"dezena: {dezena}")
print(f"unidade: {unidade}")

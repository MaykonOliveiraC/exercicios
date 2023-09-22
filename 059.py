while True:
    try:
        escolha1 = int(input("Digite o primeiro número: "))
        escolha2 = int(input("Digite outro número: "))

        while True:
            print('----Bem Vindo ao Menu----')
            print('[1] Somar')
            print('[2] Multiplicar')
            print('[3] Maior')
            print('[4] Novos números')
            print('[5] Sair do programa')

            opcao = int(input('Escolha uma opção: '))

            if opcao == 1:
                resultado_soma = escolha1 + escolha2
                print(f'A soma dos seus valores é: {resultado_soma}')
            elif opcao == 2:
                resultado_mult = escolha1 * escolha2
                print(f'A multiplicação de seus valores é: {resultado_mult}.')
            elif opcao == 3:
                if escolha1 > escolha2:
                    print(f'O maior número é: {escolha1}')
                else:
                    print(f'O maior número é: {escolha2}')
            elif opcao == 4:
                print("Digite novamente os números: ")
                escolha1 = int(input("Primeiro número: "))
                escolha2 = int(input("Segundo número: "))
            elif opcao == 5:
                print('Finalizando o programa...')
                break
            else:
                print("Opção inválida. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Certifique-se de inserir números inteiros.")

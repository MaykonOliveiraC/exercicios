nome = input("\033[0;30;46mQual o seu nome?\033[0m")
if nome.lower()  == 'maykon':
    print(f'\033[4;33;40mOlá Maykon, seu nome é extremamente bonito e você tem um pinto enorme. \033[0m')
elif nome.lower() == 'matheus' or 'rafael' or 'igor':
    print(f'\033[0;30;46mVejo que vc é um degoliano de nascença.\033[0m')
elif nome.lower() == 'ana' or 'giovanna' or 'marcela':
    print(f'ótimos nomes.')
print(f"\033[4;33;40mTenha um bom dia, {nome}. \033[0m")
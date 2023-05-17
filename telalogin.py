print(''' BEM VINDO A TELA DE LOGIN!!! ''')

usuario = input('Por favor digite o nome do usuário: ')
senha = input('Digite sua senha: ')
usuario_cadastrado = 'mauricio12'
senha_cadastrada = '90oi'

tentativa = 0
if usuario == usuario_cadastrado and senha == senha_cadastrada:
    print("Login Valido!")
else:
    tentativa += 1
    print('Usuario ou senha invalidos!')
    if tentativa == 3:
        print("Houve 3 tentativas redefina sua senha!")
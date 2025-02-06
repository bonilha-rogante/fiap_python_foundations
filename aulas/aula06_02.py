def saudacao(nome_usuario='Usuário'):
    print(f'Olá, {nome_usuario}!')


nome = input('Digite seu nome: ')
if nome == '':
    saudacao()
else:
    saudacao(nome)
    
outro_nome = input('Digite seu nome: ')

if outro_nome == '':
    saudacao()
else:
    saudacao(outro_nome)

print('Fim do programa!')    
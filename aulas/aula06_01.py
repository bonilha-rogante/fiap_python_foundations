def saudacao():
    while True:
        print('Olá, mundo')
        opcao = input('Deseja continuar? ')
        if opcao != 's':
            return
    print('Fim da saudacao()')

resultado = saudacao()
print(resultado)

print('fim do programa')
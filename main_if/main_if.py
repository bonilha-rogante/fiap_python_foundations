menu_principal = """[Menu Principal] Escolha uma das seguintes opções:
1 - Categorias
2 - Editoras
3 - Autores
4 - Livros
0 - Sair do programa
"""

menu_autores = """
[Autores] Escolha uma das seguintes opções:
1 - Listar todos os autores
2 - Adicionar novo autor
3 - Excluir autor
4 - Ver autor por Id
0 - Voltar ao menu anterior
"""

menu_editoras = """
[Editoras] Escolha uma das seguintes opções:
1 - Listar todas as editoras
2 - Adicionar nova editora
3 - Excluir editora
4 - Ver editora por Id
0 - Voltar ao menu anterior
"""

tabela_autores = []
tabela_editoras = []

while True:
    print(menu_principal)

    print()  # Uma linha vazia.

    opcao_principal = input('Digite a opção: ')
    
    if opcao_principal == '2':
        while True:
            print(menu_editoras)
            opcao_editoras = input('Digite a opção: ')
            if opcao_editoras == '0':
                break
            elif opcao_editoras == '1':
                if tabela_editoras == []:
                    print('Nenhuma editora cadastrada.')
                else:
                    print('ID | Nome | Endereço | Telefone')
                    for index, editora in enumerate(tabela_editoras):
                        print(f"{index} | {editora['nome']} | {editora['endereço']} | {editora['fone']}")
                        
            elif opcao_editoras == '2':
                nome_editora = input('Digite o nome da editora: ')
                endereco_editora = input('Digite o endereço da editora: ')
                fone_editora = input('Digite o telefone da editora: ')
                nova_editora = {
                    'nome': nome_editora,
                    'endereco': endereco_editora,
                    'fone': fone_editora
                }
                tabela_editoras.append(nova_editora)
                print('Editora adicionada com sucesso!')
            elif opcao_editoras == '3':
                id = int(input('Digite o ID da editora a ser excluída: '))
                tabela_editoras.pop(id)
                print('Editora exluída com sucesso.')
            elif opcao_editoras == '4':
                id = int(input('Digite o ID da editora para buscar: '))
                editora = tabela_editoras[id]
                print('ID | Nome | Endereço | Telefone')
                print(f"{ID} | {editora['nome']} | {editora['endereço']} | {editora['fone']}")

    if opcao_principal == '3':
        while True:
            print(menu_autores)
            opcao_autores = input('Digite a opção: ')
            if opcao_autores == '0':
                break  # interrompe o loop do while autores
            if opcao_autores == '1':
                if tabela_autores == []:
                    print("Nenhum Autor cadastrado.")
                    input("Pressione qualquer tecla para continuar...")
                    continue
                print(f'{'ID'.ljust(5)} | {'Nome'.ljust(5)} | {'Email'.ljust(5)} | {'Telefone'.ljust(5)} | {'Biografia'}')
                for index, autor in enumerate(tabela_autores):
                    print(f'{index} | {autor['nome']} | {autor['email']} | {autor['fone']} | {autor['biografia']}')
                    
            if opcao_autores == '2':
                nome_autor = input('Digite o nome do autor: ')
                email_autor = input('Digite o email do autor: ')
                fone_autor = input('Digite o telefone do autor: ')
                bio_autor = input('Digite a biografia do autor: ')
                novo_autor = {
                    'nome': nome_autor,
                    'email': email_autor,
                    'fone': fone_autor,
                    'biografia': bio_autor
                }
                tabela_autores.append(novo_autor)
                print('Autor adicionado com sucesso!')
                
            if opcao_autores == '3':
                if tabela_autoras == []:
                    print('Nenhum Autor cadastrado')
                else:
                    id = int(input('Digite o ID do autor a ser excluido: '))
                    tabela_autores.pop(id)
                    print('Autor excluído com sucesso!')
                
            if opcao_autores == '4':
                if tabela_autores == []:
                    print('Nenhum autor cadastrado.')
                else:
                    id = int(input('Digite o ID do autor para buscar: '))
                    autor = tabela_autores[id]
                    print('Id | Nome | Email | Telefone | Biografia')
                    print(f'{id} | {autor['nome']} | {autor['email']} | {autor['fone']} | {autor['biografia']}')
                    
    if opcao_principal == '0':
        break  # interrompe o loop do while principal

print('Programa Encerrado!')
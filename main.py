menu_principal = """[Menu Principal] Escolha uma das seguintes opções:
1 - Categorias
2 - Editoras
3 - Autores
4 - Livros
0 - Sair do programa
"""

menu_categorias = """
[Categorias] Escolha uma das seguintes opções:
1 - Listar todas as categorias
2 - Adicionar nova categoria
3 - Excluir categoria
4 - Ver categoria por Id
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

menu_autores = """
[Autores] Escolha uma das seguintes opções:
1 - Listar todos os autores
2 - Adicionar novo autor
3 - Excluir autor
4 - Ver autor por Id
0 - Voltar ao menu anterior
"""

menu_livros = """
[Livros] Escolha uma das seguintes opções:
1 - Listar todos os livros
2 - Adicionar novo livro
3 - Excluir livro
4 - Ver livro por Id
0 - Voltar ao menu anterior
"""

tabela_autores = []
tabela_editoras = []
tabela_categorias = []
tabela_livros = []

while True:
    print(menu_principal)

    print()  # Uma linha vazia.

    opcao_principal = input('Digite a opção: ')
    match opcao_principal:
        case '0':
            break  # interrompe o loop do while principal
     
        case '1':
            while True:
                print(menu_categorias)
                opcao_categorias = input('Digite a opção: ')
                match opcao_categorias:
                    case '0':
                        break
                    
                    case '1':
                        if tabela_categorias == []:
                            print('Nenhuma categoria cadastrada.')
                            input('Pressione ENTER para continuar...')
                            continue
                        print('ID | Nome')
                        for index, categoria in enumerate(tabela_categorias):
                            print(f"{index} | {categoria['nome']}")
                            
                    case '2':
                        nome_categoria = input('Digite o nome da categoria: ')
                        nova_categoria = {
                            'nome': nome_categoria
                        }
                        tabela_categorias.append(nova_categoria)
                        print('Categoria adicionada com sucesso.')
                        
                    case '3':
                        if tabela_categorias == []:
                            print('Nenhuma categoria cadastrada.')
                            input('Pressione ENTER para continuar')
                            continue
                        
                        id_categoria = int(input('Digite o ID da categoria que deseja excluir: '))
                        tabela_categorias.pop(id_categoria)
                        print('Categoria excluída com sucesso.')
                        
                    case '4':
                        id_categoria = int(input('Digite o ID da categoria que deseja visualizar: '))
                        categoria = tabela_categorias[id_categoria]
                        print(f"{id_categoria} | {categoria['nome']}")
                                        
        case '2':
            while True:
                print(menu_editoras)
                opcao_editoras = input('Digite a opção: ')
                match opcao_editoras:
                    case '0':
                        break
                    case '1':
                        if tabela_editoras == []:
                            print('Nenhuma editora cadastrada.')
                            input('Pressione ENTER para continuar...')
                            continue
                    
                        print('ID | Nome | Endereço | Telefone')
                        for index, editora in enumerate(tabela_editoras):
                            print(f"{index} | {editora['nome']} | {editora['endereco']} | {editora['fone']}")
                                
                    case '2':
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
                        
                    case '3':
                        if tabela_editoras == []:
                            print('Nenhuma editora cadastrada')
                            input('Pressione ENTER para continuar.')
                            continue
                        
                        id = int(input('Digite o ID da editora a ser excluída: '))
                        tabela_editoras.pop(id)
                        print('Editora exluída com sucesso.')
                        
                    case '4':
                        id = int(input('Digite o ID da editora para buscar: '))
                        editora = tabela_editoras[id]
                        print('ID | Nome | Endereço | Telefone')
                        print(f"{id} | {editora['nome']} | {editora['endereco']} | {editora['fone']}")
                        
                    case _:
                        print('Opção inválida. Tente novamente.')

        case '3':
            while True:
                print(menu_autores)
                opcao_autores = input('Digite a opção: ')
                match opcao_autores:
                    case '0':
                        break  # interrompe o loop do while autores
                    
                    case '1':
                        if tabela_autores == []:
                            print("Nenhum Autor cadastrado.")
                            input("Pressione ENTER para continuar...")
                            continue
                        print(f'{'ID'.ljust(5)} | {'Nome'.ljust(5)} | {'Email'.ljust(5)} | {'Telefone'.ljust(5)} | {'Biografia'}')
                        for index, autor in enumerate(tabela_autores):
                            print(f"{index} | {autor['nome']} | {autor['email']} | {autor['fone']} | {autor['biografia']}")
                            
                    case '2':
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
                        
                    case '3':
                        if tabela_autores == []:
                            print('Nenhum Autor cadastrado')
                            input('Pressione ENTER para continuar')
                            continue
                        
                        id = int(input('Digite o ID do autor a ser excluido: '))
                        tabela_autores.pop(id)
                        print('Autor excluído com sucesso!')
                    
                    case '4':
                        if tabela_autores == []:
                            print('Nenhum autor cadastrado.')
                            input('Pressione ENTER para continuar')
                            continue
                        
                        id = int(input('Digite o ID do autor para buscar: '))
                        autor = tabela_autores[id]
                        print('Id | Nome | Email | Telefone | Biografia')
                        print(f"{id} | {autor['nome']} | {autor['email']} | {autor['fone']} | {autor['biografia']}")
                            
                    case _:
                        print('Opção inválida. Tente novamente.')
        case '4':
            while True:
                print(menu_livros)
                opcao_livros = input('Digite a opção: ')
                match opcao_livros:
                    case '0':
                        break
                    
                    case '1':
                        if tabela_livros == []:
                            print('Nenhum livro cadastrado.')
                            input('Pressione ENTER para continuar')
                            continue
                        
                        print('ID | Título | Ano | Qtde Páginas | ISBN | Autor | Categoria | Editora')
                        for index, livro in enumerate(tabela_livros):
                            print(f"{index} | {livro['titulo']} | {livro['ano']} | {livro['paginas']} | {livro['isbn']} | {livro['autor']['nome']} | {livro['categoria']['nome']} | {livro['editora']['nome']}")
                    
                    case '2':
                        if tabela_autores == [] or tabela_categorias == [] or tabela_editoras == []:
                            print('Necessário cadastrar pelo menos um autor, uma categoria e uma editora')
                            continue
                        
                        titulo = input('Digite o título do livro: ')
                        resumo = input('Digite o resumo do livro: ')
                        ano = input('Digite o ano de publicação: ')
                        paginas = input('Digite a quantidade de páginas: ')
                        isbn = input('Digite o ISBN: ')
                        
                        print('ID | Nome | E-mail')
                        for index, autor in enumerate(tabela_autores):
                            print(f"{index} | {autor['nome']} | {autor['email']}")          
                        autor_id = int(input('Digite o ID do autor: '))
                        
                        print('ID | Nome')
                        for index, categoria in enumerate(tabela_categorias):
                            print(f"{index} | {categoria['nome']}")     
                        categoria_id = int(input('Digite o ID da categoria: '))
                        
                        print('ID | Nome')
                        for index, editora in enumerate(tabela_editoras):
                            print(f"{index} | {editora['nome']}")
                        editora_id = int(input('Digite o ID da editora: '))
                        
                        novo_livro = {
                            'titulo': titulo,
                            'resumo': resumo,
                            'ano': ano,
                            'paginas': paginas,
                            'isbn': isbn,
                            'autor': tabela_autores[autor_id],
                            'categoria': tabela_categorias[categoria_id],
                            'editora': tabela_editoras[editora_id]
                        }
                        
                        tabela_livros.append(novo_livro)
                        
                    case '3':
                        if tabela_livros == []:
                            print('Nenhum livro cadastrado.')
                            input('Pressione ENTER para continuar.')
                            continue
                       
                        id = int(input('Digite o ID do livro que deseja excluir: '))
                        tabela_livros.pop(id)
                        print('Livro excluído com sucesso!')
                    
                    case '4':
                        if tabela_livros == []:
                            print('Nenhum livro cadastrado')
                            input('Pressione ENTER para continuar')
                            continue
                        
                        id = int(input('Digite o ID do livro que deseja buscar: '))
                        livro = tabela_livros[id]
                        
                        print('ID | Título | Ano | Qtde páginas | ISBN | Autor | Categoria | Editora')
                        print(f"{index} | {livro['titulo']} | {livro['ano']} | {livro['paginas']} | {livro['isbn']} | {livro['autor']['nome']} | {livro['categoria']['nome']} | {livro['editora']['nome']}")
                        
                    case _:
                        print('Opção Inválida!')
    
        case _:
            print('OPÇÃO INVÁLIDA!\n')                   
        
print('Programa Encerrado!')
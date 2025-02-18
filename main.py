from service.autor_service import AutorService
import itertools


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



menu_livros = """
[Livros] Escolha uma das seguintes opções:
1 - Listar todos os livros
2 - Adicionar novo livro
3 - Excluir livro
4 - Ver livro por Id
0 - Voltar ao menu anterior
"""

autor_service = AutorService()
tabela_editoras = []
tabela_categorias = []
tabela_livros = []

def gerencia_categoria():
    print(menu_categorias)
    opcao_categorias = input('Digite a opção: ')
    match opcao_categorias:
        case '0':
            return #encerra a executação dentro da função
        case '1':
            if tabela_categorias == []:
                print('Nenhuma categoria cadastrada.')
                input('Pressione ENTER para continuar...')
            else:
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
            else:
                try:
                    id_categoria = input('Digite o ID da categoria que deseja excluir: ')
                    id_categoria = int(id_categoria)
                    tabela_categorias.pop(id_categoria)
                except:
                        print(f'ID da categoria  "{id}" inválido')  
                print('Categoria excluída com sucesso.') 
        case '4':
            if tabela_categoria == []:
                print('Nenhuma categoria cadastrada.')
                input('Pressione ENTER para continuar')
            else: 
                try:
                    id_categoria = input('Digite o ID da categoria que deseja visualizar: ')
                    id_categoria = int(id_categoria)
                    categoria = tabela_categorias[id_categoria]
                    print('ID | Nome')
                    print(f"{id_categoria} | {categoria['nome']}")
                except:
                    print(f'ID da categoria "{id_categoria}" inválido')
        case _:
            print('Opção inválida!')
                 
    gerencia_categoria()    

def gerencia_editora():
    print(menu_editoras)
    opcao_editoras = input('Digite a opção: ')
    match opcao_editoras:
        case '0':
            return
        case '1':
            if tabela_editoras == []:
                print('Nenhuma editora cadastrada.')
                input('Pressione ENTER para continuar...')
            else:
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
            else:  
                try:    
                    id_editora = input('Digite o ID da editora a ser excluída: ')
                    id_editora = int(id_editora)
                    tabela_editoras.pop(id_editora)
                    print('Editora exluída com sucesso.')
                except:
                    print(f'ID da editora "{id_editora}" inválido')
        case '4':
            if tabelas_editoras == []:
                print('Nenhuma editora cadastrada')
                input('Pressione ENTER para continuar')
            else:
                try:
                    id_editora = input('Digite o ID da editora para buscar: ')
                    id_editora = int(id_editora)
                    editora = tabela_editoras[id_editora]
                    print('ID | Nome | Endereço | Telefone')
                    print(f"{id} | {editora['nome']} | {editora['endereco']} | {editora['fone']}")
                except:
                    print(f'ID da editora "{id_editora}" inválido')
        case _:
            print('Opção inválida. Tente novamente.') 
            
    gerencia_editora()



def gerencia_livro():
    print(menu_livros)
    opcao_livros = input('Digite a opção: ')
    match opcao_livros:
        case '0':
            return
        case '1':
            if tabela_livros == []:
                print('Nenhum livro cadastrado.')
                input('Pressione ENTER para continuar')
            else:         
                print('ID | Título | Ano | Qtde Páginas | ISBN | Autor | Categoria | Editora')
                for index, livro in enumerate(tabela_livros):
                    print(f"{index} | {livro['titulo']} | {livro['ano']} | {livro['paginas']} | {livro['isbn']} | {livro['autor']['nome']} | {livro['categoria']['nome']} | {livro['editora']['nome']}")
        case '2':
            if AutorService.tabela_autores == [] or tabela_categorias == [] or tabela_editoras == []:
                print('Necessário cadastrar pelo menos um autor, uma categoria e uma editora')
            else:
                titulo = input('Digite o título do livro: ')
                resumo = input('Digite o resumo do livro: ')
                ano = input('Digite o ano de publicação: ')
                paginas = input('Digite a quantidade de páginas: ')
                isbn = input('Digite o ISBN: ')
                
                print('ID | Nome | E-mail')
                for index, autor in enumerate(AutorService.tabela_autores):
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
                    'autor': AutorService.tabela_autores[autor_id],
                    'categoria': tabela_categorias[categoria_id],
                    'editora': tabela_editoras[editora_id]
                }
                tabela_livros.append(novo_livro)
        case '3':
            if tabela_livros == []:
                print('Nenhum livro cadastrado.')
                input('Pressione ENTER para continuar.')
            else:
                try:
                    id_livro = input('Digite o ID do livro que deseja excluir: ')
                    id_livro = int(id_livro)
                    tabela_livros.pop(id_livro)
                    print('Livro excluído com sucesso!')
                except:
                    print('ID do livro "{id_livro}" inválido')
        case '4':
            if tabela_livros == []:
                print('Nenhum livro cadastrado')
                input('Pressione ENTER para continuar')
            else:
                try:
                    id_livro = input('Digite o ID do livro que deseja buscar: ')
                    id_livro = int(id_livro)
                    livro = tabela_livros[id_livro]
                    
                    print('ID | Título | Ano | Qtde páginas | ISBN | Autor | Categoria | Editora')
                    print(f"{index} | {livro['titulo']} | {livro['ano']} | {livro['paginas']} | {livro['isbn']} | {livro['autor']['nome']} | {livro['categoria']['nome']} | {livro['editora']['nome']}")
                except:
                    print('ID do livro "{id_livro}" inválido')  
        case _:
            print('Opção Inválida!')
    gerencia_livro()

def display_menu_principal():
    while True:
        print(menu_principal)
        print()  # Uma linha vazia.

        opcao_principal = input('Digite a opção: ')
        match opcao_principal:
            case '0':
                return #encerra a executação dentro da função  #break: interrompe o loop do while principal
            case '1':
                gerencia_categoria()                      
            case '2':
                gerencia_editora()
            case '3':
                autor_service.menu()
            case '4':
                gerencia_livro()
            case _:
                print('OPÇÃO INVÁLIDA!\n')                   
        
print('Programa Encerrado!')

display_menu_principal()
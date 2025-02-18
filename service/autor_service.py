from dao.autor_dao import AutorDAO
from model.autor import Autor

menu_autores = """
[Autores] Escolha uma das seguintes opções:
1 - Listar todos os autores
2 - Adicionar novo autor
3 - Excluir autor
4 - Ver autor por Id
5 - Editar autor
0 - Voltar ao menu anterior
"""


class AutorService:
    autor_dao = AutorDAO()
    
    def menu(self):
        print(menu_autores)
        opcao_autores = input('Digite a opção: ')
        match opcao_autores:
            case '0':
                return
            case '1':
                self.listar()
            case '2':
                self.adicionar()
            case '3':
                self.remover()
            case '4':
                self.mostrar_por_id()
            case '5':
                self.editar()
            case _:
                print('Opção inválida! Por favor, tente novamente.')
        
        self.menu()
    
    def listar(self):
        try:
            autores = AutorService.autor_dao.listar()
            if len(autores) == 0:
                print("Nenhum Autor cadastrado.")
                input("Pressione ENTER para continuar...")
            else:
                print(f'{'ID'.ljust(5)} | {'Nome'.ljust(5)} | {'Email'.ljust(5)} | {'Telefone'.ljust(5)} | {'Biografia'}')
                for index, autor in enumerate(autores):
                    print(autor)   
        except Exception as ex:
            print(f'Erro ao exibir os autores: {ex}')
    
    def adicionar(self):
        nome_autor = input('Digite o nome do autor: ')
        # while not valida_email(email_autor):
        #     print('E-mail inválido! Tente novamente.')
        #     email_autor = input('Digite o e-mail do autor: ')
            
        fone_autor = input('Digite o telefone do autor: ')
        bio_autor = input('Digite a biografia do autor: ')
        novo_autor = Autor(nome_autor, fone_autor, bio_autor)
        while True:
            try:
                email_autor = input('Digite o e-mail do autor: ')
                novo_autor.email = email_autor
            except Exception as e:
                print(e)
            else: 
                break
        
        try:
            AutorService.autor_dao.adicionar(novo_autor)   
        except Exception as ex:
            print(f'Erro ao tentar inserir novo autor: {ex}')
        else:
            print('Autor adicionado com sucesso!')
    
    def remover(self):
        if AutorService.autor_dao.empty():
            print('Nenhum Autor cadastrado')
            input('Pressione ENTER para continuar')
        else:
            try:
                id_autor = int(input('Digite o ID do autor a ser excluido: '))
                if AutorService.autor_dao.remover(id_autor):
                    print('Autor excluído com sucesso!')
                else:
                    print(f'ID "{id_autor}" do autor  inválido!')
            except:
                print(f'Erro ao tentar excluir autor: {ex}')

    def mostrar_por_id(self):
        if AutorService.autor_dao.empty():
            print('Nenhum autor cadastrado.')
            input('Pressione ENTER para continuar')
        else:
            try:
                id_autor = int(input('Digite o ID do autor para buscar: '))
                autor = AutorService.autor_dao.buscar_por_id(id_autor)
                if autor:
                    print('Id | Nome | Email | Telefone | Biografia')
                    print(autor)               
            except:
                print(f'ID do autor "{id_autor}" inválido')   
                
    def editar(self):
        if AutorService.autor_dao.empty():
            print('Nenhum Autor cadastrado.')
            input('Pressione ENTER para continuar')
        else:
            id_autor = int(input('Digite o ID do autor que deseja editar: '))
            autor = AutorService.autor_dao.editar(id_autor)
            if autor:
                novo_nome = input(f"Digite o novo nome do autor: ({autor.nome})")
                if novo_nome: 
                    autor.nome = novo_nome
                novo_fone = input(f"Digite o novo telefone do autor: ({autor.fone})")
                if novo_fone:
                    autor.fone = novo_fone
                nova_bio = input(f"Digite a nova biografia do autor: ({autor.biografia})")
                if nova_bio:
                    autor.biografia = nova_bio
            
                while True:
                    try:
                        novo_email = input(f"Digite o novo e-mail do autor: ({autor.email})")
                        if novo_email:
                            autor.email = novo_email
                    except Exception as e:
                        print(e)
                    else:
                        break
                print('Autor editado com sucesso!')
            else:
                print(f'ID "{id_autor}" do autor inválido! ')
            
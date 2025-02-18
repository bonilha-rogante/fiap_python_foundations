from model.autor import Autor

class AutorDAO:
    tabela_autores = []
    
    def empty(self) -> bool:
        return len(AutorDAO.tabela_autores) == 0
    
    def listar(self) -> list[Autor]:
        #Nesse método, conecto ao banco de dados e busco todos os registros de Autores
        return AutorDAO.tabela_autores
    
    def adicionar(self, novo_autor:Autor):
        AutorDAO.tabela_autores.append(novo_autor)
        
    def remover(self, id_autor: int) -> bool:
        encontrado = False
        for index, autor in enumerate(AutorDAO.tabela_autores):
            if autor.id == id_autor:
                encontrado = True
                break
        
        if encontrado:
            AutorDAO.tabela_autores.pop(index)
            
        return encontrado
    
    def buscar_por_id(self, id_autor: int):
        for autor in AutorDAO.tabela_autores:
            if autor.id == id_autor:
                return autor
        
    
    def editar(self, id_autor: int):
        for autor in AutorDAO.tabela_autores:
            if autor.id == id_autor:
                return autor
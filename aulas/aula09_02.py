from aula09_01 import Aluno

class Aluno:
    def __init__(self, nome):
        self.nome = nome
        
    def __str__(self):
        return f'Nome: {self.nome}'
    
    def __repr__(self):
        return f'{self.__class__.name__}("{self.nome}")'
    
    
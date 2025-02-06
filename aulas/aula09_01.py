class Aluno:
    def __init__(self, nome):
        self.nome = nome
        
    def __str__(self): #
        return f'Nome: {self.nome}'
    
    def __repr__(self): # Exibido em Debugger e arquivos de log | 
        return f'{self.__class__.__name__}("{self.nome}")"'
        
d = {
    'nome': 'João'
}

print(d)


a = Aluno('Well')
print(a)


class Aluno:
    def __init__(self, nome):
        self.nome = nome
        
    def __str__(self): #fromato que vc deseja que o usário visualize seu objeto
        return f'Nome: {self.nome}'
    
    def __repr__(self): # Exibido em Debugger e arquivos de log | Formato que você deseja visualizar o objeto
        return f'{self }("{self.nome}")"'

print(f'__name__ do módulo {__name__}')

if __name__ == '__main__':      
    d = {
        
        'nome': 'João'
    }

    print(d)
    a = Aluno('Well')
    print(a)




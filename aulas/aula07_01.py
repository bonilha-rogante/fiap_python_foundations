class Autor:
    def __init__(self ):
        self.nome = None
        self.email = None
        self.fone = None
        self.biografia = None
        
    def get_email(self): #getter
        return self.email
    
    def set_email(self, email): #setter
        self.email = email    
    
        
print('Início do programa.')
autor = Autor()

# autor.nome = 'Machado'
autor.set_email('machado@.com')
print(autor.get_email())
# print(autor.nome)
# print(autor.email)
# print(autor)
print('Fim do programa')

outro_autor = Autor()
outro_autor.nome = 'Cecília'
outro_autor.email = "teste@.com"
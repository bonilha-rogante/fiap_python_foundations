def  valida_email(email: str) -> bool:
    email = email.lower()
    
    if email.find('@') >= 0 and email.endswith('.com'):
        return True
    return False


class Autor:
    def __init__(self ):
        self.nome = None
        self.email = None
        self.fone = None
        self.biografia = None
        
    def get_email(self): #getter
        return self.email
    
    def set_email(self, email): #setter
        if valida_email(email):
            self.email = email
            return
        raise Exception('E-mail inválido.')

        
print('Início do programa.')
autor = Autor()

# autor.nome = 'Machado'
autor.set_email('machado@.com')
print(autor.get_email())
# print(autor.nome)
# print(autor.email)
# print(autor)

outro_autor = Autor()
outro_autor.nome = 'Cecília'
try:
    outro_autor.set_email("teste")
except Exception as e:
   print(e) 


print(outro_autor.get_email())
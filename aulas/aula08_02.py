def  valida_email(email: str) -> bool:
    email = email.lower()
    
    if email.find('@') >= 0 and email.endswith('.com'):
        return True
    return False

class Autor:
    __slots__ = ['__nome', '__email', '__fone', '__biografia']
    def __init__(self, nome: str, fone: str=None, biografia: str=None):
        self.nome = nome
        self.__email = None
        self.fone = fone
        self.biografia = biografia
        
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome.title()
        
    @property
    def email(self): #getter
        return self.__email
    
    @email.setter
    def email(self, email: str): #setter
        if valida_email(email):
            self.__email = email.lower()
            return
        raise Exception('E-mail inválido.')
    
    @property
    def fone(self):
        return self.__fone
    
    @fone.setter
    def fone(self, fone):
        self.__fone = fone
        
    @property
    def biografia(self):
        return self.__biografia

    @biografia.setter
    def biografia(self, biografia):
        self.__biografia = biografia    
    
    
print('Início do programa.')

autor = Autor('machado de assis', '11', 'bio')

try:
    autor.email = 'x@teste.com'
except Exception as e:
    print(e)
    
print(autor)
print(autor.nome)
print(autor.email)
print(autor.biografia)



outro_autor = Autor('CECÍLIA MEIRELES')
try:
    outro_autor.email = 'teste@.comm'
except Exception as e:
   print(e) 
   
   

outro_autor.fone = '222'
outro_autor.biografia = 'biook'

print(outro_autor.nome)
print(outro_autor.email)

print('Fim do programa')
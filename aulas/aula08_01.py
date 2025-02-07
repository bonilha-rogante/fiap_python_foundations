def  valida_email(email: str) -> bool:
    email = email.lower()
    
    if email.find('@') >= 0 and email.endswith('.com'):
        return True
    return False


class Autor:
    __slots__ = ['__nome', '__email', '__fone', '__biografia']
    def __init__(self, nome: str, email: str=None, fone: str=None, biografia: str=None):
        self.__nome = nome.title()
        self.__email = None
        self.__fone = None
        self.__biografia = None
        
    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome
        
    def get_email(self): #getter
        return self.__email
    
    def set_email(self, email): #setter
        if valida_email(email):
            self.__email = email
            return
        raise Exception('E-mail inválido.')
    
    def get_fone(self):
        return self.__fone
    
    def set_fone(self, fone):
        self.__fone = fone
        
    def get_biografia(self):
        return self.__biografia

    def set_biografia(self, biografia):
        self.__biografia = biografia    
    
    
print('Início do programa.')
autor = Autor('machado de assis', 'machado@.com', '11', 'bio')

print(autor.get_nome())
# autor.set_email('machado@.com')
# print(autor.get_email())

outro_autor = Autor('CECÍLIA MEIRELES')
try:
    outro_autor.set_email("teste@.comm")
except Exception as e:
   print(e) 
   
   outro_autor.set_fone('222')
   outro_autor.set_biografia('biook')


# print(outro_autor.get_email())
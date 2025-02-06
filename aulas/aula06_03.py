# def soma(lista_f):
#     resp = 0
#     for valor in lista_f:
#         resp += valor
        
#     return resp

# lista = [10, 20 ,30, 40]
# resultado = soma(lista)
# print(f'O resultado da soma é {resultado}')

def soma(*args):
    resp = 0
    for elemento in args:
        resp += elemento
    return resp

resultado = soma(10, 20, 30, 40, 50)
print(f'O resultado da soma é {resutlado}')
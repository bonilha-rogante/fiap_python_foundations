#Escreva uma função que aceite uma string como parâmetro e retornoe o seu inverso (de trás para frente)

mensagem = 'abcdefg'
# resultado = []

# tamanho = len(mensagem)

# for index in range(tamanho, 0, -1):
#     letra = mensagem[index -1]
#     print(letra)
#     resultado.append(letra)
#     tamanho -1
  
# print(resultado)
# print(''.join(resultado))

print(mensagem[::-1])

def inverter(palavra: str) -> str:
    return palavra[::-1]

print(inverter('Guilherme'))
# 2) Calcular e exibir a média aritmética de quatro valores quaisquer que serão digitados.
# Resolvam usando duas abordagens
# 2.1) sem 'for'
# 2.2) com 'for' ou 'while'

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))

# # sem for
soma = n1 + n2 + n3 + n4
media = soma / 4
print(f'A média é {media:.2f}')

# com for
soma = 0
for i in range(1, 5):
    nota = float(input(f'Digite a {i}ª nota:'))
    soma += nota
    print(soma)
    media = soma / 4
print(f'A média é {media:.2f}')


# Fazer um programa para receber um número e 
# validar se esse número é positivo. Após isso, exibir a tabuada de 1 a 10 desse número.

numero = int(input('Digite um número: '))

i = 1

while i < 11:
    resultado = numero * i
    print(f'{numero} X {i} = {resultado}')
    i += 1

# if numero > 0:
#     print(f'{numero} X 1 = {numero}')
#     print(f'{numero} X 2 = {numero * 2}')
# else:
#     print('O número é negativo e não é possível fazer a tabuada')

# FOR:
# if numero > 0:
#     for i in range(1, 11):
#         print(f'{numero} X {i} = {numero * i}')
# else:
#     print('O número é negativo e não é possível fazer a tabuada')

# WHILE:



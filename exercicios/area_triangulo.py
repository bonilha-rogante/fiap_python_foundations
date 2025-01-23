#1) Entrar via teclado com a base e a altura de um retângulo, calcular e exibir sua área.
# Fórmula: base * altura

base = float(input('Digite a base do triângulo:'))
altura = float(input('Digite a altura do triângulo: '))

area_triangulo = base * altura / 2

print(f'A área do triângulo é {area_triangulo:.2f}')
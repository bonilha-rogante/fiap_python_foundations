# Entrar com o peso e a altura de uma determinada pessoa. Após a digitação, exibir 
# se esta pessoa está ou não com seu peso ideal. Fórmula: peso/altura²

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / pow(altura, 2)

if imc < 20:
    print(f'Seu imc é {imc:.2f} e você está abaixo do peso')
elif imc < 25:
    print(f'Seu imc é {imc:.2f} e você está no peso ideal')
else:
    print(f'Seu imc é {imc:.2f} e você está acima do peso')
#Escreva uma função para identificar palindromos 

def is_palindromo(msg: str) -> bool:
    s = list(msg)
    lista = []
    for letra in s:
        if letra.isalnum():
            lista.append(letra.lower())
            
    temp = ''.join(lista)
    inverso = temp[::-1]
    return msg == inverso

s1 = 'Anotaram a data da maratona'
s2 = 'ana'
s3 = 'Ana'

print(f'{s2} é palíndromo? {is_palindromo(s2)}')
print(f'{s3} é palíndromo? {is_palindromo(s3)}')
    
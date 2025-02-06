def func(*args, **kwargs):
    for elemento in args:
        print(elemento)
    print('-'*40)
    for chave, valor in kwargs.items():
        print(f'{chave} = {valor}')
        

func(10)
func(10, True)
func(10, True, 12.345)

func(10, True, 12.345, nome='Well', sobrenome='Pereira', idade=20)
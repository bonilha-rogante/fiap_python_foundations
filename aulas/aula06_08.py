#Tipagem ou anotação de tipo

def funcao(a: int, b: int) -> int: 
    """_summary_

    Args:
        a (int): _description_
        b (int): _description_

    Returns:
        int: _description_
    """
    return a + b

print(f'Resultado: {funcao(2, 23)}')
print(f'Resultado: {funcao('Well', ' Pereira')}')
print('Fim do programa')
tabela_categorias = [
    {
       'nome': 'Romance'
    },
    {
       'nome': 'Terror' 
    },
    {
        'nome': 'Fantasia'
    }
]

for index, categoria in enumerate(tabela_categorias):
    print(index, categoria)
tamanho = len(tabela_categorias)



try:
    categoria_id = input('Digite o ID da categoria: ')
    categoria_id = int(categoria_id)
    print('Após int(categoria_id)')
    print(tabela_categorias[categoria_id])
    print('Após a tabela_categorias[categoria_id]')
except IndexError:
    print(f'ID {categoria_id} não encontrado na tabela.')
except ValueError:
    print(f'ID deve ser somente número inteiro. "{categoria_id}" não é um ID válido')
except Exception as e:
    print(f'Ocorreu um erro: {e}')
else: #then
    print('Não ocorreu nenhum erro/exceção')
finally:
    print('Será executado de qualquer forma.')
# if categorai_id >= 0 and categoria_id < tamanho:
#     print(tabela_categorias[categoria_id])
# else:print('ID não encontrado na tabela.')
    

print(tabela_categorias[3])
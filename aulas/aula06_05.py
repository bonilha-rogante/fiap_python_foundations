def soma(**kwargs):
    resp = 0
    for chave, valor in kwargs.items():
        resp += valor
    return resp

yy = 10
zz = 20
result = soma(y=yy, z=zz, t=0.5, v=1.3)
print(result)
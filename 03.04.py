lista = [1,2,3,4,5]

palavras = ['banana', 'morango', 'limão']

def ql(entrada):
    return sum(entrada), sum(entrada) / len(entrada)

def q2(lista, procurada, nova):
    for indice in range(len(lista)):
        if lista[indice] == procurada:
            lista[indice] = nova
            return lista

def q3(x):
    for i in range(x):
        print('*')
def q3(x):
    for i in range(x):
        print('*' * (i + 1))

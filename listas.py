"""
TUPLA
"""
tupla = ()  # PARENTESES NÃO OBRIGATÓRIO // SÃO IMUTÁVEIS
del (tupla)

"""
LISTA
"""
lista = [1, 2, 3, 5, 6]
lista.append(7)
lista.insert(0, 0)

del lista[2]  # Elimina e reposiciona índices
lista.pop(3)  # pop()
lista.remove('3')
lista.clear()  # Limpa e mas deixa índices

k = list()

a = [1, 2, 3, 4, 5]
b = a  # Cria ligação entre listas
b = a[:]  # Recebe todos valores de a

c.count('k')
c.index('k')

"""
DICT
"""
d = dict()
di = {'índice': 'Valor', 'índice2': 'Valor'}
di['novo'] = 'Valor'
del di['novo']

print(di.values())
print(di.keys())
print(di.items())

dicio = di.copy()  # Não dá pra usar [:]

for k,v in di.items():
    print(f'{k} contém {v}')
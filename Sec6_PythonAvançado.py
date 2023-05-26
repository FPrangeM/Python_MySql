
# List Comprehension
# Maneira de simplificar for loops e criar listas em uma unica linha

x = [1, 2, 3, 4, 5]
y = [i**2 for i in x]
z = [i for i in x if i % 2 == 1]

print(x)
print(y)
print(z)


# Função filter
# Interpreta uma função para cada valor de uma lista e retorna os itens com resposta da fução

def epar(i):
    if i % 2 == 0:
        return True


lista = list(range(10))

lista_par = list(filter(epar, lista))
print(lista_par)


# Função Map
# Aplica uma função a cada valor de uma lista

def sub_2(x):
    return x-2


lista = list(range(1, 20, 3))
print(lista)
print(list(map(sub_2, lista)))

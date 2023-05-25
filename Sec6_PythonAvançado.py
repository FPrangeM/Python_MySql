
# Lidando com List Comprehension

x = [1, 2, 3, 4, 5]
y = [i**2 for i in x]
z = [i for i in x if i % 2 == 1]

print(x)
print(y)
print(z)


# Trabalhando com a função filter

def epar(i):
    if i % 2 == 0:
        return i


lista = list(range(10))

lista_par = list(filter(epar, lista))
print(lista_par)

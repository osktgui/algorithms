lista = [5, 2, 4, 6, 1, 3]
print(lista)
for j in range(1,len(lista)):
    key = lista[j]
    i = j-1
    while i >= 0 and lista[i] > key:
        lista[i+1]=lista[i]
        i= i-1
    lista[i+1] = key
print(lista)

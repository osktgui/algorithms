import random

numbers = [];
length = 100;

for i in range(length):
    numbers.append(random.randint(1, 100))

search = input("Ingrese el número que desea encontrar: ")
search = int(search)
index = -1

for i in range(length):
    if( numbers[i] == search ):
        index = i
        break

print ("Lista: ", numbers)
if(index >= 0):
    print ("Encontrado en el indice:", index)
else:
    print ("Número no encontrado")

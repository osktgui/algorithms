a = [1, 0, 0]
b = [1, 1, 1]
c = []

print ("valor a:", a)
print ("valor b:", b)
a.reverse()
b.reverse()

suma = 0;
resto = 0;
division = 0;
base = 2;

for i in range(len(a)):
    suma = a[i] + b[i] + division
    division = suma // base
    resto = suma % base
    c.append(resto)
    if(i == len(a) - 1):
        c.append(division)

c.reverse()
print("la suma es: ", c);

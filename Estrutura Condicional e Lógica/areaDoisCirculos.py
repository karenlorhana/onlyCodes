r1= float(input())
r2= float(input())
pi= 3.14
c1= pi*(r1)**2
c2= pi*(r2)**2

if (c1 > c2):
    print("Primeiro circulo")
elif(c1 < c2):
    print("Segundo circulo")
else:
    print("Iguais")
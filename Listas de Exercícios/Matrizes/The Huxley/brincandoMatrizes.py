'''
    developed by Karen Lorhana
'''

matriz = []
positivos = []
positivo = 0
media = 0
menor = 1000000
delta = 0

for i in range(3):
    lista = []
    for j in range(3):
        numero = int(input())
        lista.append(numero)
    matriz.append(lista)

#media positivos
for i in matriz:
    for j in i:
        if j>0:
            positivo+= j
            positivos.append(positivo)
            media = positivo / len(positivos)

#menor valor

for i in matriz:
    for j in i:
        if j<menor:
            menor = j

#valor delta: 1 se o menor valor for par e 0 se for ímpar

if menor %2 == 0:
    delta = 1
else:
    delta = 0

#soma diagonal secundaria

for i in range(3):
    matriz[i][i] = 0
    
soma = 0
for i in matriz:
    soma += sum(i)

print("%.2f %d %d %d"%(media,menor,delta,soma))

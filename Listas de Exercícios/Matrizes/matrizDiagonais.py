#apenas ódio.

matriz = []
aux = 1
n = int(input())

#preencher matriz
for lin in range (n):
    lista = []
    for col in range(n):
        lista.append(aux)
        aux += 1
    matriz.append(lista)

print("Matriz:")

#imprimir matriz
for i in range(n):
    for j in range(n):
        if j == 0:
             print(" ",matriz[i][j], end = '  ')
        else:
            if j == n-1:
                 print(matriz[i][j])
            else:
                print(matriz[i][j], end = '  ')
print()
print("Diagonal Principal:")

#diagonal principal:

for i in range(1,n):
    for j in range(0,i):
        matriz[i][j] = " "
for i in range(n): 
    for j in range(i+1,n): 
       matriz[i][j] = " "
for i in range(n):
    for j in range(n):
        if matriz[i][j] != " ":
            print(" ",matriz[i][j], end = '')
            break
        else:
             print(" ",matriz[i][j], end = '')
    print()
print()
print("Diagonal Secundaria:")

#diagonal secundaria

matriz = []
auxx = 1
for i in range(n):
    linha = []
    for j in range(n):
        linha.append(auxx)
        auxx += 1
    matriz.append(linha)  
matriz.reverse()
for i in range(1,n):
    for j in range(0,i):
        matriz[i][j] = " "
for i in range(n): 
    for j in range(i+1,n): 
       matriz[i][j] = " "
matriz.reverse()
for i in range(n):
    for j in range(n):
        if matriz[i][j] != " ":
            print(" ",matriz[i][j], end = '')
            break
        else:
            print(" ",matriz[i][j], end = '')
    print()
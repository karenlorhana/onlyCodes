'''
    developed by Karen Lorhana
'''

matriz = []
soma = [[],[],[],[]]
qtd = input().split()
lin = int(qtd[0])
col = int(qtd[1])
soma0 = 0
soma1 = 0
soma2 = 0
soma3 = 0

for i in range(lin):
    linha = input().split()
    linha = list(map(int,linha))
    matriz.append(linha)

print("---"*10)

for l in range(lin):
    for c in range(col):
        print(matriz[l][c], end=' ')
    print()

for m in matriz:    
    soma0 += m[0]
    soma1 += m[1]
    soma2 += m[2]
    soma3 += m[3]
soma[0] = soma0
soma[1] = soma1
soma[2] = soma2
soma[3] = soma3
print(soma)
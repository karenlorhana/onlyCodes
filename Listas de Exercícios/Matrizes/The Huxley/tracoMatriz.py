matriz = []
qtd = int(input())
soma = 0

for i in range(qtd):
    linha = input().split()
    linha = list(map(float,linha))
    matriz.append(linha)


for i in range(qtd):
    soma += matriz[i][i] 

print("tr(A) = ",end="")
for i in range(qtd):
    if i == qtd-1:
        print("(%.2f) = %.2f"%(matriz[i][i],soma))
    else:
        print("(%.2f) + "%matriz[i][i],end="")
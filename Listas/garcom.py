n = int(input())
qtdQuebrados = 0

for i in range(n):
    x = input().split(" ")
    
    if(int(x[0]) > int(x[1])):
        qtdQuebrados += int(x[1])

print(qtdQuebrados)
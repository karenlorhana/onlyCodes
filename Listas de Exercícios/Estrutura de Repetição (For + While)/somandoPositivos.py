n1 = int(input())
n2 = int(input())
soma = 0

if n1 < n2:
    for i in range(n1, n2+1):
        if i > 0:
            soma += i
else:
    for i in range(n1, n2-1, -1):
        if i > 0:
            soma += i
print(soma)
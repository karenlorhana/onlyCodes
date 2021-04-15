nome = input().upper()
cont = 1

while cont <= len(nome):
    for i in range(cont):
        print(nome[i], end = "")
    print()
    cont += 1
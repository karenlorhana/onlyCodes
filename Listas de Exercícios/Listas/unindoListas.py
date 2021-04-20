'''
    developed by Karen Lorhana
'''
l1 =[]
l2 =[]
qtdLista1 = int(input())
if qtdLista1  == 0:
    print("Erro - A lista deve ter pelo menos 1 elemento.")
else:
    
    for i in range(1, qtdLista1+1):
        lista1 = int(input())
        l1.append(lista1)

    qtdLista2 = int(input())
    if qtdLista2 == 0:
        print("Erro - A lista deve ter pelo menos 1 elemento.")
    else:
        for i in range(1, qtdLista2+1):
            lista2 = int(input())
            l2.append(lista2)
        if((len(l1) == 0 or len(l2) == 0)):
            print("Erro - A lista deve ter pelo menos 1 elemento.")
        else:
            listasUnidas = str(l1 + l2)
            listasUnidas = listasUnidas.replace(",","")
            listasUnidas = listasUnidas.strip("[")
            listasUnidas = listasUnidas.strip("]")
            print(listasUnidas)
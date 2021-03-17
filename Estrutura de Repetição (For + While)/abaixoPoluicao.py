''' 
    Developed by Karen Lorhana
'''
multa = []
cont = 0
while cont <= 0:
    qtdVeiculos = int(input())
    if qtdVeiculos == 999:
        break
        cont += 1
    else:
        if qtdVeiculos != 999:
            if qtdVeiculos > 2:
                veiculoExtra = qtdVeiculos - 2
                multa.append(veiculoExtra)
print("{:.2f}".format(sum(multa)*12.89))
print(len(multa))
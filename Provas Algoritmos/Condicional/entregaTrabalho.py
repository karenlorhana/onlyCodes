''' 
    Developed by Karen Lorhana
'''

dataEntrega = float(input()) 
dataFinal = float(input()) 
diferencaDias = dataFinal - dataEntrega

if (diferencaDias < 0):
    print("Eu odeio a professora!")
elif (diferencaDias > 0 and diferencaDias >= 3):
    print("Muito bem! No prazo!")
elif (diferencaDias > 0 and diferencaDias < 4):
    print("Parece o trabalho do meu filho!")
    if  dataEntrega + 2 < 24:
        print("Trabalho Apresentado!")
    else:
        print("Voce falhou! Ate a proxima!")
elif (diferencaDias == 0):
    print("Parece o trabalho do meu filho!")
    print("Voce falhou! Ate a proxima!")
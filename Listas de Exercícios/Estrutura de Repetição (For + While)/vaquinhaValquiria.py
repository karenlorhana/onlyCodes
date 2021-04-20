''' 
    Developed by Karen Lorhana
'''

soma = 0
media = 0
print("Insira os valores das doacoes:")

valorDoado = float(input())

if valorDoado < 0:
    print("Total arrecadado: 0.00")
    print("Valor medio da doacao: 0.00")
    
else: 
    while valorDoado > 0:
        soma += valorDoado
        media += 1
        valorDoado = float(input())

    print("Total arrecadado: %.2f"%soma )
    print("Valor medio da doacao: %.2f"%(soma/media))



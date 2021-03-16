''' 
    Developed by Karen Lorhana
'''

distancia = 0
cidades = " "
while True:
    nomeCidade = input().upper()
    if nomeCidade == "FIM":
        break
    distanciaCidade = int(input())
    valorPassagem = float(input())
    if (distanciaCidade > distancia) and (valorPassagem * 2 <= 300):
        cidades = nomeCidade
        distancia = distanciaCidade
if (cidades == " "):
    print("SEM DESTINO")
else:
    print(cidades)
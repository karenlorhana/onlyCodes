''' 
    Developed by Karen Lorhana
'''

qtdCandidatos = 0
porcentagemPort = (50*80)/100
porcentagemMat = (35*60)/100

while True:
    qtdPortgues = int(input()) 
    if qtdPortgues < 0:
        break
    else: 
        qtdMatematica = int(input()) 
        notaRedacao = float(input())
    if qtdPortgues >= porcentagemPort and qtdMatematica >= porcentagemMat and notaRedacao >= 7:
        qtdCandidatos += 1
print(qtdCandidatos)
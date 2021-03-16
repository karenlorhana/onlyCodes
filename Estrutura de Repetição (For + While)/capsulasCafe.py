''' 
    Developed by Karen Lorhana
'''

capsulas = 0

for i in range (7):
    doacaoCaixa = int(input())
    tamanhoCaixa = str(input()).upper()
    if tamanhoCaixa == "P":
        capsulas += 10*doacaoCaixa
    else: 
        capsulas += 16*doacaoCaixa
print(capsulas)
print((capsulas*2)/7)
''' 
    Developed by Karen Lorhana
'''

qtdInscritos = 0
qtdAprovados = 0
qtdHomemAprovados = 0
qtdMulherAprovadas = 0
media = 0


while True:
    notaProva = int(input())
    while notaProva > 100:
        print("Digite uma nota inferior a 100.")
        notaProva = int(input())
    if notaProva < 0:
        break
    else:
        notaRedaco = int(input())
        while notaRedaco > 100:
            print("Digite uma nota inferior a 100.")
            notaRedaco = int(input())
        sexoCandidato = str(input()).upper()
        
        media = (notaProva + notaRedaco)/2
        
        
        if notaProva > 40  and notaRedaco >40 and media >= 60 and sexoCandidato == "F":
            mediaCandidato = (notaProva + notaRedaco)/2 
            qtdMulherAprovadas += 1
        if notaProva >40 and notaRedaco >40 and media >= 60 and sexoCandidato == "M":
            qtdHomemAprovados += 1
        qtdAprovados = qtdMulherAprovadas + qtdHomemAprovados  
        qtdInscritos += 1
                
        
print(qtdInscritos,"candidato(s) inscrito(s).")
print(qtdAprovados,"candidato(s) aprovado(s).")
print(qtdMulherAprovadas, "mulher(es) e", qtdHomemAprovados, "homem(ns).")
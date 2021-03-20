''' 
    Developed by Karen Lorhana
'''

idade = int(input("Sua idade:\n" ))
profissao = int(input("Profissao(1-saude;2-indigenas;3-professores;4-seguranca;5-sistema prisional; 6-outro):\n"))
comorbidades = str(input("Tem comorbidades (s/n)?\n")).lower()
resInst = str(input("Mora em residencia institucionalizada(s/n)?\n")).lower()

print("--------------------------")

if (profissao == 1 or profissao == 2 or profissao == 3 or profissao == 4 or profissao == 5 or profissao == 6):
    if(profissao == 1):
        print("Voce eh do grupo 1 e serah vacinado na Fase 1")
    elif(idade >= 60 or resInst == "s"):
            print("Voce eh do grupo 2 e serah vacinado na Fase 1")
    elif(idade >=75 or idade == 79):
        print("Voce eh do grupo 2 e serah vacinado na Fase 1")
    elif(idade >= 75 or idade == 79):
        print("Voce eh do grupo 2 e serah vacinado na Fase 1")
    elif(idade >= 80):
        print("Voce eh do grupo 2 e serah vacinado na Fase 1")
    elif(profissao == 2):
        print("Voce eh do grupo 2 e serah vacinado na Fase 1")
    elif(idade >= 70 or idade == 74):
        print("Voce eh do grupo 3 e serah vacinado na Fase 2")
    elif(idade >= 65 or idade == 69):
        print("Voce eh do grupo 4 e serah vacinado na Fase 2")
    elif(idade >= 60 or idade == 64):
        print("Voce eh do grupo 5 e serah vacinado na Fase 2")
    elif(comorbidades == "s"):
        print("Voce eh do grupo 6 e serah vacinado na Fase 3")
    elif(profissao == 3):
        print("Voce eh do grupo 7 e serah vacinado na Fase 4")
    elif(profissao == 4):
        print("Voce eh do grupo 8 e serah vacinado na Fase 4")
    elif(profissao == 5):
        print("Voce eh do grupo 8 e serah vacinado na Fase 4")
else:
    print("Voce informou um codigo de profissao invalido")
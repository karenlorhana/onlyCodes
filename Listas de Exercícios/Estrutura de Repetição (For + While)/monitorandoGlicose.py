''' 
    Developed by Karen Lorhana
'''

cont = 0
totalGlicoses = 0
while True:
    glicoses = int(input())
    if glicoses == 0:
        break
    else:
        if glicoses != 0:
            cont += 1
            totalGlicoses += glicoses
            mediaGlicose = totalGlicoses / cont
if mediaGlicose < 110:
    print("Glicose Normal")
elif mediaGlicose >= 200:
    print("Glicose Muito Alta")
else:
    print("Glicose Alterada")
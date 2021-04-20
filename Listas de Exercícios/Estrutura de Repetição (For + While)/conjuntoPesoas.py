''' 
    Developed by Karen Lorhana
'''

qtdMulher = 0
qtdHomem = 0
qtdSalario = 0
salarios = 0
maiorSalMasculino = 0
maiorSalFeminino = 0
mediaSalHomem = 0
mediaSal = 0
salariosHomem = 0


for i in range(0, 4):
    sexo = str(input("sexo: ")).upper()
    salario = float(input("salario: "))
    salarios += salario
    qtdSalario += 1
    mediaSal = salarios / qtdSalario
    
    if sexo == "F":
        qtdMulher += 1
        if maiorSalFeminino < salario:
            maiorSalFeminino = salario  
    if sexo == "M":
        qtdHomem += 1
        salariosHomem += salario
        mediaSalHomem = salariosHomem / qtdHomem
        if maiorSalMasculino < salario:
            maiorSalMasculino = salario
        

print(qtdHomem)   
print(qtdMulher) 
print(mediaSal)
if maiorSalFeminino > maiorSalMasculino:
    print("F")
else:    
    print("M")
print(mediaSalHomem)
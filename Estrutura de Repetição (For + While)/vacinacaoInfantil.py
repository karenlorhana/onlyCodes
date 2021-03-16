''' 
    Developed by Karen Lorhana
'''

primeiraDose = int(input())
periodo = int(input())


for i in range (1):
    periodoVacina2 = primeiraDose+periodo
    periodoVacina3 = primeiraDose+2*periodo
    periodoVacina4 = primeiraDose+3*periodo

    periodoVacina = periodoVacina2, periodoVacina3, periodoVacina4
    print(periodoVacina)
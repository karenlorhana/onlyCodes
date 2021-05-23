'''
    developed by Karen Lorhana
'''

def quantidadeMacaquinhos(tipoAnimal):
    contMacaco = 0
    if tipoAnimal == "MACACO":
        contMacaco += 1
    return contMacaco

def pesoGatinhos(animais, tipoAnimal, pesoAnimal):
    pesoTigre = 0
    for animal in animais:
        if animal['tipo'].upper() == "TIGRE":
            pesoTigre += animal['peso']
    return pesoTigre
def nacionalidadeCobrinhas(animais, tipoAnimal, paisOrigemAnimal):
    contCobra = 0
    for animal in animais:
        if animal['tipo'].upper() == "COBRA" and animal['pais'].upper() == "VENEZUELA":
            contCobra += 1
    return contCobra


animais = []

while True:
    tipoAnimal = str(input("Tipo: ")).upper()
    pesoAnimal = float(input("Peso: "))
    paisOrigemAnimal = str(input("Pais: ")).upper()
    animais.append({
        'tipo': tipoAnimal,
        'peso': pesoAnimal,
        'pais': paisOrigemAnimal
    })
    inserirMais = str(input("Quer parar? ")).upper()
    if inserirMais == "PARAR":
        break

qtdMacaco = quantidadeMacaquinhos(tipoAnimal)
pesoTigre = pesoGatinhos(animais, tipoAnimal, pesoAnimal)
paisCobra = nacionalidadeCobrinhas(animais,tipoAnimal, paisOrigemAnimal)
print(qtdMacaco)
print(pesoTigre)
print(paisCobra)


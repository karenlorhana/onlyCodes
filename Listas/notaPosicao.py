notas = []
media = 0
qtdNotas = int(input())
if qtdNotas > 0:
    for i in range(1, qtdNotas+1):
        nota = float(input())
        notas.append(nota)
        media = sum(notas)/len(notas)
    for i in range (len(notas)):
        print('Nota %d:'%(i+1), notas[i])
    print("Media:", media)
        
        
else:
    print("Numero de notas invalido.")
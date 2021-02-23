qtdLivros = int(input())
qtdAlunos = int(input())
media = qtdAlunos/qtdLivros

if (media < 9):
    print("A")
elif (media < 13):
    print("B")
elif (media < 19):
    print("C")
else:
    print("D")
notas = []
qtd = int(input())
notasAcima = 0
notasAbaixo = 0

for i in range(qtd):
    nota = int(input())
    notas.append(nota)

media = sum(notas)/qtd
mediaMaior = media * 1.10
mediaMenor = media * 0.90

for nota in notas:
    if nota >= mediaMaior:
        notasAcima += 1
    elif nota <= mediaMenor:
        notasAbaixo += 1

print("%.2f"%media)
print(notasAcima)
print(notasAbaixo)
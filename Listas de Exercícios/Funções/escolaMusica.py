def ClassificaAluno (nota, falta):
    if nota >= 9.5 and falta <10:
        return "APROVADO COM LOUVOR"
    elif nota >= 7.0 and nota < 9.5 and falta <=10:
        return "APROVADO"
    elif nota <= 6.9 and falta <=10:
        return "REPROVADO"
    elif falta > 10:
        return "REPROVADO POR FALTA"
nota = float(input())
falta = int(input())
print(ClassificaAluno(nota, falta))
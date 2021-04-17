aux = ""
cobol = "COBOL"
cont = 0
true = 0
    
while True:
    palavra = str(input()).upper().split("-")
    if palavra[0] != "FIM":
        for word in range(len(palavra)):
            aux = palavra[word]

            if aux[0] == cobol[cont] or aux[len(aux)-1] == cobol[cont]:
                true += 1    
            cont+= 1

        if true == cont:
            print("GRACE HOPPER")
        else:
            print("BUG")

        cont = 0
        true = 0
    else:
        break
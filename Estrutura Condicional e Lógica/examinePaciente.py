temperatura = float (input ())
sintomas = input()
if (temperatura >= 37 and sintomas == "S"):
    print("Exames Especiais")
elif (temperatura >= 37 and sintomas == "N"):
    print("Exames Basicos")
elif (temperatura < 37 and sintomas == "S" ):
    print("Exames Basicos")
elif(temperatura < 37 and sintomas == "N"):
        print("Liberado")
else:
    print("Erro")
level = int(input())
if (level >= 1 and level <= 20):
    Potencia = 20 + (level ** 3)
    print(" Potencia de : %d W" % Potencia)

elif (level >= 21 and level <= 40):
    Potencia = 8000 + (level - 10) ** 2
    print(" Potencia de : %d W" % Potencia)

elif (level >= 41 and level <= 60):
    Potencia = 9000 + 5 * level
    print(" Potencia de : %d W" % Potencia)

elif (level >= 61 and level <= 80):
    Potencia = 9300 + 2 * level
    print(" Potencia de : %d W" % Potencia)

elif (level >= 81 and level <= 100):
    Potencia = 9500 + level
    print(" Potencia de : %d W" % Potencia)
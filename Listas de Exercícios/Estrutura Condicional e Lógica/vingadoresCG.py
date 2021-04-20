vingador = str(input())


if (vingador == "Homem de Ferro" or vingador == "Hulk" or vingador == "Capitão América" or vingador == "Thor" or vingador == "Gavião Arqueiro" or vingador == "Viúva Negra"):
    poder = str(input())
    energia = int(input())
    if (vingador == "Homem de Ferro"):
        if(poder == "Armadura de Ferro"):
            if(energia >10):
                print(vingador,"conseguiu derrotar Thanos")
            else:
                print(vingador, "NAO conseguiu derrotar Thanos, chamem outro Vingador")
        elif(poder == "Força Bruta"):
            print(vingador, "NAO conseguiu derrotar Thanos")
            print("Esse é o poder do Hulk")
        elif(poder == "Escudo"):
            print(vingador, "NAO conseguiu derrotar Thanos")
            print("Esse é o poder do Capitão América")
        elif(poder == "Martelo"):
            print(vingador, "NAO conseguiu derrotar Thanos")
            print("Esse é o poder do Thor")
        elif(poder == "Arco e Flecha"):
            print(vingador, "NAO conseguiu derrotar Thanosr")
            print("Esse é o poder do Gavião Arqueiro")
        elif(poder == "Inteligência"):
            print(vingador, "NAO conseguiu derrotar Thanos")
            print("Esse é o poder da Viúva Negra")

    elif(vingador == "Hulk"):
        if (poder == "Força Bruta"):
            if (energia > 5):
                print(vingador, "conseguiu derrotar Thanos")
            else:
                print(vingador, "NAO conseguiu derrotar Thanos, chamem outro Vingador")
        elif (poder == "Armadura de Ferro"):
            print(vingador, "NAO conseguiu derrotar Thanos")
            print("Esse é o poder do Homem de Ferro")
        elif (poder == "Escudo"):
            print(vingador, "NAO conseguiu derrotar Thanos")
            print("Esse é o poder do Capitão América")
        elif (poder == "Martelo"):
            print(vingador, "NAO conseguiu derrotar Thanos")
            print("Esse é o poder do Thor")
        elif (poder == "Arco e Flecha"):
            print(vingador, "NAO conseguiu derrotar Thanos")
            print("Esse é o poder do Gavião Arqueiro")
        elif (poder == "Inteligência"):
            print(vingador, "NAO conseguiu derrotar Thanos")
            print("Esse é o poder da Viúva Negra")

    elif(vingador == "Capitão América"):
        if (poder == "Escudo"):
            if (energia > 7):
                print(vingador, "conseguiu derrotar Thanos")
            else:
                print(vingador, "NAO conseguiu derrotar Thanos, chamem outro Vingador")
        elif (poder == "Força Bruta"):
            print(vingador, "NAO conseguiu derrotar Thanos")
            print("Esse é o poder do Hulk")
        elif (poder == "Armadura de Ferro"):
            print(vingador, "NAO conseguiu derrotar Thanos")
            print("Esse é o poder do Homem de Ferro")
        elif (poder == "Martelo"):
            print(vingador, "NAO conseguiu derrotar Thanos")
            print("Esse é o poder do Thor")
        elif (poder == "Arco e Flecha"):
            print(vingador, "NAO conseguiu derrotar Thanos")
            print("Esse é o poder do Gavião Arqueiro")
        elif (poder == "Inteligência"):
            print(vingador, "NAO conseguiu derrotar Thanos")
            print("Esse é o poder da Viúva Negra")

    elif(vingador == "Thor"):
        if (poder == "Martelo"):
            if (energia > 4):
                print(vingador, "conseguiu derrotar Thanos")
            else:
                print(vingador, "NAO conseguiu derrotar Thanos, chamem outro Vingador")
        elif (poder == "Força Bruta"):
            print(vingador, "NAO conseguiu derrotar Thanos")
            print("Esse é o poder do Hulk")
        elif (poder == "Escudo"):
            print(vingador, "NAO conseguiu derrotar Thanos")
            print("Esse é o poder do Capitão América")
        elif (poder == "Armadura de Ferro"):
            print(vingador, "NAO conseguiu derrotar Thanos")
            print("Esse é o poder do Homem de Ferro")
        elif (poder == "Arco e Flecha"):
            print(vingador, "NAO conseguiu derrotar Thanos")
            print("Esse é o poder do Gavião Arqueiro")
        elif (poder == "Inteligência"):
            print(vingador, "NAO conseguiu derrotar Thanos")
            print("Esse é o poder da Viúva Negra")

    elif(vingador == "Gavião Arqueiro"):
        if (poder == "Arco e Flecha"):
            if (energia > 12):
                print(vingador, "conseguiu derrotar Thanos")
            else:
                print(vingador, "NAO conseguiu derrotar Thanos, chamem outro Vingador")
        elif (poder == "Força Bruta"):
            print(vingador, "NAO conseguiu derrotar Thanos")
            print("Esse é o poder do Hulk")
        elif (poder == "Escudo"):
            print(vingador, "NAO conseguiu derrotar Thanos")
            print("Esse é o poder do Capitão América")
        elif (poder == "Martelo"):
            print(vingador, "NAO conseguiu derrotar Thanos")
            print("Esse é o poder do Thor")
        elif (poder == "Armadura de Ferro"):
            print(vingador, "NAO conseguiu derrotar Thanos")
            print("Esse é o poder do Homem de Ferro")
        elif (poder == "Inteligência"):
            print(vingador, "NAO conseguiu derrotar Thanos")
            print("Esse é o poder da Viúva Negra")

    elif(vingador == "Viúva Negra"):
        if (poder == "Inteligência"):
            if (energia > 20):
                print(vingador, "conseguiu derrotar Thanos")
            else:
                print(vingador, "NAO conseguiu derrotar Thanos, chamem outro Vingador")
        elif (poder == "Força Bruta"):
            print(vingador, "NAO conseguiu derrotar Thanosr")
            print("Esse é o poder do Hulk")
        elif (poder == "Escudo"):
            print(vingador, "NAO conseguiu derrotar Thanos")
            print("Esse é o poder do Capitão América")
        elif (poder == "Martelo"):
            print(vingador, "NAO conseguiu derrotar Thanos")
            print("Esse é o poder do Thor")
        elif (poder == "Arco e Flecha"):
            print(vingador, "NAO conseguiu derrotar Thanos")
            print("Esse é o poder do Gavião Arqueiro")
        elif (poder == "Armadura de Ferro"):
            print(vingador, "NAO conseguiu derrotar Thanos")
            print("Esse é o poder do Homem de Ferro")

else:
        print("Vingador Inválido")
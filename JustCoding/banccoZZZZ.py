import os

saldo = 0

while True:
    print()
    print("*** Banco ZZZZZ *** \n"
      "1 - Depositar \n"
      "2 - Sacar \n"
      "3 - Transferir \n"
      "4 - Saldo \n"
      "5 - Sair \n"
      )
    opcao = str(input("Digite a opção desejada: "))
    print()

    if opcao == "1":
        os.system('clear')
        print("Você está na opção de depósito!\n")
        deposito = float(input("Digite o valor do depósito: "))
        saldo += deposito

    elif opcao == "2":
        os.system('clear')
        print("Você está na opção de sacar!\n")
        valorSaque = float(input("Informe o valor você deseja sacar: "))
        if valorSaque > saldo:
            print("Você não tem saldo o suficiente!")
        else:
            saldo = saldo - valorSaque
            print("Valor sacado com sucesso!")

    elif opcao == "3":
        os.system('clear')
        print("Você está na opção de transferir!\n")
        contaDestino = int(input("Informe o número da conta destimo para transferência: "))
        valorTransferencia = float(input("Informe o valor para a trasnferência: "))
        if valorTransferencia > saldo:
            print("Você não tem saldo o suficiente!")
        else: 
            saldo = saldo - valorTransferencia
            print("Valor transferido com sucesso!")
            print()
            print("Você deseja realizar outra transferência? \n"
                    "1 - Sim\n"
                    "2 - Não\n")
            outraTransferencia = str(input())
            while outraTransferencia == "1":
                contaDestino = int(input("Informe o número da conta destimo para transferência: "))
                valorTransferencia = float(input("Informe o valor para a trasnferência: "))
                if valorTransferencia > saldo:
                    print("Você não tem saldo o suficiente!")
                else: 
                    saldo = saldo - valorTransferencia
                    print("Valor transferido com sucesso!")
                    print()
                    print("Você deseja realizar outra transferência? \n"
                        "1 - Sim\n"
                        "2 - Não\n")
                    outraTransferencia = str(input())

    elif opcao == "4":
        os.system('clear')
        print("Você está na opção de saldo!\n")
        print("Seu saldo atual: ",saldo)
    
    
    elif opcao == "5":
        #os.system('clear')
        print("Você sairá do banco agora!")
        break
  

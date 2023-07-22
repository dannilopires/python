saldo = 1000

saque = 0

lista_saque = list(())

lista_deposito = list(())

while True:
    opcao = int(input("\n [1]Sacar \n [2]Depósito \n [3]Extrato \n [0]Sair: \n Informe uma opção: "))

    if opcao == 1:
        valor = float(input("Informe valor que deseja retirar: "))
        saldo -= valor
        saque += 1

        if saque > 3:
            print ("Não é permitido fazer mais de 3 saques por dia")
            break

        lista_saque.append(valor)

        outra_opcao = input("\n Deseja fazer mais alguma operação? S ou N? ")
        if outra_opcao=="s":
            continue
        else:
            break


        break

    elif opcao == 2:
        valor = float(input("Informe o valor que deseja depositar: "))
        saldo += valor

        lista_deposito.append(valor)

        outra_opcao = input("\n Deseja fazer mais alguma operação? S ou N? ")
        if outra_opcao=="s":
            continue
        else:
            break

        break

    elif opcao == 3:

        print("\n##########################")
        print ("Seu saldo atual é: R$", format(saldo))
        print ("\n Saques:")

        for x in lista_saque:
            print(x)
        
        print("\n Depósitos:")
        for y in lista_deposito:
            print(y)

        print("\n##########################")
        
        outra_opcao = input("\n Deseja fazer mais alguma operação? S ou N? ")
        if outra_opcao=="s":
            continue
        else:
            break

        break

    else:
        break
    


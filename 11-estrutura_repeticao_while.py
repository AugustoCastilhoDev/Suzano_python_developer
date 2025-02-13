opcao = -1

while opcao != 0:
    opcao = int(input("[1] sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o Extrato")
    else:
        print("Obrigado por utilizar nosso.")


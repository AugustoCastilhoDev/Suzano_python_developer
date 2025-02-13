opcao = -1

while opcao != 0:
    opcao = int(input("Informe um número: "))

    if opcao == 10:
        break

    print(opcao)

print("__________________________")
print()


while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    if numero % 2 == 0:
        continue
    
    print(numero)
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

# Exemplo utilizando um iterável

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print() # adiciona uma quebra de linha
    print("Executa no final do laço")        

print("_____________________________________________")    

# Utilizando range com for

for numero in range(0, 11):
    print(numero, end=" ")
print()
print("_____________________________________________")

# Exemplo de tabuada, utilizando a função range.

for numero in range(0, 51, 5):
    print(numero, end=" ")
frutas = ["laranja", "maçã", "uva", "pera"]

print(frutas[0])
print(frutas[2])


# Linhas aninhadas
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])

# Fatiamento

lista = ["p","y","t","h","o","n"]
print(lista[2:])
print(lista[:2])
print(lista[1:3])
print(lista[0:3:2])
print(lista[::])
print(lista[::-1])

# Iterar listas

carros = ["Gol","Celta","Palio"]

for carro in carros:
    print(carro)
    
# Função enumerate

carros = ["Gol","Celta","Palio"]

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")


# Filtro versão 1

numeros = [1,30,11,21,2,9,65,34]
pares = []

for numero in numeros:
    if numero % 2 ==0:
        pares.append(numero)
print(pares)        


# Filtro versão 2

numeros = [1,30,11,21,2,9,65,34]
pares = [numero for numero in numeros if numero % 2 == 0]

print(pares)  


# Modificando Valores Versão 1

numeros = [1,22,30,34,12,18,6,9]
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)
print(quadrado)    


# Modificando Valores Versão 2

numeros = [1,22,30,34,12,18,6,9]
quadrado = [numero ** 2 for numero in numeros]

print(quadrado)

# [].append

lista = []

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista)


# [].clear

lista = [1, "Python", [40,30,20]]

print(lista)

lista.clear()

print(lista)

# [].copy

lista = [1, "Python", [40,30,20,]]

lista.copy()

print(lista)


# [].count

cores = ["Vermelho", "Azul", "Verde", "Azul"]

print(cores.count("Vermelho"))
print(cores.count("Azul"))
print(cores.count("Verde"))
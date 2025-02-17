# criando sets

numeros = set([1,2,3,1,3,4])

fruta = set("abacaxi")

carros = set(("palio", "gol", "celta", "palio",))

print(carros)
print(numeros)
print(fruta)

print("________________________________________")
# acessando dadoos

numeros = {1,2,3,2}
numeros = list(numeros)
print(numeros[0])

print("________________________________________")

# Iterar conjuntos
carros = {"gol", "Celta", "palio"}

for carro in carros:
    print(carro)

print("________________________________________")

# Função enumerate
carros = {"gol", "celta", "palio"}
for i, carro in enumerate(carros):
    print(f"{i}: {carro}")
    
print("________________________________________")

# Conjuntos
conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))

print("________________________________________")

# Métodos da classe set

# remove
numeros = {1,2,3,4,5,6,7,8,9,0}

print(numeros)
print(numeros.remove(0))
print(numeros.remove(2))
print(numeros)      

print("________________________________________")

# .union

conjunto_a = {1,2}
conjunto_b = {3,4}

print(conjunto_a.union(conjunto_b))

print("________________________________________")

# intersection

conjunto_a = {1,2,3}
conjunto_b = {2,3,4,5}

print(conjunto_a.intersection(conjunto_b))

print("________________________________________")

# .difference

conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))

print("________________________________________")

# .symmetric_difference

conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

print(conjunto_a.symmetric_difference(conjunto_b))

print("________________________________________")

# .issubset

conjunto_a = {1,2,3}
conjunto_b = {4,1,2,5,6,3}

print(conjunto_a.issubset(conjunto_b))
print(conjunto_b.issubset(conjunto_a))

print("________________________________________")

# .issuperset

conjunto_a = {1,2,3}
conjunto_b = {4,1,2,5,6,3}

print(conjunto_a.issuperset(conjunto_b))
print(conjunto_b.issuperset(conjunto_a))

print("________________________________________")

# .isdisjoint

conjunto_a = {1,2,3,4,5}
conjunto_b = {6,7,8,9}
conjunto_c = {1,0}

conjunto_a.isdisjoint(conjunto_b)
conjunto_a.isdisjoint(conjunto_c)

print("________________________________________")

# .add

sorteio = {1,23,10}

print(sorteio.add(25))
print(sorteio.add(42))
print(sorteio.add(25))
print(sorteio)

print("________________________________________")

# .clear

sorteio = {1,23}

print(sorteio)
print(sorteio.clear())
print(sorteio)

print("________________________________________")

# .copy

sorteio = {1,2,3}
print(sorteio)
print(sorteio.copy)
print(sorteio)

print("________________________________________")

# .discard

numeros = {1,2,3,4,5,6,5,7,8,9,0}

print(numeros)
print(numeros.discard(1))
print(numeros.discard(30))
print(numeros)

print("________________________________________")

# .pop

numeros = {1,2,3,1,2,4,5,5,6,7,8,9,0}

print(numeros)
print(numeros.pop())
print(numeros.pop())
print(numeros)

print("________________________________________")

# len

numeros = {1,2,3,4,5,6,7,8,9,0}

print(len(numeros))

print("________________________________________")

# in

numeros = {1,2,3,4,5,6,7,8,9,0}

print(1 in numeros)
print(10 in numeros)
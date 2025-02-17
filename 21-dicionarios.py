# criação e acesso de dados

# Dicionários Aninhados

pessoa = {"nome": "Augusto", "idade": 37}

pessoa = dict(nome = "Augusto", idade = 37)

pessoa["telefone"] = "1234-5678"

print(pessoa)

print("_______________________________________")

dados = {"nome": "Augusto", "idade": 37, "telefone": "1234-5678"}

print(dados["nome"])
print(dados["idade"])
print(dados["telefone"])

dados["nome"] = "Lais"
dados["idade"] = 33
dados["telefone"] = "9876-5432"

print(dados)

print("_______________________________________")

contatos = {"augusto@gmail.com": {"nome": "Augusto", "telefone": "1234-5678", "extra": "Augusto-1234-5678"},
    "lais@gmail.com": {"nome": "Lais", "telefone": "9876-5432"},
    "tulio@gmail.com": {"nome": "Tulio", "telefone": "1234-9876"}
}

telefone = contatos["tulio@gmail.com"]["telefone"]
print(telefone)

extra = contatos["augusto@gmail.com"]["extra"]
print(extra)

print(contatos)

print("_______________________________________")

# percorrer dicionário

contatos = {
    "augusto@gmail.com": {"nome": "Augusto", "telefone": "1234-5678"},
    "lais@gmail.com": {"nome": "Lais", "telefone": "9876-5432"},
    "tulio@gmail.com": {"nome": "Tulio", "telefone": "1234-9876"}
}
for chave, valor in contatos.items():
    print(chave, valor)


print("_______________________________________")
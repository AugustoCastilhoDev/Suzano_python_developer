def exibir_mensagem():
    print("Olá MUndo!")

def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")
    
def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")
    
exibir_mensagem()    
exibir_mensagem_2(nome="Augusto")
exibir_mensagem_3()
exibir_mensagem_3(nome="Tulio")

print("_______________________________________________")

# Retorno da função

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    
    return antecessor, sucessor

def func_3():
    print("Olá Mundo!")

print(calcular_total([10, 20, 34]))
print(retorna_antecessor_e_sucessor(10))
print(func_3()) # retornar 'none'

print("_______________________________________________")

# Argumentos nomeados

def salvar_carro(marca, modelo, ano, placa):
    #salva carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca} / {modelo} / {ano} / {placa}")
    
salvar_carro("Volkswagen", "Fox", 2018, "ABC-1234")
salvar_carro(marca="Fiat", modelo="Palio", ano="2005", placa="ABC-123")
salvar_carro(**{"marca": "Chevrolet", "modelo": "Onix", "ano": 2016, "placa": "ABC-6789"})

print("_______________________________________________")

def exibir_poema(data_extenso, *lista, **dicionario):
    texto = "\n".join(lista)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in dicionario.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)
    
print(exibir_poema)
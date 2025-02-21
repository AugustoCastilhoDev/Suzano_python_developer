# - Estabelecer um limite de 10 transações diárias para uma conta
# - Se o usuário tentar fdazer uma transação após atingir o limite, deve ser informado que ele excedeu o número de transações permitidas para aquela dia.
# - Mostre no extrato, a data e hora de todas as transações.

import datetime

class ContaBancaria:
    def __init__(self, numero_conta):
        self.numero_conta = numero_conta
        self.saldo = 0
        self.transacoes = []
        self.limite_transacoes = 10

    def depositar(self, valor):
        if self.verificar_limite_transacoes():
            self.saldo += valor
            self.registrar_transacao("Depósito", valor)
        else:
            print("Você excedeu o número de transações permitidas para hoje.")
    
    def sacar(self, valor):
        if self.verificar_limite_transacoes():
            if self.saldo >= valor:
                self.saldo -= valor
                self.registrar_transacao("Saque", valor)
            else:
                print("Saldo insuficiente.")
        else:
            print("Você excedeu o número de transações permitidas para hoje.")

    def verificar_limite_transacoes(self):
        transacoes_hoje = [transacao for transacao in self.transacoes if transacao['data'].date() == datetime.datetime.now().date()]
        return len(transacoes_hoje) < self.limite_transacoes

    def registrar_transacao(self, tipo, valor):
        transacao = {
            "tipo": tipo,
            "valor": valor,
            "data": datetime.datetime.now()
        }
        self.transacoes.append(transacao)

    def extrato(self):
        for transacao in self.transacoes:
            print(f"{transacao['data']} - {transacao['tipo']}: R${transacao['valor']}")

    def historico_transacoes(self):
        print("\nHistórico de Transações:")
        for transacao in self.transacoes:
            print(f"{transacao['data']} - {transacao['tipo']}: R${transacao['valor']}")
    
def menu():
    conta = ContaBancaria(12345)
    
    while True:
        print("\nMENU")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Extrato")
        print("4. Histórico de Transações")
        print("5. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            valor = float(input("Digite o valor para depósito: "))
            conta.depositar(valor)
        elif escolha == "2":
            valor = float(input("Digite o valor para saque: "))
            conta.sacar(valor)
        elif escolha == "3":
            conta.extrato()
        elif escolha == "4":
            conta.historico_transacoes()
        elif escolha == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o menu
menu()

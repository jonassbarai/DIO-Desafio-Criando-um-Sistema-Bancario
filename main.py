from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def adicionar_transacao(self,conta):
        self.contas.append(conta)

    def realizar_transacao(self,conta, transacao):
        transacao.adicionar_transacao(conta)

class Pessoa_fisica(Cliente):
    def __init__(self,cpf, nome, data_nascimento,endereco):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero= numero
        self._agencia= "0001"
        self._cliente= cliente
        self._historico = historico

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        self._historico

    @classmethod
    def nova_conta(cls,numero,cliente):
        return(numero,cliente)

    def sacar(self, valor):
        saldo = self.saldo

        if valor > saldo:
            print("\nsaldo insuficinete para realizar a transação")
        elif valor > 0:
            self.saldo -= valor
            print("\nOperação relaizada com sucesso")
            return true
        else:
            print("\n Operação falhou, valor informado é inválido")

        return false


    def depositar(self, valor):
        saldo = self.saldo

        if valor > 0:
            self.saldo -= valor
            print("\nOperação relaizada com sucesso")
            return true
        else:
            print("\n Operação falhou, valor informado é inválido")
            return false

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite =500,limite_saques = 3):
        super().__init__(numero,cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques =len(
            [transacao for transacao in self.historico.transacoes
            if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self.limite
        exceceu_saques = numero_saques >= self.limite_saques

        if exceceu_saques:
            print("\n usuário atingiu o limite de saques.")
        elif excedeu_limite:
            print("\n usuário atingiu o limite.")
        else:
            return super.sacar(valor)

        return false

    def __str__(self):
        return f"""
        Agência:\t{self.agencia}
        C/C:\t\t{self.numero}
        TiTular:\t{self.cliente.nome}
        """

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self,transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class.__name,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s")
            }
        )

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(cls,conta):
        pass

class Saque(Transacao):
    def __init__(self):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(cls,conta):
        sucesso = conta.sacar(self.valor)

        if sucesso:
            conta.historico.adcionar_transacao(self)

class Deposito(Transacao):

    def __init__(self):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(cls, conta):
        sucesso = conta.depositar(self.valor)

        if sucesso:
            conta.historico.adcionar_transacao(self)



menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[u] Criar Usuário
[c] Conta Corrente
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
AGENCIA = "0001"
numero_conta = 0
contas = []

def criar_cliente(clientes):
    cpf = input("CPF: ")
    usuario = filtrar_usuarios(cpf,clientes)

    if usuario != None:
        print("Usuario já existe")
        return

    nome = input("nome: ")
    data_nascimento = input("data de nascimento: ")
    endereco = input("endereco: ")

    cliente = Pessoa_fisica(cpf, nome, data_nascimento,endereco)

    clientes.append(cliente)
    print("\n=== Cliente criado com sucesso! ===")

def criar_conta(AGENCIA,numero_conta,usuarios, contas):

    cpf = input("digite o CPF do titular da conta:")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario == None:
        print("Usuário inexistente")
        return

    contas.append({
        "agencia": AGENCIA,
        "numero_conta": numero_conta,
        "usuario": usuario
    })

    listar_contas(contas)

def filtrar_usuarios(cpf,clientes):
    for cliente in clientes:
        if cliente.cpf == cpf:
            return cliente

def listar_contas(contas):
    for conta in contas:
        linhas = f"""
            Agencia:\t {conta["agencia"]}
            C/C:\t\t {conta["numero_conta"]}u
            titular:\t{conta["usuario"]["nome"]}            
        """
        print(textwrap.dedent(linhas))

def imprimir_extrato(saldo,/,*,extrato):

    print(" EXTRATO ".center(41,"="))
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("".center(41,"="))

def saque(*,saldo,valor,extrato,limite,numero_saques,LIMITE_SAQUES):

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        return saldo, extrato

    else:
        print("Operação falhou! O valor informado é inválido.")
    pass

def deposito(saldo,valor,extrato,/):

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        return saldo, extrato

    else:
        print("Operação falhou! O valor informado é inválido.")

if __name__ == '__main__':
     clientes =[]
     contas = []
     while True:

         opcao = input(menu)

         if opcao == "d":
             valor = float(input("digite o valor do deposito: "))
             saldo, extrato = deposito(saldo,valor,extrato)
         elif opcao == "s":
             valor = float(input("digite o valor do saque: "))
             saldo, extrato = saque(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES)
         elif opcao == "e":
             imprimir_extrato(saldo,extrato=extrato)
         elif opcao == "c":
            numero_conta += 1
            #criar_conta(AGENCIA,numero_concta,usuarios,contas)
         elif opcao == "u":
             criar_cliente(clientes)
         elif opcao == "q":
             break
         else:
             print("Opção inválida")
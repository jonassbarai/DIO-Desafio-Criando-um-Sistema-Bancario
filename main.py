import textwrap

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
usuarios =[]
contas = []

def criar_usuario(usuarios):
    cpf = input("CPF: ")
    usuario = filtrar_usuarios(cpf,usuarios)

    if usuario != None:
        print("Usuario já existe")
        return

    nome = input("nome: ")
    data_nascimento = input("data de nascimento: ")
    endereco = input("endereco: ")

    usuarios.append(
        {"nome": nome,
         "cpf": cpf,
         "data_nascimento": data_nascimento,
         "endereco": endereco
         })

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

def filtrar_usuarios(cpf,usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario

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
             criar_conta(AGENCIA,numero_conta,usuarios,contas)
         elif opcao == "u":
             criar_usuario(usuarios)
         elif opcao == "q":
             break
         else:
             print("Opção inválida")
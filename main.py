menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def imprimir_extrato():

    print(" EXTRATO ".center(41,"="))
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("".center(41,"="))

def saque(valor):
    global saldo, limite, numero_saques,extrato, LIMITE_SAQUES

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

    else:
        print("Operação falhou! O valor informado é inválido.")
    pass

def deposito(valor):
    global saldo, limite, extrato

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
        print("Operação falhou! O valor informado é inválido.")

if __name__ == '__main__':

     while True:

         opcao = input(menu)

         if opcao == "d":
             valor = float(input("digite o valor do deposito: "))
             deposito(valor)
         elif opcao == "s":
             valor = float(input("digite o valor do saque: "))
             saque(valor)
         elif opcao == "e":
             imprimir_extrato()
         elif opcao == "q":
             break
         else:
             print("Opção inválida")



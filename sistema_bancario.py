menu = """======== MENU ========

[1] DEPÓSITO
[2] SAQUE
[3] EXTRATO
[0] SAIR 

QUAL AÇÃO DESEJA REALIZAR?
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao == "1":
        valor = float(input("VALOR DO DEPÓSITO: "))

        if valor > 0:
            saldo += valor
            extrato += f"DEPÓSITO: R$ {valor:.2f}\n"

        else:
            print("Valor inválido.")

    elif opcao == "2":
        valor = float(input("VALOR DO SAQUE: "))

        saldo_excedido = valor > saldo
        limite_excedido = valor > limite
        saque_excedido = numero_saques >= LIMITE_SAQUES

        if saldo_excedido:
            print("SALDO INSUFICIENTE.")

        elif limite_excedido:
            print("LIMITE DO VALOR DO SAQUE EXCEDIDO.")

        elif saque_excedido:
            print("LIMITE DE SAQUES EXCEDIDO.")

        elif valor > 0:
            saldo -= valor
            extrato += f'SAQUE: R$ {valor:.2f}\n'
            numero_saques += 1

        else:
            print("Valor inválido.")

    elif opcao == "3":
        print("\n======= EXTRATO =======")
        print("Não foi indetificado movimentações" if not extrato else extrato)
        print(f"\nSALDO: R$ {saldo:.2f}")
        print("=======================\n")

    elif opcao == "0":
        break

    else:
        print("OPÇÃO INVÁLIDA! TENTE NOVAMENTE.")
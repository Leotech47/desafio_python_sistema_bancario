# Criação do MENU
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

# Declaração das variaveis:
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

# O programa roda dentro de um Bloco condicional WHILE:
while True:
# Aparece na tela o MENU para o correntista digitar a opção:
    opcao = input(menu)
# Se o cliente digitar a opção "d" para depósito:
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
# Se o valor digitado for maior que ZERO:
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
# Caso o cliente digite um valor igual ou menor que zero:
        else:
            print("Operação falhou! O valor informado é inválido.")
# Caso o cliente digite a opção "s" para sacar:
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
# Declaração das variaveis locais neste bloco elif:
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES
# 1ª condição: excedeu_saque:
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
# 2ª condição: excedeu_limite:
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
#3ª condição: excedeu_saque:
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
# 4ª condição:
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
# 5ª condição: o cliente digitou um valor menor que zero:
        else:
            print("Operação falhou! O valor informado é inválido.")

# O # Caso o cliente digite a opção "e" para extrato:
    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
# Caso o cliente digite a opção "q" para sair, o código executa a operação break
    elif opcao == "q":
        break
# Caso o cliente digite um caracter diferente das opções no MENU:
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")


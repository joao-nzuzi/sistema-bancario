
menu = """
        ****** Escolha uma operação ******
        [1] - Depósito
        [2] - Levantamento
        [3] - Extrato
        [4] - Sair
"""

NUMERO_LEVANTAMENTO_DIARIO_PERMITIDO = 3
LIMITE_LEVANTAMENTO_DIARIO_PERMITIDO = 500
saldo = 0
extrato = ""
numero_levantamento_feitos = 0

while True:
    opcao = input (menu)
    if opcao == '1':
        valor = float(input('Informa o valor que deseja depositar: '))
        if valor >= 0:
            saldo += valor
            extrato += f"Depósito feito com sucesso. Valor depositado: R$ {valor:.2f}\n"
        else:
            print("É apenas permitido depósito de valor positivo. Por favor, informa um valor positivo.")
            
    elif opcao == '2':
        if numero_levantamento_feitos >= 0 and numero_levantamento_feitos <= NUMERO_LEVANTAMENTO_DIARIO_PERMITIDO - 1:
            valor = float(input('Informa o valor que deseja levantar: '))
            if valor <= saldo:
                if valor >= 0 and valor <= LIMITE_LEVANTAMENTO_DIARIO_PERMITIDO:
                    saldo -= valor
                    extrato += f"Levantamento feito com sucesso. Valor levantado: R$ {valor:.2f}\n"
                    numero_levantamento_feitos += 1
                else:
                    print(f"Excedeu o limite do valor máximo permitido por levantamento. Só é permitido levantar R$ {LIMITE_LEVANTAMENTO_DIARIO_PERMITIDO:.2f} por vez.")
            else:
                print("Não é possivel levantar o dinheiro por falta de saldo na conta.")
        else:
            print(f"Excedeu o nº de levantamento permitidos por dia. Só é permitido {NUMERO_LEVANTAMENTO_DIARIO_PERMITIDO} por dia")
            
    elif opcao == '3':
        print(f"""****** Movimentos da conta: ******\n{ "Não foram realizados movimentos na conta. " if not extrato else extrato.strip()}""" )
        print()
        print(f"Saldo actual: {saldo:.2f}")
        
    elif opcao == '4':
        break
    else:
        print('Operação inválida. Por favor, informa novamente a operação que deseja realizar')
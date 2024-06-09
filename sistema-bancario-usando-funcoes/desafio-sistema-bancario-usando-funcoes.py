
import textwrap
import datetime

def menu():
    menu = """
        ****** Escolha uma operação ******
        [1] - Depósito
        [2] - Levantamento
        [3] - Extrato
        [4] - Cadastrar Cliente
        [5] - Criar Conta
        [6] - Listar Contas
        [7] - Sair
    """
    return input(textwrap.dedent(menu)+"\n")

def depositar(saldo, extrato, valor, /):
    
    if valor >= 0:
        saldo += valor
        extrato += f"Foi depositado: R$ {valor:.2f} aos {datetime.datetime.now().strftime('%H:%M:%S')}\n"
        print("Depósito feito com sucesso")
    
    else:
        print("É apenas permitido depósito de valor positivo. Por favor, informa um valor positivo.")
        
    return saldo, extrato

def levantar(*, saldo, extrato, limite_levantamento_diario, numero_levantamento_diario, numero_levantamento_feitos):
    
    if numero_levantamento_feitos >= 0 and numero_levantamento_feitos <= numero_levantamento_diario - 1:
        
        valor = float(input('\nInforma o valor que deseja levantar: '))
        
        if valor <= saldo:
            if valor >= 0:
                if valor <= limite_levantamento_diario:
                    saldo -= valor
                    global hora
                    extrato += f"Foi levantado: R$ {valor:.2f} aos {datetime.datetime.now().strftime('%H:%M:%S')}\n"
                    numero_levantamento_feitos += 1
                    print("Depósito feito com sucesso")
                else:
                    print(f"Excedeu o limite do valor máximo permitido por levantamento. Só é permitido levantar R$ {limite_levantamento_diario:.2f} por vez.")
            else:
                print("É apenas permitido levantamento de valor positivo. Por favor, informa um valor positivo.")
        else:
            print("Não é possivel levantar o dinheiro por falta de saldo na conta.")
    else:
        print(f"Excedeu o nº de levantamento permitidos por dia. Só é permitido {numero_levantamento_diario} por dia")
    
    return saldo, extrato

def extrato_bancario(saldo, /, *, extrato):
    print(f"""\n****** Movimentos da conta aos {datetime.date.today()} ******\n{ "Não foram realizados movimentos na conta. " if not extrato else extrato.strip()}""" )
    print()
    print(f"Saldo actual: {saldo:.2f}")
    
def cadastrar_cliente(nome, data_nascimento, cpf, endereco):
    clientes = {"Nome": nome, "Data Nascimento": data_nascimento, "CPF": cpf, "Endereço": endereco}
    print(clientes)

def filtrar_clientes(cpf, clientes):
    pass

def criar_contas(agencia, numero_conta, clientes):
    pass

def executar():
    NUMERO_LEVANTAMENTO_DIARIO_PERMITIDO = 3
    LIMITE_LEVANTAMENTO_DIARIO_PERMITIDO = 500
    AGENCIA = "001"
    saldo = 0
    extrato = ""
    numero_levantamento_feitos = 0
    clientes = []
    contas = []

    while True:
        opcao = menu()
        
        if opcao == '1':
            valor = float(input('\nInforma o valor que deseja depositar: '))
            
            saldo, extrato = depositar(saldo, extrato, valor)
                
        elif opcao == '2':
            saldo, extrato = levantar(
                saldo=saldo, 
                extrato=extrato, 
                limite_levantamento_diario=LIMITE_LEVANTAMENTO_DIARIO_PERMITIDO, 
                numero_levantamento_diario=NUMERO_LEVANTAMENTO_DIARIO_PERMITIDO,
                numero_levantamento_feitos=numero_levantamento_feitos
                )
               
        elif opcao == '3':
             extrato_bancario(saldo, extrato=extrato)
             
        elif opcao == '4':
            nome_cliente = input("Informa o nome do cliente")
            datanasc = input("Informa a data do cliente")
            numero_docmento = input("Informa o nº do documento")
            morada = input("Informa O endereço: rua, º casa, bairro - cidade/sigla estado")
            cadastrar_cliente(nome_cliente, datanasc, numero_docmento, morada)
            
        elif opcao == '5':
            break
        
        elif opcao == '6':
            break
            
        elif opcao == '7':
            break
        else:
            print('Operação inválida. Por favor, informa novamente a operação que deseja realizar')
            
executar()

from abc import ABC, abstractmethod
import datetime


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
        
    def realizar_transacao(self,  conta, transacao):
        transacao.registar(conta)
    
    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        
class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = '001', 
        self._cliente = cliente,
        self._historico = Historico()
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
        
    @property
    def historico(self):
        return self._historico
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(cliente, numero)
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print('Operação de depósito realizada com sucesso')
        else: 
            print('Por ondem do seu banco não pode realizar a operação. Valor informado inválido')
            return False
        
        return True
    
    def levantar(self, valor):
        saldo = self.saldo
        excedeu_saldo_disponivel = valor > saldo
        if excedeu_saldo_disponivel:
            print("O valor informado é superior ao saldo disponível. Por favor, tente outra vez")
            
        elif valor > 0:
            self.saldo -= valor
            print('Operação de levantamento realizada com sucesso')
            return True
        
        return False

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite_levantamento_por_vez = 500, limite_levantamento_diario = 3):
        super().__init__(numero, cliente)
        self.limite = limite_levantamento_por_vez
        self.limite_saques = limite_levantamento_diario
        
    def levantar(self, valor):
        numero_levantamento_feitos = len([transacao for transacao in self.historico if transacao["tipo"] == Levantamento.__name__])
        
        if numero_levantamento_feitos < self.limite_levantamento_diario:
            if valor > 0:
                if valor <= self.limite_levantamento_por_vez:
                    return super().levantar(valor)
                else:
                    print(f"Excedeu o limite do valor máximo permitido por levantamento. Só é permitido levantar R$ {self.limite_levantamento_por_vez:.2f} por vez.")
            else:
                print("Por ondem do seu banco não pode realizar a operação. Valor informado inválido")
        else:
            print(f"Excedeu o nº de levantamento permitidos por dia. Só é permitido {self.limite_levantamento_diario} por dia")
        
        return False
    
    def __str__(self):
        return f"""Agência: {self.agencia}
                   Conta Corrente: {self.numero} 
                   Nome Titular: {self.cliente.nome}
                   """
        
class Historico:
    def __init__(self):
        self._transacoes = []
    
    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self.transacoes.append({'tipo': transacao.__Class__.__name,
                                'valor': transacao.valor,
                                'data operacacao': datetime.datetime.now().strftime('%H:%M:%S')
                                })
        
class Transacao(ABC):
    
    @classmethod
    @abstractmethod
    def registar(self, conta):
        pass

    @property
    @abstractmethod
    def valor(self):
        pass
    
class Deposito(Transacao):
    @property
    def valor(self):
        return self._valor
    
    def __init__(self, valor):
        self._valor = valor
        
    def registar(self, conta):
        if conta.depositar(self.valor):
            conta.historico.adicionar_transacao(self)
    
class Levantamento(Transacao):
    @property
    def valor(self):
        return self._valor
    
    def __init__(self, valor):
        self._valor = valor
        
    def registar(self, conta):
        if conta.levantar(self.valor):
            conta.historico.adicionar_transacao(self)
    
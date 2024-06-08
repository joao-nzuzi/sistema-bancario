# ***Desafio Sistema Bancário Usando Funções***
Existe a necessidade de tornar o código mais modularizado, legível, evolutivo, reutilizável e de fácil manutenção, e para tal será necessário o uso de funções.

## Objectivo Geral
O objectivo desse desafio consiste em tornar as operações de saque, deposito e extrato numa função cada. Além disso, para a versão 2 do nosso sistema bancário será necessário criar mais duas funções, a saber: cadastrar usuario / cliente e cadastrar conta bancária (vincular a conta com o cliente).

### Regras para o levantamento / saque
A função da operação de levantamento deve receber apenas argumentos do tipo keyword.

## Regras para o depósito
A função da operação deve receber apenas orgumentos do tipo posicional.

### Regras para o extrato
A função da extrato deve receber orgumentos do tipo posicional e keyword. O argumento Saldo como posicional  e o extrato com keyword.

### Regras para o cliente / usuário
Os clientes devem ser armazenados em um lista e devem ter os seguintes campos: nome, data de nascimento, cpf e endereço. O endereço é uma string com o seguinte formato: rua, nro da casa - bairro - cidade/sigla estado. Apenas é necessário armazenar os numeros do CPF e o mesmo não pode ser usado em mais de um cliente.

Um usuário / cliente pode ter mais de uma conta, mas uma conta pertence a somente um usuário.

> [!TIP]
> Por se tratar de uma info do tipo chave-valor, a melhor estrutura de dados a se usar é um dicionário `dict`.

### Regras para as contas
As contas deve ser armazenadas em um lista e deve ter os seguintes campos: agência, numero conta e usuário / cliente. O num da conta é sequencial (começa em 1 e incrementa 1 a cada conta criada). O número da agência é fixo "0001".

> [!TIP]
> Por se tratar de uma info do tipo chave-valor, a melhor estrutura de dados a se usar é um dicionário `dict`.

> [!TIP]
> Para vincular uma conta, filtre a lista (`dict`) de usuário / cliente pelo cpf informado por cada usuário da lista (`dict`)


# Desafio: Criando um sistema bancário pela [DIO](https://web.dio.me/users/giovanakr)

## Descrição do desafio
Criar um sistema bancário em Python com as operações: depositar, sacar
e visualizar extrato.

**DEPÓSITO:** A v1 do projeto trabalha apenas com 1 usuário, essa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

**SAQUE:** O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

**EXTRATO:** Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações

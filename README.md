# Sistema Bancário

Este projeto é um sistema bancário simples desenvolvido em Python que simula operações básicas de um banco, como criar contas, realizar depósitos, saques, e exibir extratos. O sistema é orientado a objetos e utiliza conceitos como herança, polimorfismo e abstração para organizar o código de forma modular e reutilizável.

## Funcionalidades

- **Criar Cliente:** Permite criar um novo cliente informando CPF, nome, data de nascimento e endereço.
- **Criar Conta Corrente:** Cria uma nova conta corrente associada a um cliente existente.
- **Depósito:** Realiza depósitos em contas existentes.
- **Saque:** Permite saques respeitando limites pré-definidos de valor e quantidade de saques por dia.
- **Extrato:** Exibe o extrato da conta com todas as transações realizadas.
- **Listar Contas:** Lista todas as contas criadas no sistema.

## Estrutura do Projeto

- `Cliente`: Classe base que representa um cliente com endereço e lista de contas.
- `PessoaFisica`: Subclasse de `Cliente` que adiciona nome, data de nascimento e CPF.
- `Conta`: Classe base para contas bancárias, com funcionalidades básicas como saque e depósito.
- `ContaCorrente`: Subclasse de `Conta` com limite de saque e número de saques permitidos.
- `Historico`: Classe para armazenar e gerenciar o histórico de transações de uma conta.
- `Transacao`: Classe abstrata para transações, utilizada para saques e depósitos.
- `Saque` e `Deposito`: Subclasses de `Transacao` para registrar saques e depósitos, respectivamente.

## Como Usar

1. Clone este repositório:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <NOME_DO_REPOSITORIO>

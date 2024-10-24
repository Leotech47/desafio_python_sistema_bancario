## Explicação do Código

Este código simula um sistema bancário simples com as seguintes funcionalidades:

**Funcionalidades:**

* **Depósito:** Permite que os usuários depositem fundos em sua conta.
* **Saque:** Permite que os usuários retirem fundos, com limites no valor e número de saques.
* **Extrato:** Exibe um registro das transações e o saldo atual.
* **Sair:** Permite que os usuários saiam do programa.

**Explicação do Código:**

**Criação do Menu:**

```python
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
```

Isso cria uma variável de string de várias linhas chamada `menu` que armazena as opções apresentadas ao usuário.

**Inicialização de Variáveis:**

```python
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
```

* `saldo`: Armazena o saldo da conta, inicialmente definido como 0.
* `limite`: Armazena o limite de saque, definido como 500.
* `extrato`: Armazena o histórico de transações como uma string, inicialmente vazia.
* `numero_saques`: Armazena o número de saques realizados, inicialmente 0.
* `LIMITE_SAQUES`: Armazena o número máximo de saques permitidos, definido como 3.

**Loop Principal:**

```python
while True:
    opcao = input(menu)
    # ... (resto do código) ...
```

A instrução `while True:` cria um loop infinito, o que significa que o código dentro dele será executado repetidamente até ser explicitamente interrompido. 
`opcao = input(menu)`: Exibe o `menu` para o usuário e solicita que ele insira uma opção. A entrada é armazenada na variável `opcao`.

**Depósito (d):**

```python
if opcao == "d":
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
```

Se o usuário inserir "d", o programa solicita um valor de depósito.
Se o valor for positivo, ele é adicionado ao `saldo` e registrado no `extrato`.
Se o valor for inválido (zero ou negativo), uma mensagem de erro é exibida.

**Saque (s):**

```python
elif opcao == "s":
    # ... (lógica de saque) ...
```

Se o usuário inserir "s", o programa inicia o processo de saque, verificando várias condições antes de permitir o saque:

* Verifica se o valor do saque excede o saldo (`excedeu_saldo`).
* Verifica se o valor do saque excede o limite (`excedeu_limite`).
* Verifica se o número de saques atingiu o máximo (`excedeu_saques`).

Se todas as verificações forem aprovadas, o programa deduz o valor do `saldo`, atualiza o `extrato` e incrementa `numero_saques`.
Se alguma verificação falhar, ele exibe uma mensagem de erro apropriada.

**Extrato (e):**

```python
elif opcao == "e":
    # ... (lógica de exibição do extrato) ...
```

Se o usuário inserir "e", o programa imprime o `extrato` mostrando as transações e o `saldo` atual.

**Sair (q):**

```python
elif opcao == "q":
    break
```

Se o usuário inserir "q", a instrução `break` é executada, encerrando o loop `while` e finalizando o programa.

**Opção Inválida:**

```python
else:
    print("Operação inválida, por favor selecione novamente a operação desejada.")
```

Se o usuário inserir qualquer caractere diferente de "d", "s", "e" ou "q", uma mensagem de erro é exibida.


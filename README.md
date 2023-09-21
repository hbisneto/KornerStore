# Korner Store

## Menu

1. **Adicionar produtos na sacola**: Esta opção permite que você adicione produtos à sua sacola de compras. Você poderá ver o nome e o valor de cada produto adicionado.

2. **Calcular valor total**: Depois de adicionar todos os produtos desejados à sacola, você pode usar esta opção para calcular o valor total de sua compra.

3. **Aplicar desconto**: Se você estiver cadastrado na Korner Store, poderá usar esta opção para aplicar um desconto à sua compra.

4. **Fechar a venda**: Após a aplicação de quaisquer descontos e a confirmação do valor total, você pode usar esta opção para fechar a venda. Isso irá concluir a sua compra e esvaziar os itens da sacola.

```py
===================================================================
KORNER STORE
===================================================================
1. Adicionar produto à sacola
2. Calcular valor total
3. Aplicar desconto
4. Fechar venda
===================================================================
>> Escolha uma das opções: 
```

### 1. Adicionando produtos à sacola

Para adicionar produtos à sacola, necessário escrever o nome do produto que deseja adicionar.

```py
===================================================================
KORNER STORE
===================================================================
1. Adicionar produto à sacola
2. Calcular valor total
3. Aplicar desconto
4. Fechar venda
===================================================================
>> Escolha uma das opções: 1
===================================================================
>> Digite o nome do produto: Pera
===================================================================
```

> Note que o produto deve estar previamente cadastrado no dicionário chamado "products". Por padrão, alguns itens já estão cadastrados, contendo nome e preço
> 
>```py
>products = {
>    "Banana": ["Banana Pepino", 1.20],
>    "Maca": ["Maça do vale", 2.30],
>    "Manga": ["Manga cera", 2.50],
>    "Pera": ["Pera amarela", 5],
>    "Uva": ["Uva de marte", 10],
>    "Sacola": ["Sacola pRástica", 0.05]
>}
>```

### 2. Calcular valor total

Essa opção calcula o total a pagar com base nos itens no carrinho, representado pela lista kart.

```py
kart = []
```

<br>
Se um item não estiver em products, a função imprime uma mensagem informando que o item não está cadastrado.


```py
===================================================================
HISTÓRICO DE COMPRAS
===================================================================
1 - Produtos no meu saco: Pera amarela
[!] - O item "Jarro" não foi cadastrado nos produtos
===================================================================
```

### 3. Aplicar desconto

Essa opção calcula o total a pagar pelos itens no carrinho, aplica um desconto fornecido e, em seguida, solicita o CPF do cliente. Se o cliente estiver cadastrado, a função imprime os detalhes do cliente e o total a pagar com desconto. Se o cliente não estiver cadastrado, a função informa que o cliente não está cadastrado e imprime o total da compra sem desconto.

```py
===================================================================
DESCONTO
===================================================================
>> Digite a porcentagem de desconto [1-100]: 10
===================================================================
>> Digite o CPF do cliente: 00000000001
===================================================================

===================================================================
SOBRE O CLIENTE
===================================================================
Nome do Cliente: Guido van Rossum
Idade do Cliente: 67 anos
Altura do Cliente: 1.73m
Peso do Cliente: 75 kgs
===================================================================
>> Com o desconto, o total a pagar é de R$ 4.5
===================================================================
```

```py
===================================================================
DESCONTO
===================================================================
>> Digite a porcentagem de desconto [1-100]: 10
===================================================================
>> Digite o CPF do cliente: 12345678921
===================================================================
>> O cliente não está cadastrado. O total da compra é de R$ 5
===================================================================
```

> Note que o cliente deve estar previamente cadastrado no dicionário chamado "clients". Por padrão, alguns itens já estão cadastrados, contendo nome, idade, altura e peso.
> 
>```py
>clients = {
>    "00000000001": ["Guido van Rossum", 67, 1.73, 75],
>    "00000000002": ["William Henry 'Bill' Gates III", 67, 1.78, 70],
>    "00000000003": ["Elon Reeve Musk", 52, 1.88, 82],
>    "00000000004": ["Mark Elliot Zuckerberg", 39, 1.71, 70],
>    "00000000005": ["Valesca Reis Santos", 44, 1.65, 60],
>    "00000000006": ["Jaqueline", 13, 1.53, 52]
>}
>```


#### Outros exemplos:

```py
===================================================================
DESCONTO
===================================================================
>> Digite a porcentagem de desconto [1-100]: 10
===================================================================
>> Digite o CPF do cliente: 00000000005
===================================================================

===================================================================
SOBRE O CLIENTE
===================================================================
Nome do Cliente: Valesca Reis Santos
Idade do Cliente: 44 anos
Altura do Cliente: 1.65m
Peso do Cliente: 60 kgs
===================================================================
>> Com o desconto, o total a pagar é de R$ 4.5
===================================================================
```

### 4. Fechar a venda

Essa opção serve para fechar o processo de venda: Todos os valores de cobranças e todos os itens no carrinho são excluídos.

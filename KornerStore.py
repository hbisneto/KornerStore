kart = []

### OS PRODUTOS EM "kart" PRECISAM ESTAR CADASTRADOS NO DICIONÁRIO "products"
products = {
    "Banana": ["Banana Pepino", 1.20],
    "Maca": ["Maça do vale", 2.30],
    "Manga": ["Manga cera", 2.50],
    "Pera": ["Pera amarela", 5],
    "Uva": ["Uva de marte", 10],
    "Sacola": ["Sacola pRástica", 0.05]
}

### OS CLIENTES COM DIREITO AO DESCONTO PRECISAM ESTAR CADASTRADOS NO DICIONÁRIO "clients"
clients = {
    "00000000001": ["Guido van Rossum", 67, 1.73, 75],
    "00000000002": ["William Henry 'Bill' Gates III", 67, 1.78, 70],
    "00000000003": ["Elon Reeve Musk", 52, 1.88, 82],
    "00000000004": ["Mark Elliot Zuckerberg", 39, 1.71, 70],
    "00000000005": ["Valesca Reis Santos", 44, 1.65, 60],
    "00000000006": ["Jaqueline", 13, 1.53, 52]
}

def start():
    loop = True
    while loop == True:
        print()
        print("="*80)
        print("KORNER STORE")
        print("="*80)
        print("1. Adicionar produto à sacola")
        print("2. Calcular valor total")
        print("3. Aplicar desconto")
        print("4. Fechar venda")
        print("="*80)
        userInput = int(input(">> Escolha uma das opções: "))
        print("="*80)

        if userInput == 1:
            addProdInput = str(input(">> Digite o nome do produto: "))
            kart.append(addProdInput)
            print("="*80)
        elif userInput == 2:
            getProductFromName()
        elif userInput == 3:
            print()
            print("="*80)
            print("DESCONTO")
            print("="*80)
            userInput = float(input(">> Digite a porcentagem de desconto [1-100]: "))
            print("="*80)
            discount(userInput)
        elif userInput == 4:
            kart.clear()
        elif userInput == 0:
            loop = False

### MOSTRA OS ITENS NO HISTÓRICO E O TOTAL A PAGAR
def getProductFromName(toPay = 0):
    print()
    print("="*80)
    print("HISTÓRICO DE COMPRAS")
    print("="*80)
    count = 0
    try:
        for i in kart:
            count += 1
            prodName = f'{i}'
            toPay += products[prodName][1]
            print(f'{count} - Produtos no meu saco: {products[prodName][0]}')
    except:
        print(f'[!] - O item "{i}" não foi cadastrado nos produtos')
    print("="*80)
    print()
    print("="*80)
    print("TOTAL A PAGAR")
    print("="*80)
    print(">> Total a pagar: R$", toPay)
    print("="*80)

### SOMENTE SERÁ APLICADO DESCONTO EM CASOS DE CLIENTES CADASTRADOS
def discount(percent):
    toPay = 0
    for i in kart:
        prodName = f'{i}'
        toPay += products[prodName][1]
    discountPrice = toPay - ((toPay / 100) * percent)
    userInput = str(input(">> Digite o CPF do cliente: "))
    print("="*80)
    try:
        if clients[userInput]:
            print()
            print("="*80)
            print("SOBRE O CLIENTE")
            print("="*80)
            print(f'Nome do Cliente: {clients[userInput][0]}')
            print(f'Idade do Cliente: {clients[userInput][1]} anos')
            print(f'Altura do Cliente: {clients[userInput][2]}m')
            print(f'Peso do Cliente: {clients[userInput][3]} kgs')
            print("="*80)
            print(f'>> Com o desconto, o total a pagar é de R$ {discountPrice}')
            print("="*80)
    except:
        print(f'>> O cliente não está cadastrado. O total da compra é de R$ {toPay}')
        print("="*80)

start()
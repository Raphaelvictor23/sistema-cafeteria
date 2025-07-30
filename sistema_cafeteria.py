produtos = []  # Lista de produtos cadastrados
clientes = []  # Lista de clientes
pedidos = []   # Lista de pedidos

def cadastrar_produto():
    nome = input("Nome do produto: ")
    preco = float(input("Preço: R$ "))
    ingredientes = input("Ingredientes: ")
    produto = {"nome": nome, "preco": preco, "ingredientes": ingredientes}
    produtos.append(produto)
    print("Produto cadastrado com sucesso!\n")

def exibir_cardapio():
    if not produtos:
        print("Nenhum produto cadastrado.\n")
    else:
        for i, p in enumerate(produtos):
            print(f"{i+1}. {p['nome']} - R${p['preco']:.2f} ({p['ingredientes']})")
        print("Cardápio exibido com sucesso!\n")

def cadastrar_cliente():
    nome = input("Nome do cliente: ")
    telefone = input("Telefone: ")
    cliente = {"nome": nome, "telefone": telefone}
    clientes.append(cliente)
    print("Cliente cadastrado com sucesso!\n")

def realizar_pedido():
    nome_cliente = input("Nome do cliente: ")
    exibir_cardapio()
    escolha = int(input("Digite o número do produto escolhido: ")) - 1
    if 0 <= escolha < len(produtos):
        pedido = {"cliente": nome_cliente, "produto": produtos[escolha]}
        pedidos.append(pedido)
        print("Pedido registrado com sucesso!\n")
    else:
        print("Produto inválido.\n")

def menu():
    while True:
        print("1. Cadastrar produto")
        print("2. Exibir cardápio")
        print("3. Cadastrar cliente")
        print("4. Realizar pedido")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            exibir_cardapio()
        elif opcao == "3":
            cadastrar_cliente()
        elif opcao == "4":
            realizar_pedido()
        elif opcao == "5":
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida!\n")

# Chamada do menu principal
menu()
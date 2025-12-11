"""
def ex9():
# Função para adicionar um produto à lista
def adicionar_produto(lista):
    nome = input("Digite o nome do produto: ")
    try:
        preco = float(input("Digite o preço do produto em euros (€): "))
        produto = {"nome": nome, "preco": preco}  # Cria um dicionário com nome e preço
        lista.append(produto)  # Adiciona o produto à lista
        print(f"Produto '{nome}' adicionado com sucesso!\n")
    except ValueError:
        print("Preço inválido. Tente novamente.\n")

# Função para listar todos os produtos na lista
def listar_produtos(lista):
    if not lista:  # Verifica se a lista está vazia
        print("Lista de compras vazia.\n")
        return
    print("\n📋 Lista de produtos:")
    for i, item in enumerate(lista, start=1):  # Mostra cada produto com número
        print(f"{i}. {item['nome']} - € {item['preco']:.2f}")
    print()  # Linha em branco

# Função para calcular o total da compra
def calcular_total(lista):
    total = sum(item["preco"] for item in lista)  # Soma todos os produtos
    print(f"💰 Total da compra: € {total:.2f}\n")

# Função principal com o menu
def menu_lista_compras():
    lista_compras = []  # Lista produtos

    while True:  # Loop para manter o menu a correr até o utilizador pedir p sair
        print("==== MENU LISTA DE COMPRAS ====")
        print("1 - Adicionar produto")
        print("2 - Listar produtos")
        print("3 - Calcular total")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_produto(lista_compras)
        elif opcao == "2":
            listar_produtos(lista_compras)
        elif opcao == "3":
            calcular_total(lista_compras)
        elif opcao == "0":
            print("Saindo do programa. Até logo!")
            break  # para o if
        else:
            print("Opção inválida. Tente novamente.\n")

menu_lista_compras() #chama a funcao
"""
def ex9():
    def adicionar_produto(lista):
        nome = input("Digite o nome do produto: ")
        try:
            preco = float(input("Digite o preço do produto em euros (€): "))
            produto = {"nome": nome, "preco": preco}  # Gravando nome e preço juntos
            lista.append(produto)  # Add o produto à lista
            print(f"Produto '{nome}' adicionado com sucesso!\n")
        except ValueError:
            print("Preço inválido. Tente novamente.\n")

    # Função para listar todos os produtos na lista
    def listar_produtos(lista):
        if not lista:  # Verifica se a lista está vazia
            print("Lista de compras vazia.\n")
            return
        print("\n📋 Lista de produtos:")
        for i, item in enumerate(lista, start=1):  # Mostra cada produto com número
            print(f"{i}. {item['nome']} - € {item['preco']:.2f}")
        print()  # Linha em branco

    # Função para calcular o total da compra
    def calcular_total(lista):
        total = sum(item["preco"] for item in lista)  # Soma todos os produtos
        print(f"💰 Total da compra: € {total:.2f}\n")

    # Função principal com o menu!!
    def menu_lista_compras():
        lista_compras = []  # Lista produtos

        while True:  # Loop para manter o menu a correr até o utilizador pedir p sair
            print("==== MENU LISTA DE COMPRAS ====")
            print("1 - Adicionar produto")
            print("2 - Listar produtos")
            print("3 - Calcular total")
            print("0 - Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                adicionar_produto(lista_compras)
            elif opcao == "2":
                listar_produtos(lista_compras)
            elif opcao == "3":
                calcular_total(lista_compras)
            elif opcao == "0":
                print("Saindo do programa. Até logo!")
                break  # para o if
            else:
                print("Opção inválida. Tente novamente.\n")

    menu_lista_compras()  # chama a funcao
ex9() #chama a funcao novamente
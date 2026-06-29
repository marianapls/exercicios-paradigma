
produtos = []


quantidade = int(input("Quantos produtos deseja cadastrar? "))

for i in range(quantidade):
    print("Produto", i + 1)

    nome = input("Nome do produto: ")
    estoque = int(input("Quantidade em estoque: "))
    preco = float(input("Preço unitário: "))

    produto = [nome, estoque, preco]
    produtos.append(produto)


opcao = ""

while opcao != "e":

    print("MENU")
    print("a - Adicionar unidades ao estoque")
    print("b - Retirar unidades do estoque")
    print("c - Consultar um produto")
    print("d - Listar todos os produtos")
    print("e - Encerrar")

    opcao = input("Escolha uma opção: ")

    
    if opcao == "a":

        nome = input("Digite o nome do produto: ")

        for produto in produtos:
            if produto[0] == nome:

                adicionar = int(input("Quantidade para adicionar: "))
                produto[1] = produto[1] + adicionar

                print("Estoque atualizado!")

  
    elif opcao == "b":

        nome = input("Digite o nome do produto: ")

        for produto in produtos:
            if produto[0] == nome:

                retirar = int(input("Quantidade para retirar: "))

                if retirar <= produto[1]:
                    produto[1] = produto[1] - retirar
                    print("Retirada realizada!")
                else:
                    print("Estoque insuficiente!")


    elif opcao == "c":

        nome = input("Digite o nome do produto: ")

        for produto in produtos:
            if produto[0] == nome:

                valor_total = produto[1] * produto[2]

                print("Produto encontrado")
                print("Nome:", produto[0])
                print("Quantidade:", produto[1])
                print("Preço unitário: R$", produto[2])
                print("Valor total em estoque: R$", valor_total)

    # Listar produtos
    elif opcao == "d":

        print("LISTA DE PRODUTOS")

        for produto in produtos:

            valor_total = produto[1] * produto[2]

            print("Nome:", produto[0])
            print("Quantidade:", produto[1])
            print("Preço unitário: R$", produto[2])
            print("Valor total: R$", valor_total)

    # Encerrar
    elif opcao == "e":
        print("Programa encerrado!")

    else:
        print("Opção inválida!")

produtos = {
    "1": {"nome": "Arroz", "preco": 2.50},
    "2": {"nome": "Feijão", "preco": 3.00},
    "3": {"nome": "Carne", "preco": 10.00},
    "4": {"nome": "Frango", "preco": 8.00},
    "5": {"nome": "Pão", "preco": 1.50},
    "6": {"nome": "Leite", "preco": 2.00},
    "7": {"nome": "Ovos", "preco": 1.00},
    "8": {"nome": "Queijo", "preco": 5.00},
    "9": {"nome": "Tomate", "preco": 1.50},
    "10": {"nome": "Cebola", "preco": 0.50}
}

# Função para exibir produtos
def exibir_produtos():
    print("Produtos disponíveis:")
    for codigo, produto in produtos.items():
        print(f"{codigo} - {produto['nome']} - R${produto['preco']:.2f}")

# Função para realizar compra
def realizar_compra():
    carrinho = {}
    while True:
        exibir_produtos()
        codigo = input("Digite o código do produto que deseja comprar (ou 's' para sair): ")
        if codigo.lower() == 's':
            break
        elif codigo in produtos:
            quantidade = int(input("Digite a quantidade que deseja comprar: "))
            if codigo in carrinho:
                carrinho[codigo]["quantidade"] += quantidade
            else:
                carrinho[codigo] = {"nome": produtos[codigo]["nome"], "preco": produtos[codigo]["preco"], "quantidade": quantidade}
        else:
            print("Código inválido. Tente novamente.")


    # Exibir carrinho
        print("\nCarrinho:")
        total = 0
        with open("cupom_fiscal.txt", "w") as cupom:
            cupom.write("Cupom Fiscal\n")
            cupom.write("------------\n")
            for codigo, item in carrinho.items():
                subtotal = item["preco"] * item["quantidade"]
                total += subtotal
                print(f"{item['nome']} - {item['quantidade']} unidade(s) - R${subtotal:.2f}")
                cupom.write(f"{item['nome']} - {item['quantidade']} unidade(s) - R${subtotal:.2f}\n")
            print(f"Total: R${total:.2f}")
            cupom.write(f"Total: R${total:.2f}\n")

    realizar_compra()

realizar_compra()





# Explicação do Código



#Parte 1: Definição dos Produtos



# Dicionário com produtos e preços
#produtos = {
    #"1": {"nome": "Arroz", "preco": 2.50},
    #"2": {"nome": "Feijão", "preco": 3.00},
    #"3": {"nome": "Carne", "preco": 10.00},
    #"4": {"nome": "Frango", "preco": 8.00},
    #"5": {"nome": "Pão", "preco": 1.50},
    #"6": {"nome": "Leite", "preco": 2.00},
    #"7": {"nome": "Ovos", "preco": 1.00},
    #"8": {"nome": "Queijo", "preco": 5.00},
    #"9": {"nome": "Tomate", "preco": 1.50},
    #"10": {"nome": "Cebola", "preco": 0.50}
#}

#Parte 2: Função para Exibir Produtos


# Função para exibir produtos
#def exibir_produtos():
    #print("Produtos disponíveis:")
    #for codigo, produto in produtos.items():
        #print(f"{codigo} - {produto['nome']} - R${produto['preco']:.2f}")

#A função utiliza um loop for para iterar sobre o dicionário produtos e exibir cada produto.
    

#Parte 3: Função para Realizar Compra


# Função para realizar compra
#def realizar_compra():
    #carrinho = {}
    #while True:
        #exibir_produtos()
        #codigo = input("Digite o código do produto que deseja comprar (ou 's' para sair): ")
        #if codigo.lower() == 's':
           # break
      #  elif codigo in produtos:
    #        quantidade = int(input("Digite a quantidade que deseja comprar: "))
     #       if codigo in carrinho:
    #            carrinho[codigo]["quantidade"] += quantidade
        #    else:
      #          carrinho[codigo] = {"nome": produtos[codigo]["nome"], "preco": produtos[codigo]["preco"], "quantidade": quantidade}
     #   else:
      #      print("Código inválido. Tente novamente.")
#A função realizar_compra() é responsável por realizar a compra.
#A função cria um dicionário carrinho para armazenar os produtos escolhidos pelo usuário.
#A função utiliza um loop while para permitir que o usuário escolha produtos e quantidades.
#Se o usuário digitar 's', o programa sai do loop.
#Se o usuário escolher um produto válido, o programa verifica se o produto já está no carrinho. Se estiver, aumenta a quantidade. Se não estiver, adiciona o produto ao carrinho.
 # Exibir carrinho
   # print("\nCarrinho:")
   # total = 0
    #with open("cupom_fiscal.txt", "w") as cupom:
   #     cupom.write("Cupom Fiscal\n")
    #    cupom.write("------------\n")
     #   for codigo, item in carrinho.items():
      #      subtotal = item["preco"] * item["quantidade"]
       #     total += subtotal
       #     print(f"{item['nome']} - {item['quantidade']} unidade(s) - R${subtotal:.2f}")
       #     cupom.write(f"{item['nome']} - {item['quantidade']} unidade(s) - R${subtotal:.2f}\n")
        #print(f"Total: R${total:.2f}")
       # cupom.write(f"Total: R${total:.2f}\n")

#realizar_compra()

#Explicação do código:

#Adicionei um bloco with open para criar um arquivo cupom_fiscal.txt e escrever nele as informações da compra.
#Dentro do loop que exibe o carrinho, adicionei uma linha para escrever cada item do carrinho no arquivo cupom_fiscal.txt.
#Adicionei uma linha para escrever o total da compra no arquivo cupom_fiscal.txt.
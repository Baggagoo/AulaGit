class Inventario:
    def __init__(self):
        self.produtos = {}

    def adicionar_produto(self, nome, preco, quantidade):
        if nome in self.produtos:
            print("Produto já existe. Atualizando informações.")
            self.produtos[nome]['preco'] = preco
            self.produtos[nome]['quantidade'] += quantidade
        else:
            self.produtos[nome] = {'preco': preco, 'quantidade': quantidade}
        print(f"Produto {nome} adicionado/atualizado com sucesso!")

    def remover_produto(self, nome):
        if nome in self.produtos:
            del self.produtos[nome]
            print(f"Produto {nome} removido com sucesso!")
        else:
            print("Produto não encontrado.")

    def listar_produtos(self):
        if not self.produtos:
            print("Inventário está vazio.")
        else:
            for nome, info in self.produtos.items():
                print(f"Nome: {nome}, Preço: R${info['preco']}, Quantidade: {info['quantidade']}")

# Função principal para interação com o usuário
def menu():
    inventario = Inventario()
    while True:
        print("\nMenu de Opções:")
        print("1. Adicionar Produto")
        print("2. Remover Produto")
        print("3. Listar Produtos")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do Produto: ")
            preco = float(input("Preço do Produto: "))
            quantidade = int(input("Quantidade do Produto: "))
            inventario.adicionar_produto(nome, preco, quantidade)
        elif opcao == '2':
            nome = input("Nome do Produto a ser removido: ")
            inventario.remover_produto(nome)
        elif opcao == '3':
            inventario.listar_produtos()
        elif opcao == '4':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

# Executa o menu
menu()

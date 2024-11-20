import requests

# URL base da API de produtos
PRODUCTS_API_URL = 'http://localhost:5000/produtos/'

# Função para adicionar um produto
def adicionar_produto(nome, quantidade, preco):
    produto = {'nome': nome, 'quantidade': quantidade, 'preco': preco}
    response = requests.post(PRODUCTS_API_URL, json=produto)
    
    if response.status_code == 201:
        print('Produto adicionado com sucesso!')
    else:
        print('Erro ao adicionar produto.')

# Função para listar todos os produtos
def listar_produtos():
    response = requests.get(PRODUCTS_API_URL)
    
    if response.status_code == 200:
        produtos = response.json()
        for produto in produtos:
            print(f"Nome: {produto['nome']}, Quantidade: {produto['quantidade']}, Preço: {produto['preco']}")
    else:
        print('Erro ao listar produtos.')

# Função para buscar um produto pelo nome
def buscar_produto(nome):
    response = requests.get(f"{PRODUCTS_API_URL}{nome}")
    
    if response.status_code == 200:
        produto = response.json()
        print(f"Nome: {produto['nome']}, Quantidade: {produto['quantidade']}, Preço: {produto['preco']}")
    else:
        print('Produto não encontrado.')

if __name__ == "__main__":
    # Teste para adicionar um produto
    adicionar_produto("Camiseta", 20, 29.99)

    # Teste para listar todos os produtos
    print("\nProdutos em estoque:")
    listar_produtos()

    # Teste para buscar um produto
    print("\nBuscando produto:")
    buscar_produto("Camiseta")

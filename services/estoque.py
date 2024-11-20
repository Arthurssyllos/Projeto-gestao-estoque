import requests

# URL base da API de estoque
ESTOQUE_API_URL = 'http://localhost:5001/estoque/'

# Função para atualizar a quantidade de um produto
def atualizar_quantidade(nome, quantidade):
    response = requests.put(f"{ESTOQUE_API_URL}{nome}", json={'quantidade': quantidade})
    
    if response.status_code == 200:
        print('Quantidade atualizada com sucesso!')
    else:
        print('Erro ao atualizar quantidade.')

# Função para remover um produto do estoque
def remover_produto(nome):
    response = requests.delete(f"{ESTOQUE_API_URL}{nome}")
    
    if response.status_code == 200:
        print('Produto removido com sucesso!')
    else:
        print('Erro ao remover produto.')

if __name__ == "__main__":
    # Teste para atualizar a quantidade
    atualizar_quantidade("Camiseta", 50)

    # Teste para remover um produto
    remover_produto("Camiseta")

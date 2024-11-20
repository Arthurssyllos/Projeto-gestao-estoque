# Gerenciamento de Estoque (Microsserviços)

Este projeto implementa um sistema simples de gerenciamento de estoque utilizando a arquitetura de microsserviços. Ele está dividido em dois microsserviços principais:

1. **Gerenciamento de Produtos** (Cadastro e listagem de produtos)
2. **Gerenciamento de Estoque** (Atualização de quantidade e remoção de produtos)

A interface web (frontend) foi criada utilizando HTML, CSS e JavaScript para interagir com as APIs RESTful dos microsserviços.

## Funcionalidades

### Gerenciar Produtos
- **Adicionar Produto**: Adiciona um novo produto ao estoque, especificando nome, quantidade e preço.
- **Listar Produtos**: Exibe todos os produtos cadastrados no sistema.
- **Buscar Produto**: Permite buscar um produto pelo nome.

### Gerenciar Estoque
- **Atualizar Quantidade**: Atualiza a quantidade disponível de um produto específico.
- **Remover Produto**: Remove um produto do estoque pelo nome.

## Arquitetura

A aplicação é dividida em dois microsserviços:

- **Produtos (produtos.py)**: Gerencia as informações dos produtos, como nome, quantidade e preço.
- **Estoque (estoque.py)**: Responsável por gerenciar a quantidade de produtos no estoque.

A comunicação entre o front-end (HTML) e os microsserviços é feita via **requisições HTTP**.

## Tecnologias Utilizadas

- **Backend**:
  - Python (Flask)
  - SQLite (banco de dados local)
  
- **Frontend**:
  - HTML
  - CSS
  - JavaScript (Fetch API)

## Como Executar

### Pré-requisitos

1. Ter o Python 3.x instalado em sua máquina.
2. Instalar as dependências do projeto.

### Passo a Passo para Executar o Projeto

1. **Clonar o repositório**

   Primeiro, clone este repositório para sua máquina local:

   ```bash
   git clone https://github.com/seu-usuario/projeto-microsservicos.git
   cd projeto-microsservicos

2. **Instalar as dependências do backend**

    Crie um ambiente virtual (opcional) e instale as dependências necessárias:

    ```bash
    python -m venv venv
    source venv/bin/activate  # no Linux/macOS
    venv\Scripts\activate     # no Windows
    pip install -r requirements.txt

3. **Rodar o servidor Flask**

    Com as dependências instaladas, inicie o servidor para os microsserviços de Produtos e Estoque:

    Microsserviço de Produtos:

    ```bash
    python produtos.py

    Microsserviço de Estoque:

    python estoque.py

Após isso, os servidores estarão rodando nas portas 5000 (para produtos) e 5001 (para estoque), respectivamente.

4. **Abrir a interface web**

    A interface web está na pasta frontend/. Abra o arquivo index.html diretamente no seu navegador ou utilize um servidor web simples, como o Live Server do VSCode, para visualizá-lo. O frontend interage com as APIs nos servidores Flask.

    **Estrutura de Arquivos:**

        
        projeto-microsservicos/
        │
        ├── produtos.py          # Microsserviço para gerenciamento de produtos
        ├── estoque.py           # Microsserviço para gerenciamento de estoque
        ├── frontend/
        │   ├── index.html       # Interface web para interagir com a API
        │   └── style.css        # Estilos CSS para a interface web
        ├── requirements.txt     # Dependências do projeto (Flask)
        └── README.md            # Documentação do projeto


### Endpoints da API 

## Produtos

**GET /produtos: Retorna todos os produtos cadastrados.**
**GET /produtos/{nome}: Busca um produto pelo nome.**
**POST /produtos: Adiciona um novo produto ao estoque.**

**Corpo da requisição:**

        {
         "nome": "Camiseta",
         "quantidade": 10,
         "preco": 29.99
        }

**DELETE /produtos/{nome}: Remove um produto pelo nome.**

## Estoque

PUT /estoque/{nome}: Atualiza a quantidade de um produto.

Corpo da requisição:

        {
            "quantidade": 20
        }

## Como Usar a Interface Web

Adicionar Produto: Preencha o formulário na parte superior da página com o nome do produto, a quantidade e o preço, e clique no botão "Adicionar Produto".

Listar Produtos: Ao carregar a página, todos os produtos cadastrados são exibidos automaticamente na seção "Produtos em Estoque".

Buscar Produto: Clique no botão "Buscar Produto", insira o nome do produto e veja os detalhes do produto encontrado.

Atualizar Quantidade: Clique no botão "Atualizar Quantidade", insira o nome do produto e a nova quantidade para atualizar.

Remover Produto: Clique no botão "Remover Produto", insira o nome do produto que deseja excluir.

## Exemplos de Resposta da API

### GET /produtos:

[
  {
    "nome": "Camiseta",
    "quantidade": 10,
    "preco": 29.99
  },
  {
    "nome": "Calça",
    "quantidade": 5,
    "preco": 49.99
  }
]

### POST /produtos: Resposta de sucesso:

{
  "message": "Produto adicionado com sucesso!"
}

### PUT /estoque/{nome}: Resposta de sucesso:

{
  "message": "Quantidade atualizada com sucesso!"
}

### DELETE /produtos/{nome}: Resposta de sucesso:

{
  "message": "Produto removido com sucesso!"
}

## Contribuições

### Se você deseja contribuir para este projeto, sinta-se à vontade para abrir um pull request ou relatar problemas no repositório.

### Explicação das seções:

1. **Descrição do Projeto**: Explica o propósito do projeto e o que ele faz.
2. **Funcionalidades**: Lista as funcionalidades principais que a aplicação oferece.
3. **Arquitetura**: Explica a divisão da aplicação em microsserviços e sua comunicação.
4. **Tecnologias Utilizadas**: Descreve as tecnologias e ferramentas utilizadas.
5. **Passo a Passo para Executar o Projeto**: Passo a passo detalhado sobre como rodar o projeto, desde a clonagem até a execução do servidor.
6. **Estrutura de Arquivos**: Mostra a estrutura do repositório.
7. **Endpoints da API**: Descreve os endpoints principais da API, incluindo os métodos HTTP e exemplos de requisição e resposta.
8. **Como Usar a Interface Web**: Instruções para utilizar a interface web.
9. **Exemplos de Resposta da API**: Exemplos de respostas para cada tipo de requisição.
10. **Contribuições**: Instruções de como os usuários podem contribuir para o projeto.
11. **Licença**: Licença do projeto (exemplo: MIT).

Este arquivo `README.md` fornece uma visão geral completa de como o projeto funciona e como os desenvolvedores podem interagir com ele.

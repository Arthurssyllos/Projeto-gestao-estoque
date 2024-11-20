# produtos_api.py

from flask import Flask, jsonify, request
from flask_cors import CORS  # Importando o CORS

app = Flask(__name__)
CORS(app)  # Habilitando CORS para todas as rotas

produtos = []

@app.route('/produtos', methods=['GET'])
def listar_produtos():
    return jsonify(produtos), 200

@app.route('/produtos', methods=['POST'])
def adicionar_produto():
    produto = request.get_json()
    produtos.append(produto)
    return jsonify(produto), 201

@app.route('/produtos/<nome>', methods=['GET'])
def buscar_produto(nome):
    for produto in produtos:
        if produto['nome'].lower() == nome.lower():
            return jsonify(produto), 200
    return jsonify({"message": "Produto não encontrado!"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Porta 5000

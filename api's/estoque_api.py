# estoque_api.py

from flask import Flask, jsonify, request

app = Flask(__name__)

estoque = {}

@app.route('/estoque/<nome>', methods=['PUT'])
def atualizar_quantidade(nome):
    data = request.get_json()
    if nome in estoque:
        estoque[nome]['quantidade'] = data.get('quantidade')
        return jsonify(estoque[nome]), 200
    return jsonify({"message": "Produto não encontrado!"}), 404

@app.route('/estoque/<nome>', methods=['DELETE'])
def remover_produto(nome):
    if nome in estoque:
        del estoque[nome]
        return jsonify({"message": f"Produto {nome} removido com sucesso!"}), 200
    return jsonify({"message": "Produto não encontrado!"}), 404

if __name__ == '__main__':
    app.run(debug=False, port=5001)  # Porta 5001

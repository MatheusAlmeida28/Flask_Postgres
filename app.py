from flask import jsonify, request
from banco_de_dados import Carros,app,db

@app.route('/',methods=['GET'])
def home():
    return 'Welcome'


@app.route('/carros_no_registro',methods=['GET'])
def obter_pessoas_no_registro():
    carros = Carros.query.all()
    lista_de_carros = []
    for carro in carros:
         carro_atual = {}
         carro_atual['id'] = carro.id
         carro_atual['nome'] = carro.nome
         carro_atual['modelo'] = carro.modelo
         lista_de_carros.append(carro_atual)
    
    return jsonify({'Pessoas':lista_de_carros})


@app.route('/registo_de_carro',methods=['POST'])
def novo_autor():
    novo_carro = request.get_json()
    
    carro = Carros(id=novo_carro['id'],nome=novo_carro['nome'],
    modelo=novo_carro['modelo'])

    try:
       db.session.add(carro)
       db.session.commit()
    except:
        return 'Item já existente pelo id,por isso não foi adcionado',409

    return jsonify({'mensagem': 'Novas informações adicionadas com sucesso!'}, 200)


@app.route('/carro_no_registro/<int:id_carro>', methods=['PUT'])
def atualizar_carro(id_carro):
    carros_a_alterar = request.get_json()
    carro = Carros.query.filter_by(id=id_carro).first()
    
    if not carro:
        return jsonify({'Mensagem': 'Este carro não foi encontrado'}, 400)
    
    try:
      if carros_a_alterar['nome']:
         carro.nome = carros_a_alterar['nome']
    except:
        pass
    try:
        if carros_a_alterar['modelo']:
            carro.modelo = carros_a_alterar['modelo']
    except:
        pass
    
    db.session.commit()
    return jsonify({'Mensagem': 'Dado(s) foi(ram) alterado(s) com sucesso!'}, 200)

@app.route('/deletar_carro/<int:id_carro>', methods=['DELETE'])
def excluir_autor(id_carro):
    carro = Carros.query.filter_by(id=id_carro).first()

    if not carro:
        return jsonify({'mensagem': 'Registro do carro não encontrado'}, 400)

    db.session.delete(carro)
    db.session.commit()

    return jsonify({'mensagem': ' Registro do carro excluído com sucesso!'}, 200)

if __name__ == "__main__":
    app.run(port=5000, host='localhost', debug=True)
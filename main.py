# encoding: utf-8
from flask import Flask, jsonify, request
from consumirAPI import ConsumirAPI

example = Flask(__name__)

example.config['JSON_AS_ASCII'] = False

@example.errorhandler(404)
def page_not_found(e):
    return "Págna não encontrada!"

@example.route('/consultar/<cep>', methods=['GET'])
def consultarCEP(cep):
    try:
        cep = ConsumirAPI().consultarCEP(cep)

        if not cep:
            raise Exception("CEP não encontrado")
    except Exception as ex:
        return jsonify({'success': False, 'message': ex.args}), 400
    else:
        return jsonify(cep), 200


if __name__ == "__main__":
    example.run(debug=True)
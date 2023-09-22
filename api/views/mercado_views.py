from api import api
from flask_restful import Resource
from ..schema import mercado_schema
from flask import request, make_response, jsonify
from ..entidades import mercado
from ..services import mercado_service

class Mercado(Resource):
    def get(self):
        mercadoria = mercado_service.listagem_mercadoria()
        mc = mercado_schema.MercadoSchema(many=True)
        return make_response(mc.jsonify(mercadoria), 200)
    def post(self):
        #Validação dos dados
        mc = mercado_schema.MercadoSchema()
        validate = mc.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json['nome']
            preco = request.json['preco']

        #Indo ao método construtor
        nova_mercadoria = mercado.Mercado(nome=nome, preco=preco)
        # Cadastrando
        resultado = mercado_service.cadastro_mercado(nova_mercadoria)
        x = mc.jsonify(resultado)
        return make_response(x, 201)
class MercadoDetalhes(Resource):
    def get(self, id):
        mercadoria = mercado_service.listagem_mercadoria_id(id)
        if mercadoria is None:
            return make_response(jsonify("Mercadoria não encontrada"), 404)
        ms = mercado_schema.MercadoSchema()
        return make_response(ms.jsonify(mercadoria), 200)

    def delete(self, id):
        mercadoria = mercado_service.listagem_mercadoria_id(id)
        if mercadoria is None:
            return make_response(jsonify("Mercadoria não encontrada"), 404)
        mercado_service.deletar_mercadoria(mercadoria)
        return make_response("Mercadoria excluída com sucesso", 204)

    def put(self, id):
        mercadoria = mercado_service.listagem_mercadoria_id(id)
        if mercadoria is None:
            return make_response(jsonify("Mercado não encontrado"), 404)
        mc = mercado_schema.MercadoSchema()
        validate = mc.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json['nome']
            preco = request.json['preco']

            nova_mercadoria = mercado.Mercado(nome=nome, preco=preco)
            mercado_service.atualizar_mercadoria(mercadoria, nova_mercadoria)
            mercadoria_atualizada = mercado_service.listagem_mercadoria_id(id)
            return make_response(mc.jsonify(mercadoria_atualizada), 200)


api.add_resource(Mercado, '/mercad')
api.add_resource(MercadoDetalhes, '/mercado/<int:id>')
from..models import mercado_models
from api import db

def cadastro_mercado(produto):
    produto_bd = mercado_models.Mercado(nome=produto.nome,
                                        preco=produto.preco)
    db.session.add(produto_bd)
    db.session.commit()
    return produto_bd

def listagem_mercadoria():
    mercadoria = mercado_models.Mercado.query.all()
    return mercadoria

def listagem_mercadoria_id(id):
    mercadoria = mercado_models.Mercado.query.filter_by(id=id).first()
    return mercadoria
def deletar_mercadoria(id):
    db.session.delete(id)
    db.session.commit()

def atualizar_mercadoria(mercadoria_antiga, mercadoria_nova):
    mercadoria_antiga.nome = mercadoria_nova.nome
    mercadoria_antiga.preco = mercadoria_nova.preco
    db.session.commit()

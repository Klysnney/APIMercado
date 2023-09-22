from api import ma
from..models import mercado_models
from marshmallow import fields

class MercadoSchema(ma.SQLAlchemySchema):
    class Meta:
        model = mercado_models.Mercado
        load_instance = True
        fields = ('id', 'nome', 'preco')

    nome = fields.String(required=True)
    preco = fields.Float(required=True)

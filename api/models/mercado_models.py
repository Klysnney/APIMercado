from api import db

class Mercado(db.Model):
    __tablename__ = "mercado"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = db.Column(db.String(20), nullable=False)
    preco = db.Column(db.Float, nullable=False)

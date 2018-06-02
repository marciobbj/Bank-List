from lister.extensions import db
from lister import app

class Agencias(db.Model):
    __tablename__ = "bancos"

    id = db.Column(db.Integer, primary_key = True)
    cnpj = db.Column(db.String)
    nomeinstituicao = db.Column(db.String)
    segmento = db.Column(db.String)
    nomeinstalacao = db.Column(db.String)
    endereco = db.Column(db.String)
    numero = db.Column(db.String)
    complemento = db.Column(db.String)
    bairro = db.Column(db.String)
    cep = db.Column(db.String)
    municipio = db.Column(db.String)
    uf = db.Column(db.String)
    ddd = db.Column(db.String)
    fone = db.Column(db.String)

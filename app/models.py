from app import db

class Mercadoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=True)
    preco = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Mercadoria('{self.nome}', '{self.descricao}', '{self.preco}')"

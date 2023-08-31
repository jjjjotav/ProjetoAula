from app import db

class TblCadastro(db.aModel):
    id = db.column(db.Integer, primary_key=True)
    nome = db.column(db.String(128), nullable=False)
    email = db.column(db.String(128), nullable=False)
    senha = db.column(db.String(128), nullable=False)

    def __repr__(self):
        return 'Criando o cadastro de usuário'
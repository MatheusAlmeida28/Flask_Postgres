from flask_sqlalchemy import SQLAlchemy
from flask import Flask 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:matheus123@localhost/test" #matheus123(é a senha do programa que você configurou,então vai de acordo com cada pessoa)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db:SQLAlchemy

class Carros(db.Model):
    __tablename__ = 'carros'

    id = db.Column(db.Integer,primary_key=True)
    nome = db.Column(db.String())
    modelo = db.Column(db.String())
       

#Essas configurações abaixo são para quando o banco de dados é criado pela primeira vez,uma vez usada,você pode comentar ou apagar

#db.drop_all()  
#db.create_all()
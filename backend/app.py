from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *
from flask_marshmallow import Marshmallow
from flask_cors import CORS



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://fmls03:Schipilliti03@localhost/ShoppingCart'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_object(__name__)

db = SQLAlchemy(app)
ma = Marshmallow(app)

CORS(app, resources={r'/*': {'origins': '*'}})


class Prodotto(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.VARCHAR(255))
    comprato = db.Column(db.VARCHAR(5))


class ProdottoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Prodotto
        load_istance = True

@app.route('/', methods=['GET'])
def getData():
    query = Prodotto.query.all()
    prodottiSchema = ProdottoSchema(many = True)
    prodotti = prodottiSchema.dump(query)
    return jsonify(prodotti)



if __name__ == '__main__':
    app.run()
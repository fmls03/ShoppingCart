from flask import Flask, jsonify, request
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

CORS(app, resources={r"/api/*": {"origins": "*", "allow_headers": "*", "expose_headers": "*"}})
PRODUCTS = []

class Product(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.VARCHAR(255))
    bought = db.Column(db.Boolean)


class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        load_istance = True


@app.route('/api/product/<productID>', methods=['PUT', 'DELETE'])
def product(productID):
    if request.method == 'PUT':
        product = Product.query.filter_by(id=productID).first()
        product.bought = not product.bought
        db.session.merge(product)
        db.session.commit()
        db.session.refresh(product)
        return product


@app.route('/', methods=['GET'])
def getData():
    query = Product.query.all()
    productsSchema = ProductSchema(many = True)
    products = productsSchema.dump(query)
    return jsonify(products)



if __name__ == '__main__':
    app.run()
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *
from flask_marshmallow import Marshmallow
from flask_cors import CORS, cross_origin



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://fmls03:Schipilliti03@localhost/ShoppingCart'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_object(__name__)

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Product(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.VARCHAR(255), nullable=False)
    bought = db.Column(db.Boolean, nullable=False)

    def __init__(self, name, bought):
        self.name = name
        self.bought = bought

class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        load_istance = True


@app.route('/api/product/bought/<productID>', methods=['PUT'])
def buyProduct(productID):
    if request.method == 'PUT':
        product = Product.query.filter_by(id=productID).first()
        payload = request.get_json()
        product.bought = not payload.get('bought')
        db.session.merge(product)
        db.session.commit()
        db.session.refresh(product)
        productsSchema = ProductSchema()
        products_json = productsSchema.dump(product)        
        return jsonify(products_json)

@app.route('/api/product/add', methods=['PUT'])
def addProduct():
    if request.method == 'PUT':
        payload = request.get_json()
        print(payload.get('name'))
        name = payload.get('name')
        newProduct = Product(name, False)
        db.session.add(newProduct)
        db.session.commit()
        db.session.refresh(newProduct)
        productSchema = ProductSchema()
        product_json = productSchema.dump(newProduct)
        return jsonify(product_json)


@app.route('/api/product/delete/<productID>', methods=['DELETE'])
def deleteProduct(productID):
    if request.method == 'DELETE':
        Product.query.filter_by(id = productID).delete()
        db.session.commit()
        return jsonify('deleted')
            

@app.route('/api/', methods=['GET'])
def getData():
    query = Product.query.all()
    productsSchema = ProductSchema(many = True)
    products = productsSchema.dump(query)
    return jsonify(products)



if __name__ == '__main__':
    app.run()
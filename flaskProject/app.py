from flask import Flask, request
from flask_restx import Api, Resource, fields
from flask_cors import (CORS)

from models import db, Drink

app = Flask(__name__)
CORS(app)

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///drinks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Iniciando o Banco
db.init_app(app)

# Iniciando o Flask RESTX + Swagger
api = Api(app, doc='/swagger', title='API de Drinks', description='CRUD de Drinks com Flask-RESTX')

# Modelo Swagger
drink_model = api.model('Drink', {
    'id': fields.Integer(readonly=True, description='ID do drink'),
    'name': fields.String(required=True, description='Nome do drink'),
    'ingredients': fields.String(required=False, description='Ingredientes do drink'),
    'price': fields.Float(required=False, description='Preço do drink'),
})

# Rota para listar e criar drinks
@api.route('/drinks')
class DrinkList(Resource):
    @api.doc('list_drinks')
    @api.marshal_list_with(drink_model)
    def get(self):
        """Lista todos os drinks"""
        drinks = Drink.query.all()
        return drinks

    @api.doc('create_drink')
    @api.expect(drink_model, validate=True)
    @api.marshal_with(drink_model, code=201)
    def post(self):
        """Cria um novo drink"""
        data = request.get_json()
        new_drink = Drink(
            name=data['name'],
            ingredients=data.get('ingredients'),
            price=data.get('price')
        )
        db.session.add(new_drink)
        db.session.commit()
        return new_drink, 201

# Rota para um drink específico
@api.route('/drinks/<int:id>')
@api.response(404, 'Drink não encontrado')
@api.param('id', 'ID do drink')
class DrinkResource(Resource):
    @api.doc('get_drink')
    @api.marshal_with(drink_model)
    def get(self, id):
        """Obtém os detalhes de um drink específico"""
        drink = Drink.query.get(id)
        if not drink:
            api.abort(404, "Drink não encontrado")
        return drink

    @api.doc('update_drink')
    @api.expect(drink_model)
    def put(self, id):
        """Atualiza os dados de um drink específico"""
        drink = Drink.query.get(id)
        if not drink:
            api.abort(404, "Drink não encontrado")

        data = request.get_json()
        drink.name = data.get('name', drink.name)
        drink.ingredients = data.get('ingredients', drink.ingredients)
        drink.price = data.get('price', drink.price)
        db.session.commit()

        return {'message': 'Drink atualizado', 'drink': {
            'id': drink.id,
            'name': drink.name,
            'ingredients': drink.ingredients,
            'price': drink.price
        }}

    @api.doc('delete_drink')
    def delete(self, id):
        """Deleta um drink específico"""
        drink = Drink.query.get(id)
        if not drink:
            api.abort(404, "Drink não encontrado")

        db.session.delete(drink)
        db.session.commit()
        return {'message': 'Drink apagado'}

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    ingredients = db.Column(db.String(255), nullable=True)
    price = db.Column(db.Float, nullable=True)

    def __repr__(self):
        return f'<Drink {self.name}>'

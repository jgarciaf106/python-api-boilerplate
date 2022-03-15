from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
        
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.Integer, unique=True, nullable=False)
    name = db.Column(db.String(120), unique=False, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "username": self.username,
            "name": self.name,
            "is_active": self.is_active,
            # do not serialize the password, its a security breach
        }
        
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cat_code = db.Column(db.Integer, unique=True, nullable=False)
    description = db.Column(db.String(250), unique=False, nullable=False)

    def __repr__(self):
        return '<Category %r>' % self.cat_code

    def serialize(self):
        return {
            "cat_code": self.cat_code,
            "description": self.description,
        }

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    prod_id = db.Column(db.Integer, unique=True, nullable=False)
    cat_code = db.Column(db.Integer, db.ForeignKey('category.cat_code'), unique=False, nullable=False)
    description = db.Column(db.String(250), unique=False, nullable=False)

    def __repr__(self):
        return '<Product %r>' % self.prod_id

    def serialize(self):
        return {
            "prod_id": self.prod_id,
            "prod_id": self.cat_code,
            "description": self.description,
            # do not serialize the password, its a security breach
        }
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
        
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(120), unique=False, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "username": self.user_name,
            "name": self.name,
            # do not serialize the password, its a security breach
        }
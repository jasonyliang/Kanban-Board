from kanban import db
from datetime import datetime
from flask_login import UserMixin


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    do = db.Column(db.Boolean, default=False)
    done = db.Column(db.Boolean, default=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    deadline = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    def __repr__(self):
        return f"Todo('{self.title}', '{self.description}')"

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    todo = db.relationship('Todo', backref="creator", lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

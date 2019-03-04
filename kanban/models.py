from kanban import db
from datetime import datetime


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    do = db.Column(db.Boolean)
    done = db.Column(db.Boolean)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    deadline = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"Todo('{self.title}', '{self.description}')"
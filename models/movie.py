from server import db


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), nullable=False)
    year = db.Column(db.DateTime, nullable=True)

    def __init__(self, title, year):
        self.title = title
        self.year = year

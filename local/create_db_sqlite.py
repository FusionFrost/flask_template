import datetime

from server import app, db

from models.movie import Movie

# Create SQLite database
with app.app_context():
    db.create_all()
    db.session.add(Movie("Slaughterhouse-Five", datetime.datetime.now() ))
    db.session.add(Movie("Slaughterhouse-Next", datetime.datetime.now()))
    db.session.commit()

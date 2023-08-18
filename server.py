import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from views.movies import movies
from views.auth import auth

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# Add configuration
app.config.from_object("settings")

# Add blueprints
app.register_blueprint(movies)
app.register_blueprint(auth)

### SQLite
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'local/database.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

### PostgreSQL
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:root@0.0.0.0:5432/postgres'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db.init_app(app)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

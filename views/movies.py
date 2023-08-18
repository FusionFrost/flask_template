from datetime import datetime
from flask import Blueprint, render_template, abort, redirect, url_for, request

# Defining a blueprint
movies = Blueprint('movies', __name__)

@movies.route('/')
def home_page():
    today = datetime.today()
    day_name = today.strftime("%A")
    return render_template("home.html", day=day_name)


@movies.route('/movies', methods=['GET', 'POST'])
def movies_page():
    from models.movie import Movie, db

    if request.method == "GET":
        movies = Movie.query.all()
        if movies is None:
            abort(404)
        return render_template("movies.html", movies=movies)
    else:
        form_movie_keys = request.form.getlist("movie_keys")
        for form_movie_key in form_movie_keys:
            movie_id = Movie.query.get(form_movie_key)
            db.session.delete(movie_id)
            db.session.commit()
        return redirect(url_for("movies_page"))

@movies.route('/movie/<int:movie_key>', methods=['GET', 'POST'])
def movie_page(movie_key):
    from models.movie import Movie

    movie = Movie.query.get(movie_key)
    if movie is None:
        abort(404)
    return render_template("movie.html", movie=movie)

@movies.route('/movie/add', methods=['GET', 'POST'])
def movie_add_page():
    from models.movie import Movie, db

    if request.method == "GET":
        return render_template(
            "movie_edit.html", min_year=1887, max_year=datetime.now().year)
    else:
        form_title = request.form["title"]
        form_year = request.form["year"]
        movie = db.session.add(Movie(form_title if form_title else "Nothing", datetime.datetime.now()))
        db.session.commit()
        return redirect(url_for("movie_page", movie_key=movie.key))
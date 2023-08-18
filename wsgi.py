from server import app

app.run(debug=True)
# Для локального запуска через wsgi
#uwsgi --socket 0.0.0.0:5000 --protocol=http -w wsgi:app
#uwsgi --ini app.ini
if __name__ == '__main__':
    app.run(debug=True)

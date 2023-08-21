# Application structure

```
.
└── flask_template
    ├── local
    │   └── create_db_sqlite.py
    ├── models
    │   └── movie.py
    ├── nginx
    │   ├── Dockerfile
    │   └── nginx.conf
    ├── static
    │   └── mymovies.css
    ├── templates
    │   ├── layout.html
    │   ├── index.html
    │   └── home.html
    ├── views
    │   ├── __init__.py
    │   ├── auth.py
    │   └── movies.py
    ├── .gitignore
    ├── app.ini
    ├── Docker-compose.yml
    ├── Dockerfile
    ├── makefile
    ├── Procfile
    ├── readme.md
    ├── requirements.txt
    ├── server.py
    ├── settings.py
    └── wsgi.py
```
# Flask + Gunicorn

## Create Heroku app
flask-template-app
```
# Настройка конфигурационного файла
# В файле Procfile вписать
web: gunicorn wsgi:app port:8080
 
wsgi - это файл, app - приложение

# Авторизация 
heroku login
heroku git:remote -a flask-template-movie
```

## Deploy in Heroku
```
git add .  
git commit -am "fix"  
git push heroku master

# Для чтения логов
heroku logs --tail 

```


# Flask + WSGI + Nginx 
Docker-compose with 2 containers
(Flask app + WSGI) and Nginx server 

```
docker-compose -f Docker-compose.yml -p flask_template up -d --build
```
# Application struct

```
.
└── flask_app
    ├── app
    │   ├── extensions.py
    │   ├── __init__.py
    │   ├── main
    │   │   ├── __init__.py
    │   │   └── routes.py
    │   ├── models
    │   │   ├── post.py
    │   │   └── question.py
    │   ├── posts
    │   │   ├── __init__.py
    │   │   └── routes.py
    │   ├── questions
    │   │   ├── __init__.py
    │   │   └── routes.py
    │   └── templates
    │       ├── base.html
    │       ├── index.html
    │       ├── posts
    │       │   ├── categories.html
    │       │   └── index.html
    │       └── questions
    │           └── index.html
    ├── app.db
    └── config.py
```



# Flask + WSGI + Nginx 
Docker-compose with 2 containers
(Flask app + WSGI) and Nginx server 


## Deploy in Heroku as a container
flask-template-app
```
heroku login
docker login --username=<username> --password=<password>
heroku container:login
sudo heroku container:push web --app flask-template-app
sudo heroku container:release web ca--app flask-template-app
```

## Deploy in Heroku with git


# Flask + gunicorn
App also can run only with Flask+gunicorn. 
Need only add to file **procfile** this: `web: gunicorn app:wsgi`

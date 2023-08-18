from flask import Blueprint


# Defining a blueprint
auth = Blueprint('auth', __name__)

@auth.route('/admin')   # Focus here
def admin_home():
    return "Hello Admin!"
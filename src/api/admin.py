  
import os
from flask import Flask, Response
from flask_admin import Admin
from flask_basicauth import BasicAuth
from .models import db, User
from flask_admin.contrib.sqla import ModelView
from werkzeug.exceptions import HTTPException


def setup_admin(app):
    basic_auth = BasicAuth(app)
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

    class AuthException(HTTPException):
        def __init__(self, message):
            # python 2
            super(AuthException, self).__init__(message, Response(
                message, 401,
                {'WWW-Authenticate': 'Basic realm="Login Required"'}
            ))

    class MyModelView(ModelView):
        def is_accessible(self):
            if not basic_auth.authenticate():
                raise AuthException('Not authenticated. Refresh the page.')
            else:
                return True

        def inaccessible_callback(self, name, **kwargs):
            return redirect(basic_auth.challenge())

    # Add your models here, for example this is how we add a the User model to the admin
    admin = Admin(app, name='Admin Name', template_mode='bootstrap3')
    admin.add_view(MyModelView(User, db.session))

    # You can duplicate that line to add mew models
    # admin.add_view(ModelView(YourModelName, db.session))
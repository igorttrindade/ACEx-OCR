import os
from flask import Flask
from routes.login import auth
from routes.upload import upload_route
from routes.registros import register
from routes.ultimasConsultas import ultimasConsultas
from routes.user_list import user_list
from routes.empresa import empresa

app = Flask(__name__, static_folder='static')

app.secret_key = os.urandom(24)

UPLOAD_FOLDER = 'static/uploadFIles'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.register_blueprint(auth)
app.register_blueprint(upload_route, url_prefix="/upload")
app.register_blueprint(register, url_prefix="/registro")
app.register_blueprint(user_list, url_prefix="/usuarios")
app.register_blueprint(empresa, url_prefix="/empresa")

if __name__ == '__main__':
    app.run(debug=True)
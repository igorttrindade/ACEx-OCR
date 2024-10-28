import os
from flask import Flask
from flask_login import LoginManager
from routes.login import auth,User
from routes.ponto import ponto
from routes.funcionario import func
from routes.user_list import user_list
from routes.empresa import empresa

app = Flask(__name__, static_folder='static')
app.secret_key = os.urandom(24)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth.login" 

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)


UPLOAD_FOLDER = 'static/uploadFIles'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.register_blueprint(auth)
app.register_blueprint(ponto, url_prefix="/ponto")
app.register_blueprint(func, url_prefix="/funcionario")
app.register_blueprint(user_list, url_prefix="/usuarios")
app.register_blueprint(empresa, url_prefix="/empresa")

if __name__ == '__main__':
    app.run(debug=True)
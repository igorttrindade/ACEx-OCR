from flask import Flask
from routes.home import home_route
from routes.upload import upload_route
from routes.registros import register
from routes.ultimasConsultas import ultimasConsultas

app = Flask(__name__, static_folder='static')

UPLOAD_FOLDER = 'static/uploadFIles'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.register_blueprint(home_route)
app.register_blueprint(upload_route, url_prefix="/upload")
app.register_blueprint(register, url_prefix="/registro")
app.register_blueprint(ultimasConsultas, url_prefix="/ultimasConsultas")

if __name__ == '__main__':
    app.run(debug=True)
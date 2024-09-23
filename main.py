from flask import Flask
from routes.home import home_route
from routes.upload import upload_route

app = Flask(__name__, static_folder='static')

UPLOAD_FOLDER = 'static/uploadFIles'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.register_blueprint(home_route)
app.register_blueprint(upload_route, url_prefix="/upload")

if __name__ == '__main__':
    app.run(debug=True)
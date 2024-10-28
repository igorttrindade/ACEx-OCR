from flask import Flask,Blueprint,render_template
from flask_login import LoginManager, login_required
from database.database import supabase

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)

ponto = Blueprint('ponto', __name__)

@ponto.route('/', methods=['POST','GET'])
def batida_de_ponto():
    
    return render_template('batida-ponto.html')

if __name__ == '__main__':
    app.run(debug=True)

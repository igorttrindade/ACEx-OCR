from flask import Flask,Blueprint,render_template,jsonify,request,session
from flask_login import LoginManager, login_required,current_user
from controller.pontoInsert import armazenarBatidaPonto

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)

ponto = Blueprint('ponto', __name__)

@ponto.route('/', methods=['POST','GET'])
@login_required
def batida_de_ponto():
    if request.method == 'POST':
        data = request.get_json()
        id_funcionario = data.get('id_funcionario')
        horario = data.get('horario')
        if id_funcionario:
            result = armazenarBatidaPonto(id_funcionario,horario)
        if result:
            return jsonify({"message": "Batida de ponto registrada com sucesso!"}), 200
        else:
            return jsonify({"message": "Erro ao registrar batida de ponto."}), 500
    return render_template('batida-ponto.html')

if __name__ == '__main__':
    app.run(debug=True)

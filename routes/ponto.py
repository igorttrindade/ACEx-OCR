from flask import Flask,Blueprint,render_template,jsonify,request,session
from flask_login import LoginManager, login_required,current_user
from controller.pontoInsert import armazenarBatidaPonto
from database.database import supabase
from datetime import datetime

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)

ponto = Blueprint('ponto', __name__)

@ponto.route('/', methods=['POST','GET'])
@login_required
def batida_de_ponto():
    if request.method == 'POST':
        data = request.get_json()
        id_funcionario = data.get('id_funcionario', current_user.id)  # ID do usuário logado
        horario = data.get('horario')

        if id_funcionario:
            result = armazenarBatidaPonto(id_funcionario, horario)
            if result:
                return jsonify({"message": "Batida de ponto registrada com sucesso!"}), 200
            else:
                return jsonify({"message": "Erro ao registrar batida de ponto."}), 500

    id_funcionario = current_user.id
    horario_atual = datetime.now()
    dia_ponto = horario_atual.day
    mes_ponto = horario_atual.month
    ano_ponto = horario_atual.year

    try:
        response = (
            supabase.table("tb_ponto")
            .select("*")
            .eq("id_funcionario", id_funcionario)
            .eq("dia_ponto", dia_ponto)
            .eq("mes_ponto", mes_ponto)
            .eq("ano_ponto", ano_ponto)
            .execute()
        )

        pontos = response.data if response.data else []
        return render_template('batida-ponto.html', pontos=pontos)

    except Exception as e:
        print(f"Erro ao buscar pontos do dia: {e}")
        return render_template('batida-ponto.html', pontos=[])

if __name__ == '__main__':
    app.run(debug=True)

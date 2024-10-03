from flask import Blueprint,render_template

ultimasConsultas = Blueprint('ultimas_consultas', __name__)

@ultimasConsultas.route('/')
def lastConsults():
    """GET registros do arquivo"""
    return render_template('ultimasConsultas.html')

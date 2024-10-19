from flask import Blueprint,render_template

func = Blueprint('funcionario', __name__)

@func.route('/')
def page_func():
    """GET registros do arquivo"""
    return render_template('funcionarios.html')

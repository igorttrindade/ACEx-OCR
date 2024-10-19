from flask import Blueprint,render_template

empresa = Blueprint('empresa', __name__)

@empresa.route('/')
def company():
    """GET registros do arquivo"""
    return render_template('empresa.html')

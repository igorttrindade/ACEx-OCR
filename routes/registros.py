from flask import Blueprint,render_template

register = Blueprint('registros', __name__)

@register.route('/')
def register_file():
    """GET registros do arquivo"""
    return render_template('registro.html')

from flask import Blueprint, request, jsonify, redirect, url_for, session, render_template
from flask_login import UserMixin, login_user, logout_user
from database.database import supabase

auth = Blueprint('auth', __name__)

class User(UserMixin):
    def __init__(self, id):
        self.id = id

@auth.route('/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        try:
            response = supabase.table('tb_usuario').select('*').eq('id_usuario', username).single().execute()

            if response.data and response.data['senha_usuario'] == password:
                user = User(id=username)
                login_user(user)
                id_funcionario = response.data['id_usuario']
                session['id_funcionario'] = id_funcionario
                return jsonify({'success': True, 'id_funcionario':id_funcionario}), 200
            else:
                return jsonify({'success': False, 'message': 'Credenciais inválidas'}), 401

        except Exception as e:
            print(f"Erro ao fazer login: {e}")
            return jsonify({'success': False, 'message': 'Erro no servidor'}), 500
    
    return render_template('index.html')

@auth.route('/logout')
def logout():
    logout_user
    return redirect(url_for('auth.login'))

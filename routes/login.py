from flask import Blueprint, request, jsonify, redirect, url_for,session, render_template
from database.database import supabase

auth = Blueprint('auth', __name__)

@auth.route('/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        try:
            response = supabase.table('tb_usuario').select('*').eq('id_usuario', username).single().execute()

            if response.data and response.data['senha_usuario'] == password:
                session['logged_in'] = True
                session['username'] = username
                return jsonify({'success': True}), 200
            else:
                return jsonify({'success': False, 'message': 'Credenciais inválidas'}), 401

        except Exception as e:
            print(f"Erro ao fazer login: {e}")
            return jsonify({'success': False, 'message': 'Erro no servidor'}), 500
    
    return render_template('login.html')

@auth.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))

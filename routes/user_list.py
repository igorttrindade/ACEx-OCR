from flask import Blueprint,render_template, request, jsonify
from controller.userCreate import criar_usuario
from database.database import supabase
from datetime import date

user_list = Blueprint('userlist', __name__)

@user_list.route('/', methods=['POST', 'GET'])
def registerUser():
    """GET registros do arquivo e lista de usuários"""
    try:
        response = supabase.table("tb_usuario").select("*").execute()
        users = response.data if response.data else [] 
    except Exception as e:
        print(f"Erro ao listar usuários: {e}")
        users = []

    return render_template('user_list.html', users=users)

@user_list.route('/criar-usuario', methods=['POST'])
def criar_usuario_api():
    data = request.json
    if not data:
        return jsonify({"error": "Dados inválidos"}), 400
    id_usuario = data.get('name')
    email = data.get('email')
    data_criacao = date.today()
    data_criacao_str = data_criacao.strftime("%d/%m/%Y")

    response = criar_usuario(email,id_usuario,data_criacao_str)

    if response:
        return jsonify({"message": "Usuário criado com sucesso!"}), 201
    else:
        return jsonify({"error": "Erro ao criar usuario"}), 500

@user_list.route('/excluir/<int:user_id>', methods=['DELETE'])
def excluir_usuario(user_id):
    try:
        response = (
            supabase.table("tb_usuario")
            .delete()
            .eq('id_usuario', user_id)
            .execute()
        )
        
        if response.data:
            return jsonify({"message": "Usuário excluído com sucesso!"}), 200
        else:
             return jsonify({"error": "Erro ao excluir usuário.", "details": response.error}), 500
    except Exception as e:
        return jsonify({"error": f"Erro ao excluir usuário: {str(e)}"}), 500

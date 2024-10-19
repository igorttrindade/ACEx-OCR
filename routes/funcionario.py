from flask import Blueprint,render_template,request, jsonify
from database.database import supabase
from controller.funcionarioCreate import criar_funcionario, buscar_empresas

func = Blueprint('funcionario', __name__)

@func.route('/')
def page_func():
    """GET registros do arquivo"""
    return render_template('funcionarios.html')

@func.route('/cadastro-funcionarios', methods=['GET','POST'])
def cadastro_func():
    if request.method == 'POST':
        data = request.get_json()
        if not data:
            return jsonify({"error": "Dados inválidos"}), 400
        matricula_func = data.get('matricula_func')
        nome_func = data.get('nome_func')
        cargo_func = data.get('cargo_func')
        salario_func = data.get('salario_func')
        inicio_func = data.get('inicio_func')
        compet_func = data.get('compet_func')
        empresa_func = data.get('empresa_func')
        nasc_func = data.get('dtnasc_func')
        sexo_func = data.get('sexo_func')
        status_func = data.get('status_func')

        response = criar_funcionario(matricula_func, nome_func,cargo_func,salario_func,inicio_func,compet_func,empresa_func,nasc_func,sexo_func,status_func)

        if response:
            return jsonify({"message": "Usuário criado com sucesso!"}), 201
        else:
            return jsonify({"error": "Erro ao criar usuario"}), 500
    empresas = buscar_empresas()
    return render_template('cadastroFuncionarios.html', empresas = empresas)

@func.route('/listar-funcionarios')
def listar_func():
    """GET registros do arquivo e lista de usuários"""
    try:
        response = supabase.table("tb_funcionarios").select("*").execute()
        func = response.data if response.data else [] 
    except Exception as e:
        print(f"Erro ao listar usuários: {e}")
        func = []

    return render_template('listarFuncionarios.html', func=func)

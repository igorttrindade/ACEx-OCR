from flask import Blueprint,render_template,request, jsonify
from database.database import supabase
from controller.funcionarioCreate import criar_funcionario, buscar_empresas, armazenarFolhaPonto

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

@func.route('/listar-funcionarios/folha-ponto', methods=['GET', 'POST'])
def folha_func():
    if request.method == 'POST':
        data = request.get_json()
        if not data or not isinstance(data, list):
            return jsonify({"error": "Dados inválidos"}), 400

        success_responses = []
        error_responses = []

        for registro in data:
            matricula_func = registro.get('matricula_func')
            id_linha = registro.get('id_linha')
            entrada_func = registro.get('entrada_funcionario')
            inicio_intervalo = registro.get('inicio_intervalo')
            termino_intervalo = registro.get('termino_intervalo')
            hr_trab = registro.get('hora_trabalhada')
            dia_ponto = registro.get('dia_ponto')
            mes_ponto = registro.get('mes_ponto')
            ano_ponto = registro.get('ano_ponto')
            arquivo_ponto = registro.get('arquivo_ponto')
            periodo_inicio = registro.get('periodo_inicio')
            periodo_fim = registro.get('periodo_fim')

            response = armazenarFolhaPonto(matricula_func, id_linha, entrada_func, inicio_intervalo, termino_intervalo, hr_trab, dia_ponto, mes_ponto, ano_ponto, arquivo_ponto, periodo_inicio, periodo_fim)

            if response:
                success_responses.append({"id_linha": id_linha})
            else:
                error_responses.append({"matricula_func": matricula_func, "error": "Erro ao criar usuário"})

        if error_responses:
            return jsonify({"error": "Erro ao processar alguns registros", "details": error_responses}), 500

        return jsonify({"message": "Registros criados com sucesso!", "success": success_responses}), 201

    return render_template('folhaFuncionarios.html')


@func.route('/listar-funcionarios/ultima-linha', methods=['GET'])
def obter_ultima_linha():
    try:
        response = supabase.table("tb_ponto").select("id_linha").order("id_linha", desc=True).limit(1).execute()
        if response.data:
            ultimo_id_linha = response.data[0]["id_linha"]
            return jsonify({"ultimo_id_linha": ultimo_id_linha}), 200
        else:
            return jsonify({"ultimo_id_linha": 0}), 200
    except Exception as e:
        print(f"Erro ao obter a última linha: {e}")
        return jsonify({"error": "Erro ao obter a última linha"}), 500

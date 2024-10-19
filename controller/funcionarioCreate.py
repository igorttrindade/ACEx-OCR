from database.database import supabase

def criar_funcionario(matricula_func, nome_func,cargo_func,salario_func,inicio_func,compet_func,empresa_func,nasc_func,sexo_func,status_func):
    try:
        response = (
            supabase.table("tb_func")
            .insert({"id_funcionario": matricula_func,
                     "nome_funcionario":nome_func,
                     "cargo_func":cargo_func,
                     "salario_funcionario":salario_func,
                     "inicio_empresa":inicio_func,
                     "competencia":compet_func,
                     "nome_empresa":empresa_func,
                     "dt_nascimento":nasc_func,
                     "sexo_funcionario":sexo_func,
                     "status_funcionario":status_func,
                     })
            .execute()
        )
        if response.data:
            return response.data
        else:
            error_mensage = response.error or "Erro desconhecido"
            print(f'Erro ao inserir funcionário: {error_mensage}')
            return None 
    except Exception as e:
        print(f"Erro ao criar funcionário: {e}")
        return None

def buscar_empresas():
    try:
        response = supabase.table('tb_empresa').select('*').execute()
        if response.data:
            return response.data
        else:
            error_mensage = response.error or "Erro desconhecido"
            print(f'Erro ao buscar empresa: {error_mensage}')
            return None
    except Exception as e:
        print(f"Erro ao buscar empresa: {e}")
        return None
from database.database import supabase

def criar_funcionario(matricula_func, nome_func,cargo_func,salario_func,inicio_func,compet_func,empresa_func,nasc_func,sexo_func,status_func):
    try:
        response = (
            supabase.table("tb_funcionarios")
            .insert({"id_funcionario": matricula_func,
                     "nome_funcionario":nome_func,
                     "cargo_funcionario":cargo_func,
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
    
def armazenarFolhaPonto(matricula_func,id_linha,entrada_func,inicio_intervalo,termino_intervalo,hr_trab,dia_ponto,mes_ponto,ano_ponto,arquivo_ponto,periodo_inicio,periodo_fim):
    try:
        response = (
            supabase.table("tb_ponto")
            .insert({"id_funcionario": matricula_func,
                     "id_linha":id_linha,
                     "entrada_funcionario":entrada_func,
                     "inicio_intervalo":inicio_intervalo,
                     "termino_intervalo":termino_intervalo,
                     "hora_trabalhada":hr_trab,
                     "dia_ponto":dia_ponto,
                     "mes_ponto":mes_ponto,
                     "ano_ponto":ano_ponto,
                     "arquivo_ponto":arquivo_ponto,
                     "periodo_inicio":periodo_inicio,
                     "periodo_fim":periodo_fim,
                     })
            .execute()
        )
        if response.data:
            return response.data
        else:
            error_mensage = response.error or "Erro desconhecido"
            print(f'Erro ao inserir folha de ponto: {error_mensage}')
            return None 
    except Exception as e:
        print(f"Erro ao criar folha de ponto: {e}")
        return None
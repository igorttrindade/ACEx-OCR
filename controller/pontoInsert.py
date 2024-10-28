from datetime import datetime
from database.database import supabase

def armazenarBatidaPonto(id_funcionario,horario):
    try:
        response = supabase.table("tb_ponto").select("*").eq("id_funcionario", id_funcionario).single().execute()

        if response.data:
            registro = response.data
            horario = datetime.now().isoformat()

            if not registro.get("entrada_funcionario"):
                coluna, valor = "entrada_funcionario", horario
            elif not registro.get("inicio_intervalo"):
                coluna, valor = "inicio_intervalo", horario
            elif not registro.get("termino_intervalo"):
                coluna, valor = "termino_intervalo", horario
            elif not registro.get("saida_funcionario"):
                coluna, valor = "saida_funcionario", horario
            else:
                print("Todas as batidas de ponto já foram registradas para hoje.")
                return None
            
            update_response = (
                supabase.table("tb_ponto")
                .update({coluna: valor})
                .eq("id_funcionario", id_funcionario)
                .execute()
            )

            if update_response.data:
                return update_response.data
            else:
                print(f'Erro ao atualizar a batida de ponto: {update_response.error}')
                return None
        else:
            new_record = {
                "id_funcionario": id_funcionario,
                "entrada_funcionario": horario,
            }

            insert_response = (
                supabase.table("tb_ponto")
                .insert(new_record)
                .execute()
            )

            if insert_response.data:
                return insert_response.data
            else:
                print(f'Erro ao inserir nova batida de ponto: {insert_response.error}')
                return None


    except Exception as e:
        print(f"Erro ao registrar batida de ponto: {e}")
        return None

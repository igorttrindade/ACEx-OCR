from datetime import datetime
from database.database import supabase

def armazenarBatidaPonto(id_funcionario, horario):
    try:
        horario_atual = datetime.now()
        horario_format = horario_atual.strftime("%H:%M:%S")
        dia_ponto = horario_atual.day
        mes_ponto = horario_atual.month
        ano_ponto = horario_atual.year
        response = (
            supabase.table("tb_ponto")
            .select("*")
            .eq("id_funcionario", id_funcionario)
            .eq("dia_ponto", dia_ponto)
            .eq("mes_ponto", mes_ponto)
            .eq("ano_ponto", ano_ponto)
            .execute()
        )

        if response.data:
            registro = response.data[0]

            if all(registro.get(col) for col in ["entrada_funcionario", "inicio_intervalo", "termino_intervalo", "saida_funcionario"]):
                new_record = {
                    "id_funcionario": id_funcionario,
                    "entrada_funcionario": horario_format,
                    "dia_ponto": dia_ponto,
                    "mes_ponto": mes_ponto,
                    "ano_ponto": ano_ponto
                }
                insert_response = supabase.table("tb_ponto").insert(new_record).execute()
                if insert_response.data:
                    return insert_response.data
                else:
                    print(f'Erro ao inserir nova batida de ponto: {insert_response.error}')
                    return None
            else:
                if not registro.get("entrada_funcionario"):
                    coluna, valor = "entrada_funcionario", horario_format
                elif not registro.get("inicio_intervalo"):
                    coluna, valor = "inicio_intervalo", horario_format
                elif not registro.get("termino_intervalo"):
                    coluna, valor = "termino_intervalo", horario_format
                elif not registro.get("saida_funcionario"):
                    coluna, valor = "saida_funcionario", horario_format

                update_data = {coluna: valor}
                if coluna == "saida_funcionario" and registro.get("entrada_funcionario"):
                    entrada = datetime.strptime(registro["entrada_funcionario"], "%H:%M:%S")
                    horas_trabalhadas = horario_atual - entrada
                    update_data["hora_trabalhada"] = str(horas_trabalhadas)
                    
                if "id" in registro:
                    update_response = (
                        supabase.table("tb_ponto")
                        .update(update_data)
                        .eq("id_funcionario", id_funcionario)
                        .eq("id", registro["id"])
                        .execute()
                    )
                else:
                    update_response = (
                        supabase.table("tb_ponto")
                        .update(update_data)
                        .eq("id_funcionario", id_funcionario)
                        .eq("dia_ponto", dia_ponto)
                        .eq("mes_ponto", mes_ponto)
                        .eq("ano_ponto", ano_ponto)
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
                "entrada_funcionario": horario_format,
                "dia_ponto": dia_ponto,
                "mes_ponto": mes_ponto,
                "ano_ponto": ano_ponto
            }
            insert_response = supabase.table("tb_ponto").insert(new_record).execute()
            if insert_response.data:
                return insert_response.data
            else:
                print(f'Erro ao inserir nova batida de ponto: {insert_response.error}')
                return None

    except Exception as e:
        print(f"Erro ao registrar batida de ponto: {e}")
        return None
    
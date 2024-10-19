from database.database import supabase

def criar_usuario(email, id_usuario,date):
    try:
        response = (
            supabase.table("tb_usuario")
            .insert({"id_usuario": id_usuario,
                     "email_usuario":email,
                     "data_criacao":date,
                     })
            .execute()
        )
        if response.data:
            return response.data
        else:
            error_mensage = response.error or "Erro desconhecido"
            print(f'Erro ao inserir usuario: {error_mensage}')
            return None 
    except Exception as e:
        print(f"Erro ao criar usuário: {e}")
        return None
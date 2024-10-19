import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

def conectar_supabase():
    url = os.getenv('SUPABASE_URL')
    key = os.getenv('SUPABASE_KEY')

    try:
        supabase: Client = create_client(url, key)
        print("Conexão com Supabase bem-sucedida!")
        return supabase
    except Exception as e:
        print(f"Erro ao conectar com o Supabase: {e}")
        return None
supabase = conectar_supabase()

if supabase:
    print("Pronto para usar a base de dados!")
else:
    print("Falha na conexão com o Supabase.")
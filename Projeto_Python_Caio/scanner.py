import requests
import requests
import sqlite3 # Biblioteca para SQL

# 1. Criar/Conectar ao Banco de Dados e criar a tabela
conexao = sqlite3.connect("monitoramento.db")
cursor = conexao.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        site TEXT,
        status TEXT,
        seguranca TEXT
    )
""")
conexao.commit()

def verificar_e_salvar_sql(url):
    try:
        resposta = requests.get(url, timeout=5)
        status = str(resposta.status_code)
        seguranca = "Seguro (HTTPS)" if url.startswith("https") else "Inseguro (HTTP)"
    except:
        status = "Erro"
        seguranca = "N/A"

    # 2. Inserir os dados no Banco de Dados SQL
    cursor.execute("INSERT INTO logs (site, status, seguranca) VALUES (?, ?, ?)", (url, status, seguranca))
    conexao.commit()
    print(f"Dados de {url} salvos no SQL!")

# Teste
sites = ["https://www.google.com", "https://www.alguemquenaoexiste123.com"]
for s in sites:
    verificar_e_salvar_sql(s)

conexao.close()
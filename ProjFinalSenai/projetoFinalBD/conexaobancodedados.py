import mysql.connector


def conectar():
    return mysql.connector.connect(
        host='localhost',
        user='guilherme',
        password='cisco',
        database='loja'
    )

conexao = conectar()
if conexao.is_connected():
    print("Conectado com sucesso")
else:
    print("Erro ao conectar com o banco de dados")

import mysql.connector
from conexaobancodedados import conectar

def excluirClientePorID(id_cliente):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        
        cursor.execute("SET foreign_key_checks = 0")

        # Excluir o cliente
        query = "DELETE FROM Clientes WHERE id = %s"
        cursor.execute(query, (id_cliente,))
        conexao.commit()

        cursor.execute("SET foreign_key_checks = 1")

        print(f"Cliente com ID {id_cliente} excluído com sucesso!")

    except mysql.connector.Error as err:
        print(f"Erro: {err}")

def excluirFornecedorPorID(id_fornecedor):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        
        cursor.execute("SET foreign_key_checks = 0")

        # Excluir o fornecedor
        query = "DELETE FROM Fornecedor WHERE id = %s"
        cursor.execute(query, (id_fornecedor,))
        conexao.commit()

        cursor.execute("SET foreign_key_checks = 1")

        print(f"Fornecedor com ID {id_fornecedor} excluído com sucesso!")

    except mysql.connector.Error as err:
        print(f"Erro: {err}")

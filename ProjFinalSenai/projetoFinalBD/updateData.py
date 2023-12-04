import mysql.connector
from conexaobancodedados import conectar
from datetime import datetime, date

def atualizarCliente():
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        
        id_cliente = input('Digite o id do cliente: ')
        novo_p_nome = input('Digite o novo primeiro nome do cliente: ')
        novo_sobrenome = input('Digite o novo sobrenome do cliente:')
        novo_cpf = input('Digite o novo CPF do cliente: ')
        
        while True:
            data_nascimento_str = input("Digite a nova data de nascimento (AAAA-MM-DD): ")
            try:
                nova_data_nasc = datetime.strptime(data_nascimento_str, '%Y-%m-%d').date()
                break
            except ValueError:
                print("Formato de data inválido. Tente novamente.")

        # Atualizar os dados do cliente
        query = "UPDATE Clientes SET p_nome = %s, sobrenome = %s, cpf = %s, data_nasc = %s WHERE id = %s"
        cursor.execute(query, (novo_p_nome, novo_sobrenome, novo_cpf, nova_data_nasc, id_cliente))
        conexao.commit()

        print(f"Dados do Cliente com ID {id_cliente} atualizados com sucesso!")

    except mysql.connector.Error as err:
        print(f"Erro: {err}")


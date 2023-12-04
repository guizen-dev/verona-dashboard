import mysql.connector
from conexaobancodedados import conectar
from datetime import datetime, date
from getData import getCidadeByName

# Função para cadastrar cliente
def cadastrar_cliente():
    p_nome = input("Digite o primeiro nome: ")
    sobrenome = input("Digite o sobrenome: ")
    cpf = input("Digite o CPF: ")

    # Solicitar a data de nascimento no formato 'AAAA-MM-DD'
    while True:
        data_nascimento_str = input("Digite a data de nascimento (AAAA-MM-DD):")
        try:
            data_nascimento = datetime.strptime(data_nascimento_str, '%Y-%m-%d').date()
            break
        except ValueError:
            print("Formato de data inválido. Tente novamente.")

    # Solicitar o id_endereco associado ao cliente
    logradouro = input("Digite o logradouro do endereço: ")
    numero = input("Digite o número do endereço: ")
    cep = input("Digite o CEP do endereço: ")
    cidade_nome = input("Digite o nome da cidade: ")
    cidade_id = getCidadeByName(cidade_nome)

    cadastrar_endereco(logradouro, numero, cep, cidade_id)

    # Solicitar o id_telefone associado ao cliente
    telefone = int(input("Digite o telefone do cliente:"))
    tipo = input("Digite o tipo do telefone do cliente:")

    cadastrar_telefone(telefone, tipo)

    # Obter o id do último endereço e telefone cadastrados
    id_endereco = obter_ultimo_id("Enderecos")
    id_telefone = obter_ultimo_id("Telefone")

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        sql = "INSERT INTO Clientes (p_nome, sobrenome, cpf, data_nasc, id_endereco, id_telefone) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (p_nome, sobrenome, cpf, data_nascimento, id_endereco, id_telefone)
        cursor.execute(sql, valores)

        conexao.commit()
        print("Cliente cadastrado com sucesso!")

    except mysql.connector.Error as erro:
        print(f"Erro ao cadastrar cliente: {erro}")

    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()

# Função para cadastrar endereço
def cadastrar_endereco(logradouro, numero, cep, cidade_id):
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        sql = "INSERT INTO Enderecos (logradouro, numero, cep, cidade_id) VALUES (%s, %s, %s, %s)"
        valores = (logradouro, numero, cep, cidade_id)
        cursor.execute(sql, valores)

        conexao.commit()
        print("Endereço cadastrado com sucesso!")

    except mysql.connector.Error as erro:
        print(f"Erro ao cadastrar endereço: {erro}")

    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()

# Função para cadastrar telefone
def cadastrar_telefone(telefone, tipo):
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        sql = "INSERT INTO Telefone (telefone, tipo) VALUES (%s, %s)"
        valores = (telefone, tipo)
        cursor.execute(sql, valores)

        conexao.commit()
        print("Telefone cadastrado com sucesso!")

    except mysql.connector.Error as erro:
        print(f"Erro ao cadastrar telefone: {erro}")

    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()

# Função para obter o último ID de uma tabela
def obter_ultimo_id(tabela):
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        # Obter o último ID da tabela usando uma consulta
        sql = f"SELECT MAX(id) as last_id FROM {tabela}"
        cursor.execute(sql)

        resultado = cursor.fetchone()

        if resultado:
            return resultado[0]
        else:
            return None

    except mysql.connector.Error as erro:
        print(f"Erro ao obter último ID: {erro}")

    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()

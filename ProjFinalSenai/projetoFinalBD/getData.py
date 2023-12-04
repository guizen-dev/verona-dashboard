import mysql.connector
from conexaobancodedados import conectar

def getUfByName(name_uf):
    while True:
        try:      
            conexao = conectar()
            cursor = conexao.cursor()
            
            query = "SELECT id FROM Uf WHERE nome LIKE %s"
            cursor.execute(query, ('%' + name_uf + '%',))
            
            result = cursor.fetchone()
            return (result[0])
        except:
            print('Esse Uf não existe, tente novamente')
            
def getCidadeByName(cidade_nome):
    conexao = conectar()
    cursor = conexao.cursor()
    
    query = "SELECT id FROM Cidade WHERE nome LIKE %s"
    cursor.execute(query, (cidade_nome,))
    
    result = cursor.fetchone()
    
    if result:
        return result[0]
    else:
        print(f"No matching record found for {cidade_nome}")
        return err
    
def listarClientePorID(cliente_id):
    try:
        conexao = conectar()
        cursor = conexao.cursor(dictionary=True)
        query = "SELECT * FROM Clientes WHERE id = %s"
        cursor.execute(query, (cliente_id,))
        
        cliente = cursor.fetchone()

        if cliente:
            print(f"Detalhes do Cliente com ID {cliente_id}:")
            print(f"Primeiro Nome: {cliente['p_nome']}")
            print(f"Sobrenome: {cliente['sobrenome']}")
            print(f"CPF: {cliente['cpf']}")
            print(f"Data de Nascimento: {cliente['data_nasc']}")
            # Adicione mais campos conforme necessário

            return cliente
        else:
            print(f"Nenhum cliente encontrado com o ID {cliente_id}")
            return None

    except mysql.connector.Error as err:
        print(f"Erro: {err}")
        return None
    
    
def listarFornecedorPorID(id_fornecedor):
    try:
        conexao = conectar()
        cursor = conexao.cursor(dictionary=True)
        query = "SELECT * FROM Fornecedor WHERE id = %s"
        cursor.execute(query, (id_fornecedor,))
        
        fornecedor = cursor.fetchone()

        if fornecedor:
            print(f"Detalhes do Fornecedor com ID {id_fornecedor}:")
            print(f"Nome: {fornecedor['nome']}")
            print(f"CNPJ: {fornecedor['cnpj']}")
            # Adicione mais campos conforme necessário

            return fornecedor
        else:
            print(f"Nenhum fornecedor encontrado com o ID {id_fornecedor}")
            return None

    except mysql.connector.Error as err:
        print(f"Erro: {err}")
        return None
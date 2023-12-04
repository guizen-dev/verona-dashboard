import mysql.connector
from conexaobancodedados import conectar
from getData import getCidadeByName, listarClientePorID, listarFornecedorPorID
from deleteData import excluirClientePorID, excluirFornecedorPorID
from updateData import atualizarCliente
from createData import cadastrar_cliente, cadastrar_endereco, cadastrar_telefone, obter_ultimo_id

while True:
    print("[1] Cadastrar\n[2] Listar\n[3] Alterar\n[4] Deletar\n[5] Sair")
    opcao = int(input("Opção:  "))

    if opcao == 1:
        print("[1] Cadastrar Cliente\n[2] Cadastrar Fornecedor\n[0] Voltar")
        opcao_cadastro = int(input("Opção:"))

        if opcao_cadastro == 1:
            cadastrar_cliente()
        elif opcao_cadastro == 2:
            print('Disponivel em breve...')
                        
    if opcao == 2:
        print("[1] Listar Cliente\n[2] Listar Fornecedor\n[0] Voltar")
        opcao_listar = int(input("Opção:"))
        if opcao_listar == 1:
            cliente_id = input("Digite o id do cliente: ")
            print(listarClientePorID(cliente_id))
        elif opcao_listar == 2:
            fornecedor_id = input("Digite o id do fornecedor: ")
            print(listarFornecedorPorID(fornecedor_id))
    
    if opcao == 3:
        print("[1] Alterar Cliente\n[2] Alterar Fornecedor\n[0] Voltar")
        opcao_alterar= int(input("Opção:"))
        if opcao_alterar == 1:
            atualizarCliente()
        elif opcao_alterar == 2:
            fornecedor_id = input("Digite o id do fornecedor: ")
            print('Disponivel em breve...')
            
    if opcao == 4:
        print("[1] Deletar Cliente\n[2] Deletar Fornecedor\n[0] Voltar")
        opcao_deletar = int(input("Opção: "))
        if opcao_deletar == 1:
            cliente_id = input("Digite o id do cliente: ")
            excluirClientePorID(cliente_id)
        elif opcao_listar == 2:
            fornecedor_id = input("Digite o id do fornecedor: ")
            excluirFornecedorPorID(fornecedor_id)     

    elif opcao == 5:
        print("Programa Encerrado")
        break

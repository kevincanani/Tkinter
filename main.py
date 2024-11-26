import mysql.connector

conexao_banco = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'escritorio'

)

cursor = conexao_banco.cursor()

def create():

    op = input(f"Digite \nC se for cliente \nA se for Arquiteto \nP para projeto: ").upper()
    if op == 'C':
        id = int(input("Digite o id: "))         
        comando_sql = f'SELECT * FROM cliente WHERE id = {id}'
        cursor.execute(comando_sql)
        dados_escritorio = cursor.fetchall()
        
        if len(dados_escritorio) == 0:
            id = int(input("Digite o id do cliente: "))
            nome = input("Digite seu nome: ")
            cpf = int(input("Digite o seu CPF: "))
            rg = int(input("Digite o seu RG: "))
            telefone = int(input("Digite seu telefone: "))
            email = input("Digite seu email: ")
            cidade = input("Digite o nome da sua cidade: ")
            estado = input("Digie o nome do seu estado")
            endereco = input("Digite seu endereço: ")

            comando_sql = f'INSERT INTO cliente (id, nome, cpf, rg, telefone, email, cidade, estado, endereco) VALUES({id}, "{nome}","{cpf}", "{rg}", {telefone}, "{email}", "{cidade}", "{estado}", "{endereco}")'
            cursor.execute(comando_sql)
            conexao_banco.commit()
        else:
            print(dados_escritorio)
            print("Id já cadastrado!")

    elif op == 'A':
        id = int(input("Digite o id do arquiteto(a): "))
        comando_sql = f'SELECT * FROM arquiteto WHERE id = {id}'
        cursor.execute(comando_sql)
        dados_escritorio = cursor.fetchall()

        if len(dados_escritorio) == 0:
            id = int(input("Digite o id: "))
            nome = input("Digite seu nome: ")
            cpf = int(input("Digite o seu CPF: "))
            rg = int(input("Digite o seu RG: "))
            telefone = int(input("Digite seu telefone: "))
            email = input("Digite seu email: ")
            cidade = input("Digite o nome da sua cidade: ")
            estado = input("Digie o nome do seu estado")
            endereco = input("Digite seu endereço: ")

            comando_sql = f'INSERT INTO arquiteto(id, nome, cpf, rg, telefone, email, cidade, estado, endereco) VALUES({id}, "{nome}","{cpf}", "{rg}", {telefone}, "{email}", "{cidade}", "{estado}", "{endereco}")'
            cursor.execute(comando_sql)
            conexao_banco.commit()
        else:
            print(dados_escritorio)
            print("Id já cadastrado!")

    elif op == 'P':
        id = int(input("Digite o id do projeto: "))
        comando_sql = f'SELECT * FROM projeto WHERE id = {id}'
        cursor.execute(comando_sql)
        dados_escritorio = cursor.fetchall()

        if len(dados_escritorio) == 0:
            id = int(input("Digite o id: "))
            projeto = input("Digite seu nome: ")
            tipo_projeto = input("Digite o tipo de projeto: ")
            orcamento = float(input("Digite o orçamento do projeto: "))
            cidade = input("Digite o nome da sua cidade: ")
            data_inicio = input("Digite a data de inicio (formato: YYYY-MM-DD): ")
            data_entrega = input("Digite a data de entrega (formato: YYYY-MM-DD): ")
            id_cliente = int(input("Digite o id do cliente:"))
            id_arquiteto = int(input("Digite o id do arquiteto: "))

            comando_sql = f'INSERT INTO projeto (id, projeto, tipo, orcamento, data_inicio, data_entrega, id_cliente, id_arquiteto) VALUES({id}, "{projeto}","{tipo_projeto}", "{orcamento}", "{data_inicio}", "{data_entrega}", "{id_cliente}","{id_arquiteto}")'
            cursor.execute(comando_sql)
            conexao_banco.commit()
            if not cursor.fetchall():
                print("Cliente não encontrado! Insira um id válido.")
                return

            comando_sql = f'SELECT * FROM arquiteto WHERE id = {id}'
            cursor.execute(comando_sql)
            if not cursor.fetchall():
                print("Arquiteto não encontrado! Insira um id válido.")
                return
            
            comando_sql = f'INSERT INTO projeto (id, projeto, tipo, orcamento, data_inicio, data_entrega, id_cliente, id_arquiteto) VALUES({id}, "{projeto}","{tipo_projeto}, "{orcamento}", "{data_inicio}", "{data_entrega}", {id_cliente},{id_arquiteto})'
            cursor.execute(comando_sql)
            conexao_banco.commit()
            print("Projeto cadastratado com sucesso!")
        else:
            print(dados_escritorio)
            print("Id já cadastrado!")
    else:
        print("Opção inválida!")
        
def update():
    op = input(f"Digite o que deseja alterar: \nC se for cliente \nA se for Arquiteto \nP para projeto: ").upper()

    if op == 'C':
        id = int(input("Digite o id do cliente: "))  
        comando_sql = f'SELECT * FROM cliente WHERE id = {id}'
        cursor.execute(comando_sql)
        dados_escritorio = cursor.fetchall()

        if len(dados_escritorio) > 0:
            for cont in dados_escritorio:
                    print(f'ID: {cont[0]}\nNome: {cont[1]}\nCPF: {cont[2]} \nRG: {cont[3]} \nTelefone: {cont[4]} \nEmail: {cont[5]} \nCidade: {cont[6]} \nEstado: {cont[7]} \nEndereço: {cont[8]}')

            escolha = input('O que deseja alterar?:\nT - telefone\nE - E-mail \nC - cidade \nES - estado \nED - endereço: ').upper()
            
            if escolha == "T":
                telefone = int(input('Insira o novo telefone: '))
                comando_sql = f'UPDATE cliente SET telefone = {telefone} WHERE id = {id}'
                cursor.execute(comando_sql)
                conexao_banco.commit()
                print(f"Dado atualizado com sucesso!")

            elif escolha == "E":
                email = input('Insira o novo email: ')
                comando_sql = f'UPDATE cliente SET email = "{email}" WHERE id = {id}'
                cursor.execute(comando_sql)
                conexao_banco.commit()
                print(f"Dado atualizado com sucesso!")

            elif escolha == "C":
                cidade = input('Insira a nova cidade: ')
                comando_sql = f'UPDATE cliente SET cidade = "{cidade}" WHERE id = {id}'
                cursor.execute(comando_sql)
                conexao_banco.commit()
                print(f"Dado atualizado com sucesso!")

            elif escolha == "ES":
                estado = input('Insira o novo estado: ')
                comando_sql = f'UPDATE cliente SET estado = "{estado}" WHERE id = {id}'
                cursor.execute(comando_sql)
                conexao_banco.commit()
                print(f"Dado atualizado com sucesso!")

            elif escolha == "ED":
                endereco = input('Insira o novo endereço: ')
                comando_sql = f'UPDATE cliente SET endereco = "{endereco}" WHERE id = {id}'
                cursor.execute(comando_sql)
                conexao_banco.commit()
                print(f"Dado atualizado com sucesso!")

            else:
                print("Opção inválida!")

        else:
            print(f"Cliente com ID {id} não encontrado!")

    elif op == 'A':
        id = int(input("Digite o id do arquiteto: "))  
        comando_sql = f'SELECT * FROM arquiteto WHERE id = {id}'
        cursor.execute(comando_sql)
        dados_escritorio = cursor.fetchall()

        if len(dados_escritorio) > 0:
            for cont in dados_escritorio:
                    print(f'ID: {cont[0]}\nNome: {cont[1]}\nCPF: {cont[2]} \nRG: {cont[3]} \nTelefone: {cont[4]} \nEmail: {cont[5]} \nCidade: {cont[6]} \nEstado: {cont[7]} \nEndereço: {cont[8]}')

            escolha = input('O que deseja alterar?:\nT - telefone\nE - E-mail \nC - cidade \nES - estado \nED - endereço: ').upper()

            if escolha == "T":
                telefone = int(input('Insira o novo telefone: '))
                comando_sql = f'UPDATE arquiteto SET telefone = {telefone} WHERE id = {id}'
                cursor.execute(comando_sql)
                conexao_banco.commit()
                print(f"Dado atualizado com sucesso!")

            elif escolha == "E":
                email = input('Insira o novo email: ')
                comando_sql = f'UPDATE arquiteto SET email = "{email}" WHERE id = {id}'
                cursor.execute(comando_sql)
                conexao_banco.commit()
                print(f"Dado atualizado com sucesso!")

            elif escolha == "C":
                cidade = input('Insira a nova cidade: ')
                comando_sql = f'UPDATE arquiteto SET cidade = "{cidade}" WHERE id = {id}'
                cursor.execute(comando_sql)
                conexao_banco.commit()
                print(f"Dado atualizado com sucesso!")

            elif escolha == "ES":
                estado = input('Insira o novo estado: ')
                comando_sql = f'UPDATE arquiteto SET estado = "{estado}" WHERE id = {id}'
                cursor.execute(comando_sql)
                conexao_banco.commit()
                print(f"Dado atualizado com sucesso!")

            elif escolha == "ED":
                endereco = input('Insira o novo endereço: ')
                comando_sql = f'UPDATE arquiteto SET endereco = "{endereco}" WHERE id = {id}'
                cursor.execute(comando_sql)
                conexao_banco.commit()
                print(f"Dado atualizado com sucesso!")

            else:
                print("Opção inválida!")

        else:
            print(f"Arquiteto com ID {id} não encontrado!")

    elif op == 'P':
        id = int(input("Digite o id do projeto: "))  
        comando_sql = f'SELECT * FROM projeto WHERE id = {id}'
        cursor.execute(comando_sql)
        dados_escritorio = cursor.fetchall()

        if len(dados_escritorio) > 0:
            for cont in dados_escritorio:
                    print(f'ID: {cont[0]}\nNome do Projeto: {cont[1]}\nTipo de Projeto: {cont[2]} \nOrçamento: {cont[3]} \nData de Início: {cont[4]} \Data Final: {cont[5]}')

            escolha = input('O que deseja alterar?:\nN - nome do projeto \nT - tipo de projeto \nO - orçamento \nDI - data de início \nDF - data final: ').upper()

            if escolha == "N":
                nome = input('Insira o novo nome do projeto: ')
                comando_sql = f'UPDATE projeto SET projeto = "{nome}" WHERE id = {id}'
                cursor.execute(comando_sql)
                conexao_banco.commit()
                print(f"Dado atualizado com sucesso!")

            elif escolha == "T":
                tipo_projeto = input('Insira o novo tipo de projeto: ')
                comando_sql = f'UPDATE projeto SET tipo = "{tipo_projeto}" WHERE id = {id}'
                cursor.execute(comando_sql)
                conexao_banco.commit()
                print(f"Dado atualizado com sucesso!") 

            elif escolha == "O":
                orcamento = float(input('Insira o novo orçamento: '))
                comando_sql = f'UPDATE projeto SET orcamento = {orcamento} WHERE id = {id}'
                cursor.execute(comando_sql)
                conexao_banco.commit()
                print(f"Dado atualizado com sucesso!")

            elif escolha == "DI":
                data_inicio = input('Insira a nova data de início (YYYY-MM-DD): ')
                comando_sql = f'UPDATE projeto SET data_inicio = "{data_inicio}" WHERE id = {id}'
                cursor.execute(comando_sql)
                conexao_banco.commit()
                print(f"Dado atualizado com sucesso!")

            elif escolha == "DF":
                data_final = input('Insira a nova data de entrega (YYYY-MM-DD): ')
                comando_sql = f'UPDATE projeto SET data_entrega = "{data_final}" WHERE id = {id}'
                cursor.execute(comando_sql)
                conexao_banco.commit()
                print(f"Dado atualizado com sucesso!")

            else:
                print("Opção inválida!")

        else:
            print(f"Projeto com ID {id} não encontrado!")

    else:
        print("Opção inválida!")


def delete():

        op = input(f"Digite o que você é: \nA para arquiteto e \nC para cliente:  ").upper()
        if op == 'A':
            id = int(input("Digite o id do arquiteto(a): "))
            comando_sql = f'SELECT * FROM arquiteto WHERE id = {id}'
            cursor.execute(comando_sql)
            dados_escritorio = cursor.fetchall()
            if id in dados_escritorio and len(dados_escritorio) > 0:
                for cont in dados_escritorio:
                    print(f'ID: {cont[0]}\nNome: {cont[1]}\nCPF: {cont[2]} \nRG: {cont[3]} \nTelefone: {cont[4]} \nEmail: {cont[5]} \nCidade: {cont[6]} \nEstado: {cont[7]} \nEndereço: {cont[8]}')
                
            id = int(input("Digite o id do: "))
            comando_sql = f'SELECT * FROM projeto WHERE id = {id}'
            cursor.execute(comando_sql)
            dados_escritorio = cursor.fetchall()

            comando = f'DELETE FROM projeto WHERE id = {id}'
            cursor.execute(comando)
            conexao_banco.commit()
            print('Projeto excluído!')

        elif op == 'C':
            print("Você não é autorizado á utilizar este serviço.")

        else:
            print("Opção inválida!")

def read():
        op = input(f"Digite para pesquisa: \nC se for cliente \nA se for Arquiteto \nP para projeto: ").upper()  

        if op == 'C':
            escolha = input(f"Digite o que deseja pesquisar do cliente: \nN - nome \nCPF - cpf \nRG - rg \nT - telefone \nEm - email \nC - cidade \nE - estado \nEND - endereço:").upper()
            if escolha == 'N':
                nome = input('Digite o nome do cliente: ')
                comando_sql= f'SELECT * FROM cliente WHERE nome like "%{nome}%"'
                cursor.execute(comando_sql)
                dados_escritorio = cursor.fetchall()
                if len(dados_escritorio) <= 0:
                    print('Nome não encontrado!')
                else:
                    for cont in dados_escritorio:
                        print(f'ID: {cont[0]}\nNome: {cont[1]}\nCPF: {cont[2]} \nRG: {cont[3]} \nTelefone: {cont[4]} \nEmail: {cont[5]} \nCidade: {cont[6]} \nEstado: {cont[7]} \nEndereço: {cont[8]}')
                

            elif escolha == 'CPF':
                cpf = int(input("Digite o cpf do cliente: "))
                comando_sql= f'SELECT * FROM cliente WHERE cpf = {cpf}'
                cursor.execute(comando_sql)
                dados_escritorio = cursor.fetchall()
                if len(dados_escritorio) <= 0:
                    print('CPF não encontrado!')
                else:
                    for cont in dados_escritorio:
                        print(f'ID: {cont[0]}\nNome: {cont[1]}\nCPF: {cont[2]} \nRG: {cont[3]} \nTelefone: {cont[4]} \nEmail: {cont[5]} \nCidade: {cont[6]} \nEstado: {cont[7]} \nEndereço: {cont[8]}')

            elif escolha == 'RG':
                rg = int(input("Digite o rg do cliente: "))
                comando_sql= f'SELECT * FROM cliente WHERE rg = {rg}'
                cursor.execute(comando_sql)
                dados_escritorio = cursor.fetchall()
                if len(dados_escritorio) <= 0:
                    print('RG não encontrado!')
                else:
                    for cont in dados_escritorio:
                        print(f'ID: {cont[0]}\nNome: {cont[1]}\nCPF: {cont[2]} \nRG: {cont[3]} \nTelefone: {cont[4]} \nEmail: {cont[5]} \nCidade: {cont[6]} \nEstado: {cont[7]} \nEndereço: {cont[8]}')

            elif escolha == 'T':
                telefone = int(input("Digite o telefone do cliente: "))
                comando_sql= f'SELECT * FROM cliente WHERE telefone = {telefone}'
                cursor.execute(comando_sql)
                dados_escritorio = cursor.fetchall()
                if len(dados_escritorio) <= 0:
                    print('Telefone não encontrado!')
                else:
                    for cont in dados_escritorio:
                        print(f'ID: {cont[0]}\nNome: {cont[1]}\nCPF: {cont[2]} \nRG: {cont[3]} \nTelefone: {cont[4]} \nEmail: {cont[5]} \nCidade: {cont[6]} \nEstado: {cont[7]} \nEndereço: {cont[8]}')

            elif escolha == 'EM':
                email = input("Digite o email do cliente: ")
                comando_sql= f'SELECT * FROM cliente WHERE email LIKE "%{email}%"'
                cursor.execute(comando_sql)
                dados_escritorio = cursor.fetchall()
                if len(dados_escritorio) <= 0:
                    print('Email não encontrado!')
                else:
                    for cont in dados_escritorio:
                        print(f'ID: {cont[0]}\nNome: {cont[1]}\nCPF: {cont[2]} \nRG: {cont[3]} \nTelefone: {cont[4]} \nEmail: {cont[5]} \nCidade: {cont[6]} \nEstado: {cont[7]} \nEndereço: {cont[8]}')

            elif escolha == 'C':
                cidade = input("Digite a cidade do cliente: ")
                comando_sql= f'SELECT * FROM cliente WHERE cidade LIKE  "%{cidade}%"'
                cursor.execute(comando_sql)
                dados_escritorio = cursor.fetchall()
                if len(dados_escritorio) <= 0:
                    print('Cidade não encontrada!')
                else:
                    for cont in dados_escritorio:
                        print(f'ID: {cont[0]}\nNome: {cont[1]}\nCPF: {cont[2]} \nRG: {cont[3]} \nTelefone: {cont[4]} \nEmail: {cont[5]} \nCidade: {cont[6]} \nEstado: {cont[7]} \nEndereço: {cont[8]}')


            elif escolha == 'E':
                estado = input("Digite o estado do cliente: ")
                comando_sql= f'SELECT * FROM cliente WHERE estado LIKE "%{estado}%"'
                cursor.execute(comando_sql)
                dados_escritorio = cursor.fetchall()
                if len(dados_escritorio) <= 0:
                    print('Estado não encontrado!')
                else:
                    for cont in dados_escritorio:
                        print(f'ID: {cont[0]}\nNome: {cont[1]}\nCPF: {cont[2]} \nRG: {cont[3]} \nTelefone: {cont[4]} \nEmail: {cont[5]} \nCidade: {cont[6]} \nEstado: {cont[7]} \nEndereço: {cont[8]}')

            elif escolha == 'END':
                endereco = input("Digite o endereço do cliente: ")
                comando_sql= f'SELECT * FROM cliente WHERE endereco LIKE "%{endereco}%"'
                cursor.execute(comando_sql)
                dados_escritorio = cursor.fetchall()
                if len(dados_escritorio) <= 0:
                    print('Endereço não encontrado!')
                else:
                    for cont in dados_escritorio:
                        print(f'ID: {cont[0]}\nNome: {cont[1]}\nCPF: {cont[2]} \nRG: {cont[3]} \nTelefone: {cont[4]} \nEmail: {cont[5]} \nCidade: {cont[6]} \nEstado: {cont[7]} \nEndereço: {cont[8]}')

        elif op == "A":
            escolha = input(f"Digite o que deseja pesquisar do arquiteto: \nN - nome \nCPF - cpf \nRG - rg \nT - telefone \nEm - email \nC - cidade \nE - estado \nEND - endereço:").upper()
            if escolha == 'N':
                nome = input('Digite o nome do arquiteto: ')
                comando_sql= f'SELECT * FROM arquiteto WHERE nome like "%{nome}%"'
                cursor.execute(comando_sql)
                dados_escritorio = cursor.fetchall()
                if len(dados_escritorio) <= 0: 
                    print('Nome não encontrado!')
                else:
                    for cont in dados_escritorio:
                        print(f'ID: {cont[0]}\nNome: {cont[1]}\nCPF: {cont[2]} \nRG: {cont[3]} \nTelefone: {cont[4]} \nEmail: {cont[5]} \nCidade: {cont[6]} \nEstado: {cont[7]} \nEndereço: {cont[8]}')
            elif escolha == 'CPF':
                cpf = int(input("Digite o cpf do arquiteto: "))
                comando_sql= f'SELECT * FROM arquiteto WHERE cpf = {cpf}'
                cursor.execute(comando_sql)
                dados_escritorio = cursor.fetchall()
                if len(dados_escritorio) <= 0:
                    print('CPF não encontrado!')
                else:
                    for cont in dados_escritorio:
                        print(f'ID: {cont[0]}\nNome: {cont[1]}\nCPF: {cont[2]} \nRG: {cont[3]} \nTelefone: {cont[4]} \nEmail: {cont[5]} \nCidade: {cont[6]} \nEstado: {cont[7]} \nEndereço: {cont[8]}')

            elif escolha == 'RG':
                rg = int(input("Digite o rg do arquiteto: "))
                comando_sql= f'SELECT * FROM arquiteto WHERE rg = {rg}'
                cursor.execute(comando_sql)
                dados_escritorio = cursor.fetchall()
                if len(dados_escritorio) <= 0:
                    print('RG não encontrado!')
                else:
                    for cont in dados_escritorio:
                        print(f'ID: {cont[0]}\nNome: {cont[1]}\nCPF: {cont[2]} \nRG: {cont[3]} \nTelefone: {cont[4]} \nEmail: {cont[5]} \nCidade: {cont[6]} \nEstado: {cont[7]} \nEndereço: {cont[8]}')


            elif escolha == 'T':
                telefone = int(input("Digite o seu telefone: "))
                comando_sql= f'SELECT * FROM arquiteto WHERE telefone = {telefone}'
                cursor.execute(comando_sql)
                dados_escritorio = cursor.fetchall()
                if len(dados_escritorio) <= 0:
                    print('Telefone não encontrado!')
                else:
                    for cont in dados_escritorio:
                        print(f'ID: {cont[0]}\nNome: {cont[1]}\nCPF: {cont[2]} \nRG: {cont[3]} \nTelefone: {cont[4]} \nEmail: {cont[5]} \nCidade: {cont[6]} \nEstado: {cont[7]} \nEndereço: {cont[8]}')

            elif escolha == 'EM':
                email = input("Digite o email do arquiteto: ")
                comando_sql= f'SELECT * FROM arquiteto WHERE email LIKE "%{email}%"'
                cursor.execute(comando_sql)
                dados_escritorio = cursor.fetchall()
                if len(dados_escritorio) <= 0:
                    print('Email não encontrado!')
                else:
                    for cont in dados_escritorio:
                        print(f'ID: {cont[0]}\nNome: {cont[1]}\nCPF: {cont[2]} \nRG: {cont[3]} \nTelefone: {cont[4]} \nEmail: {cont[5]} \nCidade: {cont[6]} \nEstado: {cont[7]} \nEndereço: {cont[8]}')

            elif escolha == 'C':
                cidade = input("Digite a cidade do arquiteto: ")
                comando_sql= f'SELECT * FROM arquiteto WHERE cidade LIKE  "%{cidade}%"'
                cursor.execute(comando_sql)
                dados_escritorio = cursor.fetchall()
                if len(dados_escritorio) <= 0:
                    print('Cidade não encontrada!')
                else:
                    for cont in dados_escritorio:
                        print(f'ID: {cont[0]}\nNome: {cont[1]}\nCPF: {cont[2]} \nRG: {cont[3]} \nTelefone: {cont[4]} \nEmail: {cont[5]} \nCidade: {cont[6]} \nEstado: {cont[7]} \nEndereço: {cont[8]}')

            elif escolha == 'E':
                estado = input("Digite o estado do arquiteto: ")
                comando_sql= f'SELECT * FROM arquiteto WHERE estado LIKE "%{estado}%"'
                cursor.execute(comando_sql)
                dados_escritorio = cursor.fetchall()
                if len(dados_escritorio) <= 0:
                    print('Estado não encontrado!')
                else:
                    for cont in dados_escritorio:
                        print(f'ID: {cont[0]}\nNome: {cont[1]}\nCPF: {cont[2]} \nRG: {cont[3]} \nTelefone: {cont[4]} \nEmail: {cont[5]} \nCidade: {cont[6]} \nEstado: {cont[7]} \nEndereço: {cont[8]}')

            elif escolha == 'END':
                endereco = input("Digite o endereço do arquiteto: ")
                comando_sql= f'SELECT * FROM arquiteto WHERE endereco LIKE "%{endereco}%"'
                cursor.execute(comando_sql)
                dados_escritorio = cursor.fetchall()
                if len(dados_escritorio) <= 0:
                    print('Endereço não encontrado!')
            else:
                for cont in dados_escritorio:
                        print(f'ID: {cont[0]}\nNome: {cont[1]}\nCPF: {cont[2]} \nRG: {cont[3]} \nTelefone: {cont[4]} \nEmail: {cont[5]} \nCidade: {cont[6]} \nEstado: {cont[7]} \nEndereço: {cont[8]}')
        elif op == "P":
            escolha = input('O que deseja pesquisar?:\nN para nome do projeto \nT para tipo de projeto \nO para orçamento \nDI para data de início \nDF para data final: ').upper()
            if escolha == 'N':
                nome = input('Digite o nome do projeto: ')
                comando_sql= f'SELECT * FROM projeto WHERE nome like "%{nome}%"'
                cursor.execute(comando_sql)
                dados_escritorio = cursor.fetchall()
                if len(dados_escritorio) <= 0:
                    print('Nome não encontrado!')
                else:
                    for cont in dados_escritorio:
                        print(f'ID: {cont[0]}\nNome do Projeto: {cont[1]}\nTipo de Projeto: {cont[2]} \nOrçamento: {cont[3]} \nData de Início: {cont[4]} \Data Final: {cont[5]}')


            elif escolha == 'T':
                tipo = input('Digite o tipo do projeto: ')
                comando_sql= f'SELECT * FROM projeto WHERE tipo like "%{tipo}%"'
                cursor.execute(comando_sql)
                dados_escritorio = cursor.fetchall()   
                if len(dados_escritorio) <= 0:
                    print('Tipo de projeto não encontrado!')
                else:
                    for cont in dados_escritorio:
                        print(f'ID: {cont[0]}\nNome do Projeto: {cont[1]}\nTipo de Projeto: {cont[2]} \nOrçamento: {cont[3]} \nData de Início: {cont[4]} \Data Final: {cont[5]}')


            elif escolha == 'O':
                orcamento = float(input('Digite o orçamento do projeto: '))
                comando_sql= f'SELECT * FROM projeto WHERE orcamento = {orcamento}'
                cursor.execute(comando_sql)
                dados_escritorio = cursor.fetchall()
                if len(dados_escritorio) <= 0:
                    print('Nome não encontrado!')
                else:
                    for cont in dados_escritorio:
                        print(f'ID: {cont[0]}\nNome do Projeto: {cont[1]}\nTipo de Projeto: {cont[2]} \nOrçamento: {cont[3]} \nData de Início: {cont[4]} \Data Final: {cont[5]}')
           
            elif escolha == 'DI':
                data_inicio = input('Digite a data de entrega do projeto: ')
                comando_sql= f'SELECT * FROM projeto WHERE data_inicio = "{data_inicio}"'
                cursor.execute(comando_sql)
                dados_escritorio = cursor.fetchall()
                if len(dados_escritorio) <= 0:
                    print('Data não encontrada!')
                else:
                    for cont in dados_escritorio:
                        print(f'ID: {cont[0]}\nNome do Projeto: {cont[1]}\nTipo de Projeto: {cont[2]} \nOrçamento: {cont[3]} \nData de Início: {cont[4]} \Data Final: {cont[5]}')

            elif escolha == 'DF':
                data_entrega = input('Digite a data final do projeto: ')
                comando_sql= f'SELECT * FROM projeto WHERE data_entrega = "{data_entrega}"'
                cursor.execute(comando_sql)
                dados_escritorio = cursor.fetchall()
                if len(dados_escritorio) <= 0:
                    print('Data não encontrada!')
                else:
                    for cont in dados_escritorio:
                        print(f'ID: {cont[0]}\nNome do Projeto: {cont[1]}\nTipo de Projeto: {cont[2]} \nOrçamento: {cont[3]} \nData de Início: {cont[4]} \Data Final: {cont[5]}')


def sair():
    print("Você está deixando o programa...")

while True:
    menu = input('-- Controle de cadastro --\n1 - Cadastrar\n2 - Alterar\n3 - Deletar\n4 - Pesquisar\n5 - Sair: ')

    if menu == '1':
        create()
    elif menu == '2':
        update()
    elif menu == '3':
        delete()
    elif menu == '4':
        read()
    elif menu == '5':
        print('Saindo do programa... ')
        break
    else:
        print('Opção inválida!')
import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Conexão com o banco de dados
conexao_banco = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='escritorio'
)
cursor = conexao_banco.cursor()

# Função para limpar campos
def limpar_campos():
    nome_entry.delete(0, tk.END)
    cpf_entry.delete(0, tk.END)
    rg_entry.delete(0, tk.END)
    telefone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    cidade_entry.delete(0, tk.END)
    estado_entry.delete(0, tk.END)
    endereco_entry.delete(0, tk.END)
    id_entry.delete(0, tk.END)
    descricao_entry.delete(0, tk.END)
    data_inicio_entry.delete(0, tk.END)
    prazo_entry.delete(0, tk.END)
    arquiteto_id_entry.delete(0, tk.END)
    cliente_id_entry.delete(0, tk.END)

# Função de criar (Cadastrar)
def create(categoria):
    if categoria == 'A':  # Arquiteto
        nome = nome_entry.get()
        cpf = cpf_entry.get()
        rg = rg_entry.get()
        telefone = telefone_entry.get()
        email = email_entry.get()
        cidade = cidade_entry.get()
        estado = estado_entry.get()
        endereco = endereco_entry.get()
        comando_sql = f"INSERT INTO arquiteto (nome, cpf, rg, telefone, email, cidade, estado, endereco) VALUES ('{nome}', '{cpf}', '{rg}', '{telefone}', '{email}', '{cidade}', '{estado}', '{endereco}')"
        cursor.execute(comando_sql)
        conexao_banco.commit()
        messagebox.showinfo("Sucesso", "Arquiteto cadastrado com sucesso!")
    elif categoria == 'C':  # Cliente
        nome = nome_entry.get()
        cpf = cpf_entry.get()
        rg = rg_entry.get()
        telefone = telefone_entry.get()
        email = email_entry.get()
        cidade = cidade_entry.get()
        estado = estado_entry.get()
        endereco = endereco_entry.get()
        comando_sql = f"INSERT INTO cliente (nome, cpf, rg, telefone, email, cidade, estado, endereco) VALUES ('{nome}', '{cpf}', '{rg}', '{telefone}', '{email}', '{cidade}', '{estado}', '{endereco}')"
        cursor.execute(comando_sql)
        conexao_banco.commit()
        messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
    elif categoria == 'P':  # Projeto
        id = id_entry.get()
        projeto = descricao_entry.get()
        tipo_projeto = tipo_projeto_entry.get()
        orcamento = prazo_entry.get()
        data_inicio = data_inicio_entry.get()
        data_entrega = prazo_entry.get()
        cliente_id = cliente_id_entry.get()
        arquiteto_id = arquiteto_id_entry.get()

        # Validação de ID do cliente
        comando_sql = f'SELECT * FROM cliente WHERE id = {cliente_id}'
        cursor.execute(comando_sql)
        if not cursor.fetchall():
            messagebox.showerror("Erro", "Cliente não encontrado! Insira um id válido.")
            return

        # Validação de ID do arquiteto
        comando_sql = f'SELECT * FROM arquiteto WHERE id = {arquiteto_id}'
        cursor.execute(comando_sql)
        if not cursor.fetchall():
            messagebox.showerror("Erro", "Arquiteto não encontrado! Insira um id válido.")
            return

        comando_sql = f'INSERT INTO projeto (id, projeto, tipo, orcamento, data_inicio, data_entrega, id_cliente, id_arquiteto) VALUES ({id}, "{projeto}", "{tipo_projeto}", "{orcamento}", "{data_inicio}", "{data_entrega}", {cliente_id}, {arquiteto_id})'
        cursor.execute(comando_sql)
        conexao_banco.commit()
        messagebox.showinfo("Sucesso", "Projeto cadastrado com sucesso!")

# Função de ler (Pesquisar)
def read(categoria):
    if categoria == 'P':  # Projeto
        id = id_entry.get()
        comando_sql = f"SELECT * FROM projeto WHERE id = {id}"
        cursor.execute(comando_sql)
        dados = cursor.fetchall()
        if dados:
            for dado in dados:
                messagebox.showinfo("Resultado", f"ID: {dado[0]}\nProjeto: {dado[1]}\nTipo: {dado[2]}")
        else:
            messagebox.showinfo("Resultado", "Nenhum projeto encontrado!")

# Função de atualizar (Alterar)
def update(categoria):
    id = id_entry.get()
    if categoria == 'P':  # Projeto
        # Coleta os novos dados
        projeto = descricao_entry.get()
        tipo_projeto = tipo_projeto_entry.get()
        orcamento = prazo_entry.get()
        data_inicio = data_inicio_entry.get()
        data_entrega = prazo_entry.get()
        cliente_id = cliente_id_entry.get()
        arquiteto_id = arquiteto_id_entry.get()

        # Verificar se o projeto existe no banco de dados
        comando_sql = f"SELECT * FROM projeto WHERE id = {id}"
        cursor.execute(comando_sql)
        dados = cursor.fetchall()

        if dados:
            # Atualiza os dados no banco
            comando_sql = f"UPDATE projeto SET projeto='{projeto}', tipo='{tipo_projeto}', orcamento='{orcamento}', data_inicio='{data_inicio}', data_entrega='{data_entrega}', id_cliente={cliente_id}, id_arquiteto={arquiteto_id} WHERE id={id}"
            cursor.execute(comando_sql)
            conexao_banco.commit()
            messagebox.showinfo("Sucesso", "Projeto atualizado com sucesso!")
        else:
            messagebox.showerror("Erro", "Projeto não encontrado!")

# Função de deletar (Excluir)
def delete(categoria):
    id = id_entry.get()
    if categoria == 'P':  # Projeto
        comando_sql = f"DELETE FROM projeto WHERE id={id}"
        cursor.execute(comando_sql)
        conexao_banco.commit()
        messagebox.showinfo("Sucesso", "Projeto deletado com sucesso!")

# Função de sair
def sair():
    conexao_banco.close()
    window.quit()

# Criando a janela principal
window = tk.Tk()
window.title("Controle de Cadastro")

# Labels
tk.Label(window, text="Categoria (A para Arquiteto, C para Cliente, P para Projeto):").grid(row=0, column=0)
tk.Label(window, text="ID (para Alterar ou Deletar):").grid(row=1, column=0)
tk.Label(window, text="Nome:").grid(row=2, column=0)
tk.Label(window, text="CPF:").grid(row=3, column=0)
tk.Label(window, text="RG:").grid(row=4, column=0)
tk.Label(window, text="Telefone:").grid(row=5, column=0)
tk.Label(window, text="Email:").grid(row=6, column=0)
tk.Label(window, text="Cidade:").grid(row=7, column=0)
tk.Label(window, text="Estado:").grid(row=8, column=0)
tk.Label(window, text="Endereço:").grid(row=9, column=0)

# Novos campos para projeto
tk.Label(window, text="Descrição do Projeto:").grid(row=10, column=0)
tk.Label(window, text="Tipo de Projeto:").grid(row=11, column=0)
tk.Label(window, text="Orçamento:").grid(row=12, column=0)
tk.Label(window, text="Data de Início:").grid(row=13, column=0)
tk.Label(window, text="Data de Entrega:").grid(row=14, column=0)
tk.Label(window, text="ID do Cliente:").grid(row=15, column=0)
tk.Label(window, text="ID do Arquiteto:").grid(row=16, column=0)

# Entry widgets
op_entry = tk.Entry(window)
id_entry = tk.Entry(window)
nome_entry = tk.Entry(window)
cpf_entry = tk.Entry(window)
rg_entry = tk.Entry(window)
telefone_entry = tk.Entry(window)
email_entry = tk.Entry(window)
cidade_entry = tk.Entry(window)
estado_entry = tk.Entry(window)
endereco_entry = tk.Entry(window)
descricao_entry = tk.Entry(window)
tipo_projeto_entry = tk.Entry(window)
prazo_entry = tk.Entry(window)
data_inicio_entry = tk.Entry(window)
data_entrega_entry = tk.Entry(window)
cliente_id_entry = tk.Entry(window)
arquiteto_id_entry = tk.Entry(window)

# Grid de entradas
op_entry.grid(row=0, column=1)
id_entry.grid(row=1, column=1)
nome_entry.grid(row=2, column=1)
cpf_entry.grid(row=3, column=1)
rg_entry.grid(row=4, column=1)
telefone_entry.grid(row=5, column=1)
email_entry.grid(row=6, column=1)
cidade_entry.grid(row=7, column=1)
estado_entry.grid(row=8, column=1)
endereco_entry.grid(row=9, column=1)
descricao_entry.grid(row=10, column=1)
tipo_projeto_entry.grid(row=11, column=1)
prazo_entry.grid(row=12, column=1)
data_inicio_entry.grid(row=13, column=1)
data_entrega_entry.grid(row=14, column=1)
cliente_id_entry.grid(row=15, column=1)
arquiteto_id_entry.grid(row=16, column=1)

# Botões
# Cadastro
tk.Button(window, text="Cadastrar Arquiteto", command=lambda: create('A')).grid(row=17, column=0)
tk.Button(window, text="Cadastrar Cliente", command=lambda: create('C')).grid(row=17, column=1)
tk.Button(window, text="Cadastrar Projeto", command=lambda: create('P')).grid(row=17, column=2)

# Atualizar
tk.Button(window, text="Alterar Arquiteto", command=lambda: update('A')).grid(row=18, column=0)
tk.Button(window, text="Alterar Cliente", command=lambda: update('C')).grid(row=18, column=1)
tk.Button(window, text="Alterar Projeto", command=lambda: update('P')).grid(row=18, column=2)

# Deletar
tk.Button(window, text="Excluir Arquiteto", command=lambda: delete('A')).grid(row=19, column=0)
tk.Button(window, text="Excluir Cliente", command=lambda: delete('C')).grid(row=19, column=1)
tk.Button(window, text="Excluir Projeto", command=lambda: delete('P')).grid(row=19, column=2)

# Pesquisar
tk.Button(window, text="Pesquisar Arquiteto", command=lambda: read('A')).grid(row=20, column=0)
tk.Button(window, text="Pesquisar Cliente", command=lambda: read('C')).grid(row=20, column=1)
tk.Button(window, text="Pesquisar Projeto", command=lambda: read('P')).grid(row=20, column=2)

# Botão Sair
tk.Button(window, text="Sair", command=sair).grid(row=21, column=2)

# Executando a janela
window.mainloop()

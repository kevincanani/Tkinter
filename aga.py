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

    elif categoria == 'A':  # Arquiteto
        id = id_entry.get()
        comando_sql = f"SELECT * FROM arquiteto WHERE id = {id}"
        cursor.execute(comando_sql)
        dados = cursor.fetchall()
        if dados:
            for dado in dados:
                messagebox.showinfo("Resultado", f"ID: {dado[0]}\nArquiteto: {dado[1]}")
        else:
            messagebox.showinfo("Resultado", "Nenhum arquiteto encontrado!")

    
    elif categoria == 'C':  # Cliente
        id = id_entry.get()
        comando_sql = f"SELECT * FROM cliente WHERE id = {id}"
        cursor.execute(comando_sql)
        dados = cursor.fetchall()
        if dados:
            for dado in dados:
                messagebox.showinfo("Resultado", f"ID: {dado[0]}\nCliente: {dado[1]}")
        else:
            messagebox.showinfo("Resultado", "Nenhum cliente encontrado!")

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
    elif categoria == 'A':  # Arquiteto
        comando_sql = f"DELETE FROM arquiteto WHERE id={id}"
        cursor.execute(comando_sql)
        conexao_banco.commit()
        messagebox.showinfo("Sucesso", "Arquiteto deletado com sucesso!")
    elif categoria == 'C':  # Cliente
        comando_sql = f"DELETE FROM cliente WHERE id={id}"
        cursor.execute(comando_sql)
        conexao_banco.commit()
        messagebox.showinfo("Sucesso", "Cliente deletado com sucesso!")


# Função de sair
def sair():
    conexao_banco.close()
    window.quit()

# Criando a janela principal
window = tk.Tk()
window.title("Controle de Cadastro")
window['bg'] = "Navy Blue"

# Labels
tk.Label(window, text="Categoria (A para Arquiteto, C para Cliente, P para Projeto):",fg="Lime",bg="Navy Blue").place(x=550,y=70)
tk.Label(window, text="ID (para Alterar ou Deletar):",fg="Lime",bg="Navy Blue").place(x=550,y=90)
tk.Label(window, text="Nome:",fg="Lime",bg="Navy Blue").place(x=550,y=110)
tk.Label(window, text="CPF:",fg="Lime",bg="Navy Blue").place(x=550,y=130)
tk.Label(window, text="RG:",fg="Lime",bg="Navy Blue").place(x=550,y=150)
tk.Label(window, text="Telefone:",fg="Lime",bg="Navy Blue").place(x=550,y=170)
tk.Label(window, text="Email:",fg="Lime",bg="Navy Blue").place(x=550,y=190)
tk.Label(window, text="Cidade:",fg="Lime",bg="Navy Blue").place(x=550,y=210)
tk.Label(window, text="Estado:",fg="Lime",bg="Navy Blue").place(x=550,y=230)
tk.Label(window, text="Endereço:",fg="Lime",bg="Navy Blue").place(x=550,y=250)

# Novos campos para projeto
tk.Label(window, text="Descrição do Projeto:",fg="Lime",bg="Navy Blue").place(x=550,y=270)
tk.Label(window, text="Tipo de Projeto:",fg="Lime",bg="Navy Blue").place(x=550,y=290)
tk.Label(window, text="Orçamento:",fg="Lime",bg="Navy Blue").place(x=550,y=310)
tk.Label(window, text="Data de Início:",fg="Lime",bg="Navy Blue").place(x=550,y=330)
tk.Label(window, text="Data de Entrega:",fg="Lime",bg="Navy Blue").place(x=550,y=350)
tk.Label(window, text="ID do Cliente:",fg="Lime",bg="Navy Blue").place(x=550,y=370)
tk.Label(window, text="ID do Arquiteto:",fg="Lime",bg="Navy Blue").place(x=550,y=390)

# Entry widgets
op_entry = tk.Entry(window,background="Black",foreground="White",)
id_entry = tk.Entry(window,background="Black",foreground="White",)
nome_entry = tk.Entry(window,background="Black",foreground="White",)
cpf_entry = tk.Entry(window,background="Black",foreground="White",)
rg_entry = tk.Entry(window,background="Black",foreground="White",)
telefone_entry = tk.Entry(window,background="Black",foreground="White",)
email_entry = tk.Entry(window,background="Black",foreground="White",)
cidade_entry = tk.Entry(window,background="Black",foreground="White",)
estado_entry = tk.Entry(window,background="Black",foreground="White",)
endereco_entry = tk.Entry(window,background="Black",foreground="White",)
descricao_entry = tk.Entry(window,background="Black",foreground="White",)
tipo_projeto_entry = tk.Entry(window,background="Black",foreground="White",)
prazo_entry = tk.Entry(window,background="Black",foreground="White",)
data_inicio_entry = tk.Entry(window,background="Black",foreground="White",)
data_entrega_entry = tk.Entry(window,background="Black",foreground="White",)
cliente_id_entry = tk.Entry(window,background="Black",foreground="White",)
arquiteto_id_entry = tk.Entry(window,background="Black",foreground="White",)

# Grid de entradas
op_entry.place(x=890,y=70,)
id_entry.place(x=890,y=90)
nome_entry.place(x=890,y=110)
cpf_entry.place(x=890,y=130)
rg_entry.place(x=890,y=150)
telefone_entry.place(x=890,y=170)
email_entry.place(x=890,y=190)
cidade_entry.place(x=890,y=210)
estado_entry.place(x=890,y=230)
endereco_entry.place(x=890,y=250)
descricao_entry.place(x=890,y=270)
tipo_projeto_entry.place(x=890,y=290)
prazo_entry.place(x=890,y=310)
data_inicio_entry.place(x=890,y=330)
data_entrega_entry.place(x=890,y=350)
cliente_id_entry.place(x=890,y=370)
arquiteto_id_entry.place(x=890,y=390)

# Botões
# Cadastro
tk.Button(window, text="Cadastrar Arquiteto",background="Black",foreground="White", command=lambda: create('A')).place(x=535,y=420)
tk.Button(window, text="Cadastrar Cliente",background="Black",foreground="White", command=lambda: create('C')).place(x=650,y=420)
tk.Button(window, text="Cadastrar Projeto",background="Black",foreground="White", command=lambda: create('P')).place(x=750,y=420)

# Atualizar
tk.Button(window, text="Alterar Projeto",background="Black",foreground="White", command=lambda: update('P')).place(x=750,y=450)

# Deletar
tk.Button(window, text="Excluir Arquiteto",background="Black",foreground="White", command=lambda: delete('A')).place(x=535,y=480)
tk.Button(window, text="Excluir Cliente",background="Black",foreground="White", command=lambda: delete('C')).place(x=650,y=480)
tk.Button(window, text="Excluir Projeto",background="Black",foreground="White", command=lambda: delete('P')).place(x=750,y=480)

# Pesquisar
tk.Button(window, text="Pesquisar Arquiteto",background="Black",foreground="White", command=lambda: read('A')).place(x=535,y=510)
tk.Button(window, text="Pesquisar Cliente",background="Black",foreground="White", command=lambda: read('C')).place(x=650,y=510)
tk.Button(window, text="Pesquisar Projeto",background="Black",foreground="White", command=lambda: read('P')).place(x=750,y=510)

# Botão Sair
tk.Button(window, text="Sair",background="Black",foreground="White", command=sair).place(x=535,y=535)

# Executando a janela
window.mainloop()

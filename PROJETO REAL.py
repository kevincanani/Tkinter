from tkinter import *
 
menu = Tk()
menu.title("Sistema de Gerenciamento UGC")
 
menu.geometry("1920x1080")
menu['bg'] = "White"
 
#####################################################################################Centralização#################################################################################################
 
largura = 1920
altura = 1080
 
largura_screen = menu.winfo_screenwidth()
altura_screen = menu.winfo_screenheight()
 
 
print(largura_screen,altura_screen)
 
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2
 
menu.geometry("%dx%d+%d+%d" % (largura,altura,posx,posy))
 
 
####################################################################################DEFS################################################################################################
def cmd_Del():
    menu.destroy()

def Ppag():
    def Spag():
        def Acad_pag():
            def Volt():
                Label3.destroy()
                id_label.destroy()
                id.destroy()
                nome_label.destroy()
                nome.destroy()
                cpf_label.destroy()
                cpf.destroy()
                rg_label.destroy()
                rg.destroy()
                telefone_label.destroy()
                telefone.destroy()
                email_label.destroy()
                email.destroy()
                cidade_label.destroy()
                cidade.destroy()
                estado_label.destroy()
                estado.destroy()
                endereco_label.destroy()
                endereco.destroy()
                btnConfirmar.destroy()
                btnVoltar.destroy()
                Ppag()

            Label2.destroy()
            btnA.destroy()
            btnC.destroy()
            btnP.destroy()

            Label3 = Label(menu,text="------------------------------------------------------------------------------------------------------------------------Cadastro do Arquiteto------------------------------------------------------------------------------------------------------------------------:",bg="Black",fg="White", font="Courier 10 bold")
            Label3.pack()

            id_label = Label(menu, text='ID: ', bg="White", font=('Courier'))
            id_label.place(x=865, y=75)

            id = Entry(menu, width=50, background="Black", foreground="White")
            id.place(x=865, y=105)

            nome_label = Label(menu, text='Nome: ', bg="White", font=('Courier'))
            nome_label.place(x=865, y=135)

            nome = Entry(menu, width=50, background="Black", foreground="White")
            nome.place(x=865, y=165)

            cpf_label = Label(menu, text='CPF: ', bg="White", font=('Courier'))
            cpf_label.place(x=865, y=195)

            cpf = Entry(menu, width=50, background="Black", foreground="White")
            cpf.place(x=865, y=225)

            rg_label = Label(menu, text='RG: ', bg="White", font=('Courier'))
            rg_label.place(x=865, y=255)

            rg = Entry(menu, width=50, background="Black", foreground="White")
            rg.place(x=865, y=285)

            telefone_label = Label(menu, text='Telefone: ', bg="White", font=('Courier'))
            telefone_label.place(x=865, y=315)

            telefone = Entry(menu, width=50, background="Black", foreground="White")
            telefone.place(x=865, y=345)

            email_label = Label(menu, text='Email: ', bg="White", font=('Courier'))
            email_label.place(x=865, y=375)

            email = Entry(menu, width=50, background="Black", foreground="White")
            email.place(x=865, y=405)

            cidade_label = Label(menu, text='Cidade: ', bg="White", font=('Courier'))
            cidade_label.place(x=865, y=435)

            cidade = Entry(menu, width=50, background="Black", foreground="White")
            cidade.place(x=865, y=465)

            estado_label = Label(menu, text='Estado: ', bg="White", font=('Courier'))
            estado_label.place(x=865, y=495)

            estado = Entry(menu, width=50, background="Black", foreground="White")
            estado.place(x=865, y=525)

            endereco_label = Label(menu, text='Endereço: ', bg="White", font=('Courier'))
            endereco_label.place(x=865, y=555)

            endereco = Entry(menu, width=50, background="Black", foreground="White")
            endereco.place(x=865, y=585)

            btnConfirmar = Button(menu, text="Confirmar", width=15,bg="Black",fg="White")
            btnConfirmar.place(x=835, y=645)

            btnVoltar = Button(menu, text="Voltar", command=Volt, width=15,bg="Black",fg="White")
            btnVoltar.place(x=1080, y=645)

        def Ccad_pag():
            def Volt():
                Label3.destroy()
                id_label.destroy()
                id.destroy()
                nome_label.destroy()
                nome.destroy()
                cpf_label.destroy()
                cpf.destroy()
                rg_label.destroy()
                rg.destroy()
                telefone_label.destroy()
                telefone.destroy()
                email_label.destroy()
                email.destroy()
                cidade_label.destroy()
                cidade.destroy()
                estado_label.destroy()
                estado.destroy()
                endereco_label.destroy()
                endereco.destroy()
                btnConfirmar.destroy()
                btnVoltar.destroy()
                Ppag()

            Label2.destroy()
            btnA.destroy()
            btnC.destroy()
            btnP.destroy()

            Label3 = Label(menu,text="------------------------Cadastro do Cliente---------------------:",bg="Black",fg="White", font="Courier 10 bold")
            Label3.pack()

            id_label = Label(menu, text='ID: ', bg="White", font=('Courier'))
            id_label.place(x=865, y=75)

            id = Entry(menu, width=50, background="Black", foreground="White")
            id.place(x=865, y=105)

            nome_label = Label(menu, text='Nome: ', bg="White", font=('Courier'))
            nome_label.place(x=865, y=135)

            nome = Entry(menu, width=50, background="Black", foreground="White")
            nome.place(x=865, y=165)

            cpf_label = Label(menu, text='CPF: ', bg="White", font=('Courier'))
            cpf_label.place(x=865, y=195)

            cpf = Entry(menu, width=50, background="Black", foreground="White")
            cpf.place(x=865, y=225)

            rg_label = Label(menu, text='RG: ', bg="White", font=('Courier'))
            rg_label.place(x=865, y=255)

            rg = Entry(menu, width=50, background="Black", foreground="White")
            rg.place(x=865, y=285)

            telefone_label = Label(menu, text='Telefone: ', bg="White", font=('Courier'))
            telefone_label.place(x=865, y=315)

            telefone = Entry(menu, width=50, background="Black", foreground="White")
            telefone.place(x=865, y=345)

            email_label = Label(menu, text='Email: ', bg="White", font=('Courier'))
            email_label.place(x=865, y=375)

            email = Entry(menu, width=50, background="Black", foreground="White")
            email.place(x=865, y=405)

            cidade_label = Label(menu, text='Cidade: ', bg="White", font=('Courier'))
            cidade_label.place(x=865, y=435)

            cidade = Entry(menu, width=50, background="Black", foreground="White")
            cidade.place(x=865, y=465)

            estado_label = Label(menu, text='Estado: ', bg="White", font=('Courier'))
            estado_label.place(x=865, y=495)

            estado = Entry(menu, width=50, background="Black", foreground="White")
            estado.place(x=865, y=525)

            endereco_label = Label(menu, text='Endereço: ', bg="White", font=('Courier'))
            endereco_label.place(x=865, y=555)

            endereco = Entry(menu, width=50, background="Black", foreground="White")
            endereco.place(x=865, y=585)

            btnConfirmar = Button(menu, text="Confirmar", width=15,bg="Black",fg="White")
            btnConfirmar.place(x=835, y=645)

            btnVoltar = Button(menu, text="Voltar", command=Volt, width=15,bg="Black",fg="White")
            btnVoltar.place(x=1080, y=645)

        def Pcad_pag():
            def Volt():
                Label3.destroy()
                nome_label.destroy()
                nome.destroy()
                tipo_label.destroy()
                tipo.destroy()
                orcamento_label.destroy()
                orcamento.destroy()
                data_inicio_label.destroy()
                data_inicio.destroy()
                data_entrega_label.destroy()
                data_entrega.destroy()
                btnConfirmar.destroy()
                btnVoltar.destroy()
                Ppag()

            Label2.destroy()
            btnA.destroy()
            btnC.destroy()
            btnP.destroy()

            Label3 = Label(menu,text="------------------------------------------------------------------------------------------------------------------------Cadastro do Projeto------------------------------------------------------------------------------------------------------------------------:",bg="Black",fg="White", font="Courier 10 bold")
            Label3.pack()

            nome_label = Label(menu, text='Nome: ', bg="White", font=('Courier'))
            nome_label.place(x=865, y=75)

            nome = Entry(menu, width=50, background="Black", foreground="White")
            nome.place(x=865, y=105)

            tipo_label = Label(menu, text='Tipo: ', bg="White", font=('Courier'))
            tipo_label.place(x=865, y=135)

            tipo = Entry(menu, width=50, background="Black", foreground="White")
            tipo.place(x=865, y=165)

            orcamento_label = Label(menu, text='Orçamento: ', bg="White", font=('Courier'))
            orcamento_label.place(x=865, y=195)

            orcamento = Entry(menu, width=50, background="Black", foreground="White")
            orcamento.place(x=865, y=225)

            data_inicio_label = Label(menu, text='Data de início: ', bg="White", font=('Courier'))
            data_inicio_label.place(x=865, y=255)

            data_inicio = Entry(menu, width=50, background="Black", foreground="White")
            data_inicio.place(x=865, y=285)

            data_entrega_label = Label(menu, text='Data de entrega: ', bg="White", font=('Courier'))
            data_entrega_label.place(x=865, y=315)

            data_entrega = Entry(menu, width=50, background="Black", foreground="White")
            data_entrega.place(x=865, y=345)

            btnConfirmar = Button(menu, text="Confirmar", width=15,bg="Black",fg="White")
            btnConfirmar.place(x=835, y=645)

            btnVoltar = Button(menu, text="Voltar", command=Volt, width=15,bg="Black",fg="White")
            btnVoltar.place(x=1080, y=645)

        Label1.destroy()
        btn1.destroy()
        btn2.destroy()
        btn3.destroy()
        btn4.destroy()
        btn5.destroy()
 
        Label2 = Label(menu,text="------------------------------------------------------------------------------------------------------------------------Escolha a opção desejada de cadastro------------------------------------------------------------------------------------------------------------------------:",bg="Black",fg="White", font="Courier 10 bold")
        Label2.pack()
 
        btnA = Button(menu, text="Arquiteto" , command=Acad_pag,  width= 23,bg="Black",fg="White")
        btnA.place(x=865, y=75)
 
        btnC = Button(menu, text="Cliente" , command=Ccad_pag,  width= 23,bg="Black",fg="White")
        btnC.place(x=865, y=125)
 
        btnP = Button(menu, text="Projeto" , command=Pcad_pag,  width= 23,bg="Black",fg="White")
        btnP.place(x=865, y=175)

    Label1 = Label(menu,text="------------------------------------------------------------------------------------------------------------------------Sistema de Gerenciamento UGC------------------------------------------------------------------------------------------------------------------------",bg="Black",fg="White", font="Courier 10 bold")
    Label1.pack()
 
    def Altpag():
        def AltArq():
            def Volt():
                Label3.destroy()
                telefone_labelarq.destroy()
                telefonearq.destroy()
                email_labelarq.destroy()
                emailarq.destroy()
                cidade_labelarq.destroy()
                cidadearq.destroy()
                estado_labelarq.destroy()
                estadoarq.destroy()
                endereco_labelarq.destroy()
                enderecoarq.destroy()
                btnconf.destroy()
                btnvolt.destroy()
                Ppag()
        
            Label2.destroy()
            btnA.destroy()
            btnC.destroy()
            btnP.destroy()

            Label3 = Label(menu,text="------------------------------------------------------------------------------------------------------------------------Alterar Dados------------------------------------------------------------------------------------------------------------------------",bg="Black",fg="White", font="Courier 10 bold")
            Label3.pack()

            telefone_labelarq = Label(menu, text='Telefone: ', bg="White", font=('Courier'))
            telefone_labelarq.place(x=865, y=30)

            telefonearq = Entry(menu, width=50,bg="Black",fg="White")
            telefonearq.place(x=865, y=50)

            email_labelarq = Label(menu, text='Email: ', bg="White", font=('Courier'))
            email_labelarq.place(x=865, y=70)
 
            emailarq = Entry(menu, width=50,bg="Black",fg="White")
            emailarq.place(x=865, y=90)

            cidade_labelarq = Label(menu, text='Cidade: ', bg="White", font=('Courier'))
            cidade_labelarq.place(x=865, y=110)
 
            cidadearq = Entry(menu, width=50,bg="Black",fg="White")
            cidadearq.place(x=865, y=130)

            estado_labelarq = Label(menu, text='Estado: ', bg="White", font=('Courier'))
            estado_labelarq.place(x=865, y=150)
 
            estadoarq = Entry(menu, width=50,bg="Black",fg="White")
            estadoarq.place(x=865, y=170)

            endereco_labelarq = Label(menu, text='Endereço: ', bg="White", font=('Courier'))
            endereco_labelarq.place(x=865, y=190)
 
            enderecoarq = Entry(menu, width=50,bg="Black",fg="White")
            enderecoarq.place(x=865, y=210)

            btnconf = Button(menu, text="Confirmar",command=Volt, width= 23,bg="Black",fg="White")
            btnconf.place(x=835, y=260)

            btnvolt = Button(menu, text="Voltar",command=Volt, width= 23,bg="Black",fg="White")
            btnvolt.place(x=1080, y=260)

        def AltCli():
            def Volt():
                Label3.destroy()
                telefone_labelcli.destroy()
                telefonecli.destroy()
                email_labelcli.destroy()
                emailcli.destroy()
                cidade_labelcli.destroy()
                cidadecli.destroy()
                estado_labelcli.destroy()
                estadocli.destroy()
                endereco_labelcli.destroy()
                enderecocli.destroy()
                btnconf.destroy()
                btnvolt.destroy()
                Ppag()

            Label2.destroy()
            btnA.destroy()
            btnC.destroy()
            btnP.destroy()

            Label3 = Label(menu,text="------------------------------------------------------------------------------------------------------------------------Alterar Dados------------------------------------------------------------------------------------------------------------------------",bg="Black",fg="White", font="Courier 10 bold")
            Label3.pack()

            telefone_labelcli = Label(menu, text='Telefone: ', bg="White", font=('Courier'))
            telefone_labelcli.place(x=865, y=30)

            telefonecli = Entry(menu, width=50,bg="Black",fg="White")
            telefonecli.place(x=865, y=50)

            email_labelcli = Label(menu, text='Email: ', bg="White", font=('Courier'))
            email_labelcli.place(x=865, y=70)
 
            emailcli = Entry(menu, width=50,bg="Black",fg="White")
            emailcli.place(x=865, y=90)

            cidade_labelcli = Label(menu, text='Cidade: ', bg="White", font=('Courier'))
            cidade_labelcli.place(x=865, y=110)
 
            cidadecli = Entry(menu, width=50,bg="Black",fg="White")
            cidadecli.place(x=865, y=130)

            estado_labelcli = Label(menu, text='Estado: ', bg="White", font=('Courier'))
            estado_labelcli.place(x=865, y=150)
 
            estadocli = Entry(menu, width=50,bg="Black",fg="White")
            estadocli.place(x=865, y=170)

            endereco_labelcli = Label(menu, text='Endereço: ', bg="White", font=('Courier'))
            endereco_labelcli.place(x=865, y=190)
 
            enderecocli = Entry(menu, width=50,bg="Black",fg="White")
            enderecocli.place(x=865, y=210)

            btnconf = Button(menu, text="Confirmar",command=Volt, width= 23,bg="Black",fg="White")
            btnconf.place(x=835, y=260)

            btnvolt = Button(menu, text="Voltar",command=Volt, width= 23,bg="Black",fg="White")
            btnvolt.place(x=1080, y=260)

        def AltProj():
            def Volt():
                Label3.destroy()
                Nome_label.destroy()
                Nome.destroy()
                Tipo_label.destroy()
                Tipo.destroy()
                orca_label.destroy()
                Orca.destroy()
                DataI_label.destroy()
                DataI.destroy()
                DataF_label.destroy()
                DataF.destroy()
                btnconf.destroy()
                btnvolt.destroy()
                Ppag()

            Label2.destroy()
            btnA.destroy()
            btnC.destroy()
            btnP.destroy()

            Label3 = Label(menu,text="------------------------------------------------------------------------------------------------------------------------Alterar Dados------------------------------------------------------------------------------------------------------------------------",bg="Black",fg="White", font="Courier 10 bold")
            Label3.pack()

            Nome_label = Label(menu, text='Nome: ', bg="White", font=('Courier'))
            Nome_label.place(x=865, y=30)

            Nome = Entry(menu, width=50,bg="Black",fg="White")
            Nome.place(x=865, y=50)

            Tipo_label = Label(menu, text='Tipo: ', bg="White", font=('Courier'))
            Tipo_label.place(x=865, y=70)

            Tipo = Entry(menu, width=50,bg="Black",fg="White")
            Tipo.place(x=865, y=90)

            orca_label = Label(menu, text='Orçamento: ', bg="White", font=('Courier'))
            orca_label.place(x=865, y=110)

            Orca = Entry(menu, width=50,bg="Black",fg="White")
            Orca.place(x=865, y=130)

            DataI_label = Label(menu, text='DataInicio: ', bg="White", font=('Courier'))
            DataI_label.place(x=865, y=150)

            DataI = Entry(menu, width=50,bg="Black",fg="White")
            DataI.place(x=865, y=170)

            DataF_label = Label(menu, text='DataFinal: ', bg="White", font=('Courier'))
            DataF_label.place(x=865, y=190)

            DataF = Entry(menu, width=50,bg="Black",fg="White")
            DataF.place(x=865, y=210)

            btnconf = Button(menu, text="Confirmar",command=Volt, width= 23,bg="Black",fg="White")
            btnconf.place(x=835, y=260)

            btnvolt = Button(menu, text="Voltar",command=Volt, width= 23,bg="Black",fg="White")
            btnvolt.place(x=1080, y=260)




            


        Label1.destroy()
        btn1.destroy()
        btn2.destroy()
        btn3.destroy()
        btn4.destroy()
        btn5.destroy()
    
        Label2 = Label(menu,text="------------------------------------------------------------------------------------------------------------------------Escolha a opção desejada para Alterar------------------------------------------------------------------------------------------------------------------------:",bg="Black",fg="White", font="Courier 10 bold")
        Label2.pack()
    
        btnA = Button(menu, text="Arquiteto" ,command=AltArq,  width= 23,bg="Black",fg="White")
        btnA.place(x=865, y=75)
    
        btnC = Button(menu, text="Cliente" ,command=AltCli,  width= 23,bg="Black",fg="White")
        btnC.place(x=865, y=125)
    
        btnP = Button(menu, text="Projeto" ,command=AltProj,  width= 23,bg="Black",fg="White")
        btnP.place(x=865, y=175)



    #botao C
    btn1 = Button(menu, text="Cadastrar" , command=Spag,  width= 23,bg="Black",fg="White")
    btn1.place(x=865, y=75)
 
    #botao A
    btn2 = Button(menu, text="Alterar" ,command=Altpag, width= 23, bg="Black",fg="White")
    btn2.place(x=865, y=125)
 
    #botao D
    btn3 = Button(menu, text="Deletar" ,  width= 23,bg="Black",fg="White")
    btn3.place(x=865, y=175)
 
    #botao P
    btn4 = Button(menu, text="Pesquisar" , width= 23,bg="Black",fg="White")
    btn4.place(x=865, y=225)
 
    #botao S
    btn5 = Button(menu, text="Sair" , command=cmd_Del, width= 23,bg="Black",fg="White")
    btn5.place(x=865, y=275)

Ppag()
menu.mainloop()
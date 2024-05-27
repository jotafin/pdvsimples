import customtkinter

janela = customtkinter.CTk()
janela.geometry("500x300")
janela.title("Minha Oficina")
janela.iconbitmap("")
janela.resizable(False, False)
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

def fazer_login():
    # Verificar se o email e senha estão corretos (substitua isso com sua lógica real)
    if email.get() == "email" and senha.get() == "senha123":
        
        janela.destroy()
        
        abrir_tela_principal()
    else:
        print("Email ou senha incorretos")


def abrir_tela_principal():
    
    tela_principal = customtkinter.CTk()
    tela_principal.geometry("1200x720")
    tela_principal.title("Minha Oficina")
    tela_principal.iconbitmap("")
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")

    # Criando o Tabview para as abas
    tabview = customtkinter.CTkTabview(tela_principal)
    tabview.pack(fill="both", expand=True)

    tabview.add("Cadastro de Clientes")  # add tab at the end
    tabview.add("Cadastro de Produtos")  # add tab at the end
    tabview.set("Cadastro de Produtos")  # set currently visible tab

    # Widgets na aba "Cadastro de Clientes"
    frame_clientes = tabview.tab("Cadastro de Clientes")

    label_nome = customtkinter.CTkLabel(master=frame_clientes, text="Nome:")
    label_nome.grid(row=0, column=9, padx=10, pady=5)

    entry_nome = customtkinter.CTkEntry(master=frame_clientes)
    entry_nome.grid(row=0, column=10, padx=10, pady=5)

    label_email = customtkinter.CTkLabel(master=frame_clientes, text="Email:")
    label_email.grid(row=1, column=9, padx=10, pady=5)

    entry_email = customtkinter.CTkEntry(master=frame_clientes)
    entry_email.grid(row=1, column=10, padx=10, pady=5)

    label_endereco = customtkinter.CTkLabel(master=frame_clientes, text="Endereço:")
    label_endereco.grid(row=2, column=9, padx=10, pady=5)

    entry_endereco = customtkinter.CTkEntry(master=frame_clientes)
    entry_endereco.grid(row=2, column=10, padx=10, pady=5)

    label_celular = customtkinter.CTkLabel(master=frame_clientes, text="Celular:")
    label_celular.grid(row=3, column=9, padx=10, pady=5)

    entry_celular = customtkinter.CTkEntry(master=frame_clientes)
    entry_celular.grid(row=3, column=10, padx=10, pady=5)

    label_veiculo = customtkinter.CTkLabel(master=frame_clientes, text="Veículo:")
    label_veiculo.grid(row=4, column=9, padx=10, pady=5)

    entry_veiculo = customtkinter.CTkEntry(master=frame_clientes)
    entry_veiculo.grid(row=4, column=10, padx=10, pady=5)

    label_placa = customtkinter.CTkLabel(master=frame_clientes, text="Placa:")
    label_placa.grid(row=5, column=9, padx=10, pady=5)

    entry_placa = customtkinter.CTkEntry(master=frame_clientes)
    entry_placa.grid(row=5, column=10, padx=10, pady=5)

    checkPlaca = customtkinter.CTkCheckBox(master=frame_clientes, text="Sem Placa")
    checkPlaca.grid(row=6, column=10, padx=10, pady=10)


    def cadastrar_cliente():
        nome_cliente = entry_nome.get()
        email_c = entry_email.get()
        endereco_c = entry_endereco.get()
        celular_c = entry_celular.get()
        veiculo_c = entry_veiculo.get()
        placa_c = entry_placa.get()
        Splaca_c = checkPlaca.get()
        # Aqui você pode adicionar a lógica para cadastrar o cliente
        print("Cliente cadastrado:", nome_cliente, email_c, endereco_c, celular_c, veiculo_c, placa_c, Splaca_c )
    

    button_cadastrar = customtkinter.CTkButton(master=frame_clientes, text="Cadastrar", command=cadastrar_cliente)
    button_cadastrar.grid(row=7, column=10, padx=10, pady=10, sticky="ew")


    tela_principal.mainloop()


# LABEL
texto = customtkinter.CTkLabel(janela, text="Fazer Login")
texto.pack(padx=10, pady=10)

#EMAIL
email = customtkinter.CTkEntry(janela, placeholder_text="Seu e-mail")
email.pack(padx=10, pady=10)

#SENHA
senha = customtkinter.CTkEntry(janela, placeholder_text="Sua Senha", show="*")
senha.pack(padx=10, pady=10)

#CHECKBOX
check = customtkinter.CTkCheckBox(janela, text="lembrar Login")
check.pack(padx=10, pady=10)

#BOTAO
botao = customtkinter.CTkButton(janela, text="Login", command=fazer_login)
botao.pack(padx=10, pady=10)

#EXECUTAR A TELA
janela.mainloop()




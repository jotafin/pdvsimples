import customtkinter
from tela_principal import abrir_tela_principal

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

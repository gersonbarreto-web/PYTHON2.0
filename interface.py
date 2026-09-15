import customtkinter as ctk 
ctk.set_appearance_mode("dark")

#janela ------

janela = ctk.CTk()
janela.geometry("500x300")
janela.resizable(False,False)
janela.title("Sistema de Acesso - 2026")
janela.iconbitmap("padlock_21084.ico")

#------------------------------

# corpo da janela ------------------

titulo = ctk.CTkLabel(janela,
                      text="Sistema de Login",
                      text_color="#77ff00",
                      font=("arial",40))
titulo.pack()


login = ctk.CTkEntry(janela,
                     width=400,
                     height=40,
                     border_color="#77ff00",
                     placeholder_text="Digite o seu Login")
login.pack(pady=30)


senha = ctk.CTkEntry(janela,
                     width=400,
                     height=40,
                     border_color="#77ff00",
                     placeholder_text="Digite sua Senha",
                     show="•")
senha.pack()

botao = ctk.CTkButton(janela,
                      width=200,
                      height=40,
                      text="Acessar",
                      fg_color="#77ff00",
                      text_color="black",
                      cursor = "hand2",
                      font=("arial",30))
botao.pack(pady=30)



janela.mainloop()













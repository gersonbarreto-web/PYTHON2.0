import customtkinter as ctk
ctk.set_appearance_mode("dark")

#Funcao
def calcular ():
   try:
        m1 = float(media1.get())
        m2 = float(media2.get())
        m3 = float(media3.get())

        formula = (m1+m2+m3)/3

        if formula >= 5.0:
            status = "Aprovado"
            cor = "green" 
        else:
            status = "Recuperação"
            cor = "red"    

        resultado.configure(
            text=f"Média: {formula:.2f} - {status}", 
            text_color=cor
            )

   except ValueError:
        resultado.configure(text="Digite apenas números")

#janela
janela = ctk.CTk()
janela.geometry("600x550")
janela.resizable(False,False)
janela.title("Calculadora de Media")
janela.iconbitmap("42496school_99040.ico")

#Elementos internos
titulo = ctk.CTkLabel(janela,
                      text="Sistema escola",
                      text_color="#d5e408",
                      font=("Arial", 45,"bold"))
titulo.pack(pady=20)


media1 = ctk.CTkEntry(janela,
                      width=400,
                      height=40,
                      border_color="#ffffff",
                      placeholder_text= "Digite a primeira nota ")
media1.pack(pady=20)


media2 = ctk.CTkEntry(janela,
                      width=400,
                      height=40,
                      border_color="#ffffff",
                      placeholder_text="Digite a segunda nota ")

media2.pack(pady=20)


media3 = ctk.CTkEntry(janela,
                      width=400,
                      height=40,
                      border_color="#ffffff",
                      placeholder_text="Digite a terceira nota ")

media3.pack(pady=20)


botao = ctk.CTkButton(janela,
                      width=200,
                      height=40,
                      text="Resultado",
                      fg_color="#fbff07",
                      text_color="black",
                      cursor = "hand2",
                      font=("verdana",20),
                      command=calcular,
                      hover_color="#afafaf")
                        
botao.pack(pady=20)


resultado = ctk.CTkLabel(janela,
                         text="Media: ",
                         text_color="white",
                         font=("arial",20))

resultado.pack(pady=20)

janela.mainloop()


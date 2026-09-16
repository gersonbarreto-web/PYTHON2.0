import customtkinter as ctk
ctk.set_appearance_mode("dark")

#funcoes -------

def calcular():
    d = int(distancia.get())
    c = float(consumo.get())
    p = float(combustivel.get())

    formula = (d/c)*p

    resultado.configure(text=f"O valor para a viagem e de R$ {formula:.2f}")



#janela ----

janela = ctk.CTk()
janela.geometry("500x400")
janela.resizable(False,False)
janela.title("Calculadora de Viagem")
janela.iconbitmap("vw_transportation_car_7077.ico")

#--------------

# corpo da janela 

titulo = ctk.CTkLabel(janela,
                      text="APP VIAGEM",
                      text_color="#ffffff",
                      font=("verdana",45))
titulo.pack(pady=20)


distancia = ctk.CTkEntry(janela,
                         width=400,
                         height=40,
                         border_color="#ffffff",
                         placeholder_text="Digite a distancia da viagem em KM")
distancia.pack()


consumo = ctk.CTkEntry(janela,
                       width=400,
                       height=40,
                       border_color="#ffffff",
                       placeholder_text="Digite o consumo do seu veiculo")
consumo.pack(pady=30)


combustivel = ctk.CTkEntry(janela,
                       width=400,
                       height=40,
                       border_color="#ffffff",
                       placeholder_text="Digite o preco atual do combustivel")
combustivel.pack()



botao = ctk.CTkButton(janela,
                      width=200,
                      height=40,
                      text="Calcular Gasto",
                      fg_color="#f4f8f0",
                      text_color="black",
                      cursor = "hand2",
                      font=("verdana",20),
                      command=calcular)
botao.pack(pady=20)


resultado = ctk.CTkLabel(janela,
                         text="",
                         text_color="white",
                         font=("arial",20))

resultado.pack(pady=10)


janela.mainloop()


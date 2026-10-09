#Gerson Bruno Nunes Barreto
#Vitor Reis Moura Costa Doria



import customtkinter as ctk
janela = ctk.CTk()
ctk.set_appearance_mode("dark")

def calcular():
    try:
        
        m1 = float(media1.get())
        m2 = float(media2.get())

        formula = (m1 + m2) / 2

        if formula >= 7.0:
            status = "Aprovado"
            cor = "green"
        elif 5.0 <= formula < 7.0:
            status = "Recuperação"
            cor = "yellow"
        else:
            status = "Reprovado"
            cor = "red"
        
        resultado.configure(
            text=f"Média: {formula:.2f}\n{status}",
            text_color=cor
        )    
    except ValueError:
        resultado.configure(text="Digite apenas números válidos", text_color="white")

janela = ctk.CTk()
janela.geometry("600x550")
janela.resizable(False, False)
janela.title("Calculadora de Média")
janela.iconbitmap("42496school_99040.ico")



titulo = ctk.CTkLabel(
    janela,
    text="Sistema Escolar",
    text_color="#d5e408",
    font=("Arial", 45, "bold")
)
titulo.pack(pady=20)

nomeAluno = ctk.CTkEntry(
    janela,
    width=400,
    height=40,
    border_color="#ffffff",
    placeholder_text="Digite o nome do Aluno"
)
nomeAluno.pack(pady=20)

media1 = ctk.CTkEntry(
    janela,
    width=400,
    height=40,
    border_color="#ffffff",
    placeholder_text="Digite a primeira nota"
)
media1.pack(pady=20)

media2 = ctk.CTkEntry(
    janela,
    width=400,
    height=40,
    border_color="#ffffff",
    placeholder_text="Digite a segunda nota"
)
media2.pack(pady=20)

botao = ctk.CTkButton(
    janela,
    width=200,
    height=40,
    text="Resultado",
    fg_color="#fbff07",
    text_color="black",
    cursor="hand2",
    font=("verdana", 20),
    command=calcular,
    hover_color="#afafaf"
)
botao.pack(pady=20)

resultado = ctk.CTkLabel(
    janela,
    text="Média: ",
    text_color="white",
    font=("arial", 20)
)
resultado.pack(pady=20)

janela.mainloop()
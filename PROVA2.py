# Gerson Bruno Nunes Barreto
# Vitor Reis Moura Costa Doria

import customtkinter as ctk
janela = ctk.CTk()
ctk.set_appearance_mode("dark")




janela.resizable(False, False)
janela.title("Reserva de Hotel")


def calcular_hospedagem():
    try:
        diarias = int(Quantidade_D.get())
        valor_diaria = float(Valor_D.get().replace(",", "."))

        
        v_hospedagem = diarias * valor_diaria

        if diarias >= 5:
            desconto = v_hospedagem * 0.10
        else:
            desconto = 0.0

        total = v_hospedagem - desconto

        resultado.configure(
            text=f"Hospedagem: R$ {v_hospedagem:.2f}\n"
                 f"Desconto: R$ {desconto:.2f}\n"
                 f"Total a Pagar: R$ {total:.2f}"
        )
    except ValueError:
        resultado.configure(text="Erro: Preencha os campos numéricos corretamente!")


titulo = ctk.CTkLabel(
    janela.geometry("600x550"),
    text="Sistema de Hospedagem",
    text_color="#d5e408",
    font=("Arial", 35, "bold"),

)
titulo.pack(pady=20)

nome_H = ctk.CTkEntry(
    janela,
        width=400,
        height=40,
        border_color="#ffffff",
        placeholder_text="Digite o Nome do hospede")

nome_H.pack(pady=10)


Quantidade_D = ctk.CTkEntry(
    janela,
    width=400,
    height=40,
    border_color="#ffffff",
    placeholder_text="Digite a quantidade de diárias"
)
Quantidade_D.pack(pady=10)

Valor_D = ctk.CTkEntry(
    janela,
    width=400,
    height=40,
    border_color="#ffffff",
    placeholder_text="Digite o valor da diária (R$)"
)
Valor_D.pack(pady=10)

botao = ctk.CTkButton(
    janela,
    width=300,
    height=40,
    text="CALCULAR HOSPEDAGEM",
    fg_color="#0026ff",
    text_color="black",
    cursor="hand2",
    font=("verdana", 16, "bold"),
    command=calcular_hospedagem,
    hover_color="#afafaf"
)
botao.pack(pady=20)

resultado = ctk.CTkLabel(
    janela,
    text="",
    text_color="green",
    font=("arial", 18),
    justify="left"
)
resultado.pack(pady=10)

janela.mainloop()
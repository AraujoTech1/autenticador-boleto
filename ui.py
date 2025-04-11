import tkinter as tk
from tkinter import messagebox
from boleto_utils import validar_boleto, extrair_info

def validar():
    codigo = entry_codigo.get().strip()

    if not codigo:
        messagebox.showwarning("Campo vazio", "Digite o código de barras do boleto.")
        return

    if not validar_boleto(codigo):
        messagebox.showerror("Código inválido", "O código de barras digitado é inválido.")
        return

    banco, valor, vencimento = extrair_info(codigo)
    resultado.config(
        text=f"🏦 Banco: {banco}\n💵 Valor: R$ {valor}\n📅 Vencimento: {vencimento}"
    )

# UI com Tkinter
janela = tk.Tk()
janela.title("Autenticador de Boletos")
janela.geometry("400x300")
janela.configure(bg="#1e1e1e")

tk.Label(janela, text="Digite o código de barras do boleto:", bg="#1e1e1e", fg="white").pack(pady=10)
entry_codigo = tk.Entry(janela, width=50)
entry_codigo.pack()

tk.Button(janela, text="Validar", command=validar, bg="#4CAF50", fg="white").pack(pady=10)
resultado = tk.Label(janela, text="", bg="#1e1e1e", fg="white", font=("Arial", 11))
resultado.pack()

janela.mainloop()

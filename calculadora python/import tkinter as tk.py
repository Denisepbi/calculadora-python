import tkinter as tk

def calcular():
    try:
        expressao = entrada.get()
        resultado = eval(expressao)
        resultado_label.config(text=f"Resultado: {resultado}")
    except Exception as e:
        resultado_label.config(text="Erro ao calcular")

# Configuração da janela
janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("300x200")

# Entrada de texto
entrada = tk.Entry(janela, width=20)
entrada.pack(pady=10)

# Botão de cálculo
calcular_btn = tk.Button(janela, text="Calcular", command=calcular)
calcular_btn.pack()

# Resultado
resultado_label = tk.Label(janela, text="")
resultado_label.pack()

janela.mainloop()

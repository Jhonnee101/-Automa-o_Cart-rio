import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def salvar_matricula():
    try:
        # Tenta converter o texto do Entry para um inteiro
        valor_int_mat = int(mat_entry.get())
        valor_int_quant = int(quant_entry.get())
        print("Matrícula (int):", valor_int_mat)
        print("Quantidade (int):", valor_int_quant)
    except ValueError:
        # Se a conversão falhar, imprime uma mensagem de erro
        print("Por favor, digite números inteiros válidos.")

tela = ttk.Window(themename='darkly')
tela.geometry("400x240")
tela.title("Copiador de Matrículas")

# Label para o campo de matrícula
mat_label = ttk.Label(tela, text="Matrícula:")
mat_label.place(relx=0.3, rely=0.3, anchor='e')

mat_entry = ttk.Entry(tela, width=20)
mat_entry.place(relx=0.5, rely=0.3, anchor='center')

# Label para o campo de quantidade
quant_label = ttk.Label(tela, text="Quantidade:")
quant_label.place(relx=0.3, rely=0.5, anchor='e')

quant_entry = ttk.Entry(tela, width=20)
quant_entry.place(relx=0.5, rely=0.5, anchor='center')

salvar_btn = ttk.Button(tela, text="Salvar Matrícula", command=salvar_matricula)
salvar_btn.place(relx=0.5, rely=0.7, anchor='center')

tela.mainloop()


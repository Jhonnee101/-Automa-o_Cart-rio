import tkinter as tk
from func import *


janela = tk.Tk()
janela.geometry("500x400")

btn_selecionar = tk.Button(janela, text="Selecionar arquivo", command=selecionar_entrada)
btn_selecionar.pack()

btn_selecionar = tk.Button(janela, text="Selecionar Pasta", command=selecionar_pasta)
btn_selecionar.pack()

btn_salvar = tk.Button(janela, text="Iniciar Processo", command=extrair_matriculas)
btn_salvar.pack()

janela.mainloop()
import tkinter as tk
from tkinter import filedialog

def selecionar_arquivo():
    caminho_arquivo = filedialog.askopenfilename(title="Selecione o arquivo para analisar")
    if caminho_arquivo:
        label_caminho.config(text=caminho_arquivo)
    else:
        label_caminho.config(text="") 


janela = tk.Tk()
janela.geometry("500x200")
janela.title("Seleção de Arquivo")

btn_selecionar = tk.Button(janela, text="Selecionar Arquivo", command=selecionar_arquivo)
btn_selecionar.pack()

label_caminho = tk.Label(janela, text="", wraplength=400)
label_caminho.pack()

janela.mainloop()
import tkinter as tk
from tkinter import filedialog

janela = tk.Tk()
janela.geometry("500x400")

def salvar():
    caminho_arquivo = filedialog.asksaveasfilename(defaultextension=".txt")
    if caminho_arquivo:
        with open(caminho_arquivo, "w") as arquivo:
            arquivo.write("Conteúdo do arquivo") 
            print("Salvo com Sucesso!")


texto = tk.Label(janela, text="Fazer Login")
texto.pack(padx=10, pady=10)

botao = tk.Button(janela, text="Login", command=salvar)
botao.pack(padx=10, pady=10)


janela.mainloop()
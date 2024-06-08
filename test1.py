import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
caminho_arquivo = filedialog.asksaveasfilename(defaultextension=".txt")
if caminho_arquivo:
    with open(caminho_arquivo, "w") as arquivo:
        arquivo.write("Conteúdo do arquivo") 

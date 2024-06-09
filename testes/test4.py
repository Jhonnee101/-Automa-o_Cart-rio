import openpyxl as xl
import docx
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


caminho_selecionado = ""

def selecionar_pasta():
    global caminho_selecionado
    caminho_arquivo = filedialog.askdirectory(title="Selecione uma pasta para Salvar!")
    caminho_selecionado = caminho_arquivo

def extrair_matriculas():
    workbook = xl.load_workbook("doc.xlsx")
    planilha = workbook.active
    messagebox.showinfo("Concluido", "Processo concluido com Sucesso!")

    for rows in planilha.iter_rows(min_row=2):
        mat = rows[0].value
        texto = rows[1].value

        doc = docx.Document()
        doc.add_paragraph(f"Matrícula: {texto}")

        nome_arquivo = f"{mat} FALTA CONFERIR.docx"
        caminho_completo = f"{caminho_selecionado}/{nome_arquivo}"
        doc.save(caminho_completo)

    workbook.close()


janela = tk.Tk()
janela.geometry("500x400")

btn_selecionar = tk.Button(janela, text="Selecionar Pasta", command=selecionar_pasta)
btn_selecionar.pack()

btn_salvar = tk.Button(janela, text="Iniciar Processo", command=extrair_matriculas)
btn_salvar.pack()

janela.mainloop()
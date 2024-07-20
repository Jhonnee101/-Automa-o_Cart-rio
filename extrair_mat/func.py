from tkinter import messagebox
from tkinter import filedialog
import openpyxl as xl
import docx
import re
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Definição das variáveis globais
caminho_entrada = ""
caminho_saida = ""
strings_para_remover = [
    'CERTIDÃO DE INTEIRO TEOR',
    'CERTIFICO que atendendo ao requerimento do Sr.(a) , inscrito no CPF/MF sob o nº , conforme protocolo nº xxx, e assim, após ter procedido a competente busca nos Livros e Fichas de Registro de Imóveis deste Serviço Registral, deles verifiquei constar, que a matrícula nº ', 'CERTIFICO finalmente, que é tudo que contém na matrícula supramencionada O referido é verdade, dou fé. Para efeito de lavratura de atos notariais, a presente certidão é válida por 30 (trinta) dias, conforme item IV, art. 1º, do Decreto nº 93.240, de 09.09.1986.'
]

# Função para selecionar o arquivo de entrada
def selecionar_entrada():
    global caminho_entrada
    arquivo = filedialog.askopenfile(title="Selecione a planilha para analisar!")
    if arquivo:
        caminho_entrada = arquivo.name

# Função para selecionar a pasta de saída
def selecionar_pasta():
    global caminho_saida
    caminho_pasta = filedialog.askdirectory(title="Selecione uma pasta para Salvar!")
    caminho_saida = caminho_pasta

# Função para extrair matrículas e remover as strings definidas
# ... código anterior ...

def extrair_matriculas():
    global caminho_entrada, caminho_saida, strings_para_remover
    workbook = xl.load_workbook(caminho_entrada)
    planilha = workbook.active

    for rows in planilha.iter_rows(min_row=2):
        mat = rows[0].value
        texto = rows[1].value

        if mat is None:
            break
        else:
            # Remove as strings definidas se elas aparecerem no texto
            texto_atualizado = texto if texto else ''
            for string in strings_para_remover:
                texto_atualizado = texto_atualizado.replace(string, '')

            # Substitui qualquer sequência de 20 ou mais '=' por uma nova linha
            padrao = r'={10,}'
            texto_atualizado = re.sub(padrao, '\n\n', texto_atualizado)

            # Substitui cada string da lista strings_especificas2 por uma nova linha
            strings_especificas2 = ['Proprietária: ', 'Proprietário: ', 'Proprietaria: ', 'Proprietários: ', 'Proprietarios: ', 'Proprietárias: ', 'Proprietarias: ','Proprietarias -','Proprietarios -','Proprietaria -','Proprietario -',]
            for string in strings_especificas2:
                texto_atualizado = texto_atualizado.replace(string, '\n\n')

            doc = docx.Document()
            doc.styles['Normal'].font.name = 'Courier New'
            doc.styles['Normal'].font.size = Pt(12)
            p = doc.add_paragraph(texto_atualizado)
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

            nome_arquivo = f"{mat} FALTA CONFERIR.docx"
            caminho_completo = f"{caminho_saida}/{nome_arquivo}"
            doc.save(caminho_completo)

    workbook.close()
    messagebox.showinfo("Concluído", "Processo concluído com sucesso!")


root = ttk.Window("Extrator de Matriculas V3")
style = ttk.Style("vapor")

label = ttk.Label(root, text="Extrator de Matriculas V3")
label.pack(pady=20)
label.config(font=("Courier New", 18, "bold"))


b1 = ttk.Button(root, text="Selecionar Planilha", command=selecionar_entrada, bootstyle=INFO)
b1.pack(side=LEFT, padx=5, pady=10)

b2 = ttk.Button(root, text="Selecionar Pasta", command=selecionar_pasta, bootstyle=INFO)
b2.pack(side=LEFT, padx=5, pady=10)

b3 = ttk.Button(root, text="Iniciar Extração", command=extrair_matriculas, bootstyle=SUCCESS)
b3.pack(side=LEFT, padx=5, pady=10)

root.mainloop()


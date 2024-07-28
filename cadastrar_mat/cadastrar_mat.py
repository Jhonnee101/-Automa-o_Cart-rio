#Cadastrar apontamentos 
#Ler planilha contendo os dados para ser preenchidos
#Clicar em matriculas
#Clicar em apontamentos
#Clicar em cadastrar apontamentos antigo
#Clicar e digitar o nº da matricula a ser cadastrada
#Selecionar se é averbação ou não
#Clicar e digitar o nº do apontamento
#Clicar em cadastrar apontamento
#Inserir a data
#Colar texto da matricula + Ctrl + A
#Clicar em justificar
#Selecionar fonte courier new
#Selecionar tamanho 16
#Clicar em salvar
#=======================================================================================================#

import time
import pyautogui
import openpyxl as xl 
import tkinter as tk
from tkinter import filedialog, messagebox

# Inicializa a lista de matrículas e o caminho de entrada
matriculas = []
caminho_entrada = ""

# Coordenadas dos elementos da aplicação
cadastrar_apont = {
    'campo_mat': (368, 106),
    'campo_apont': (397, 161),
    'cadastrar_apont': (565, 190),
    'num_mat': (919, 536), # Número da matrícula
    'verif_averb': (971, 564),
    'selecionar_averbação': (952, 604),
    'num_apont': (1047, 604),
    'click_cadastrar': (974, 599)
}

inserir_texto = {
    'campo_data': (685, 323),
    'campo_texto': (663, 533),
    'campo_fonte': (739, 473),
    'fonte_courier': (751, 581),
    'tamanho_16': (833, 473),
    'salvar': (1047, 648)
}

def cadastrar(matricula, num_apont, tipo_de_apont):
    pyautogui.click(cadastrar_apont['campo_mat'])  # Clicar em matrículas
    time.sleep(0.5)
    pyautogui.click(cadastrar_apont['campo_apont']) # Clicar em apontamento
    time.sleep(0.5)
    pyautogui.click(cadastrar_apont['cadastrar_apont']) # Clicar em cadastrar apontamento antigo
    time.sleep(0.5)
    pyautogui.click(cadastrar_apont['num_mat']) # Clicar no campo de matrícula
    pyautogui.typewrite(matricula, interval=0.25) # Digitar o número da matrícula
    time.sleep(0.5)
    
    if tipo_de_apont == "1":
        # Apontamento direto
        pyautogui.click(cadastrar_apont['num_apont'])  # Clicar no campo de apontamento
        pyautogui.typewrite(num_apont, interval=0.25) # Digitar o número do apontamento
    else:
        # Averbação
        pyautogui.click(cadastrar_apont['verif_averb']) # Clicar para verificar se é averbação
        pyautogui.click(cadastrar_apont['selecionar_averbação']) # Selecionar que é averbação
        pyautogui.click(cadastrar_apont['num_apont']) # Clicar no campo de apontamento
        pyautogui.typewrite(num_apont, interval=0.25) # Digitar o número do apontamento

    pyautogui.click(cadastrar_apont['click_cadastrar']) # Clicar em cadastrar apontamento

def inserir_texto(campo_data, campo_texto):
    pyautogui.click(inserir_texto['campo_data'])
    pyautogui.typewrite(campo_data, interval=0.25)
    time.sleep(0.5)
    pyautogui.click(inserir_texto['campo_texto'])
    pyautogui.typewrite(campo_texto, interval=0.25)
    pyautogui.hotkey('ctrl', 'a') # Selecionar todo o texto
    time.sleep(0.5)
    pyautogui.click(inserir_texto['campo_fonte'])
    time.sleep(0.2)
    pyautogui.click(inserir_texto['fonte_courier'])
    time.sleep(0.5)
    pyautogui.click(inserir_texto['tamanho_16'])
    time.sleep(0.5)
    pyautogui.click(inserir_texto['salvar'])
    time.sleep(0.5)

def selecionar_entrada():
    global caminho_entrada
    arquivo = filedialog.askopenfile(title="Selecione a planilha para analisar!")
    if arquivo:
        caminho_entrada = arquivo.name

def extrair_dados(matricula):
    global caminho_entrada
    workbook = xl.load_workbook(caminho_entrada)
    planilha = workbook.active

    for rows in planilha.iter_rows(min_row=2, values_only=True):
        num_apont = rows[0]
        campo_data = rows[1]
        tipo_de_apont = rows[2]
        campo_texto = rows[3]
        
        cadastrar(matricula, num_apont, tipo_de_apont)
        inserir_texto(campo_data, campo_texto)

def iniciar_programa():
    matricula = entrada_matricula.get()
    if not matricula:
        messagebox.showerror("Erro", "Digite o número da matrícula.")
        return
    
    if caminho_entrada == "":
        selecionar_entrada()
    
    if caminho_entrada:
        extrair_dados(matricula)
        messagebox.showinfo("Concluído", "Processo concluído com sucesso!")
    else:
        messagebox.showerror("Erro", "Nenhum arquivo selecionado.")

# Criando a janela de início
janela = tk.Tk()
janela.title("Bot Automatizador")
janela.geometry("400x250")

# Adicionando um rótulo de boas-vindas
label_boas_vindas = tk.Label(janela, text="Bem-vindo ao Bot Automatizador!")
label_boas_vindas.pack(pady=20)

# Campo de entrada para matrícula
label_matricula = tk.Label(janela, text="Número da Matrícula:")
label_matricula.pack(pady=5)
entrada_matricula = tk.Entry(janela)
entrada_matricula.pack(pady=5)

# Botão para iniciar o programa
botao_iniciar = tk.Button(janela, text="Iniciar", command=iniciar_programa)
botao_iniciar.pack(pady=20)

# Executando a interface gráfica
janela.mainloop()

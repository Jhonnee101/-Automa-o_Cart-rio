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
import pyperclip  # Importa o módulo pyperclip
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
    'num_mat': (919, 536),  # Número da matrícula
    'verif_averb': (971, 564),
    'selecionar_averbação': (952, 604),
    'num_apont': (1047, 604),
    'click_cadastrar': (974, 599)
}

inserir_texto = {
    'campo_inserir_data': (685, 323),
    'campo_texto': (663, 533),
    'campo_fonte': (739, 473),
    'fonte_courier': (751, 581),
    'tamanho_16': (833, 473),
    'salvar': (1047, 648)
}

def cadastrar(matricula, numero_apont, tipo_de_apont, inserir_data, campo_texto):
    try:
        # Cadastro do apontamento
        pyautogui.click(cadastrar_apont['campo_mat'])
        time.sleep(0.5)
        pyautogui.write(matricula, interval=0.1)  # Usar write para melhor suporte a caracteres especiais
        time.sleep(0.5)
        
        pyautogui.click(cadastrar_apont['campo_apont'])
        time.sleep(0.5)
        pyautogui.click(cadastrar_apont['cadastrar_apont'])
        time.sleep(0.5)
        pyautogui.click(cadastrar_apont['num_mat'])
        pyautogui.write(matricula, interval=0.1)  # Usar write para melhor suporte a caracteres especiais
        time.sleep(0.5)
        
        if tipo_de_apont == "1":
            pyautogui.click(cadastrar_apont['num_apont'])
            pyautogui.write(numero_apont, interval=0.25)  # Usar write para melhor suporte a caracteres especiais
        else:
            pyautogui.click(cadastrar_apont['verif_averb'])
            pyautogui.click(cadastrar_apont['selecionar_averbação'])
            pyautogui.click(cadastrar_apont['num_apont'])
            pyautogui.write(numero_apont, interval=0.25)  # Usar write para melhor suporte a caracteres especiais

        pyautogui.click(cadastrar_apont['click_cadastrar'])
        time.sleep(1)

        # Inserção de texto
        pyautogui.click(inserir_texto['campo_inserir_data'])
        pyautogui.write(inserir_data, interval=0.25)  # Usar write para melhor suporte a caracteres especiais
        time.sleep(0.5)
        pyautogui.click(inserir_texto['campo_texto'])
        pyperclip.copy(campo_texto)  # Copia o texto para a área de transferência
        pyautogui.hotkey('ctrl', 'v')  # Cola o texto
        #pyautogui.hotkey('ctrl', 'a')
        time.sleep(0.5)
        pyautogui.click(inserir_texto['campo_fonte'])
        time.sleep(0.2)
        pyautogui.click(inserir_texto['fonte_courier'])
        time.sleep(0.5)
        pyautogui.click(inserir_texto['tamanho_16'])
        time.sleep(0.5)
        pyautogui.click(inserir_texto['salvar'])
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao cadastrar e inserir texto: {e}")

def selecionar_entrada():
    global caminho_entrada
    arquivo = filedialog.askopenfile(title="Selecione a planilha para analisar!", filetypes=[("Excel files", "*.xlsx")])
    if arquivo:
        caminho_entrada = arquivo.name

def extrair_dados():
    global caminho_entrada
    try:
        workbook = xl.load_workbook(caminho_entrada)
        planilha = workbook.active

        matricula = entrada_matricula.get()  # Pegando a matrícula
        
        for rows in planilha.iter_rows(min_row=2, values_only=True):
            inserir_data  = str(rows[0]) if rows[0] is not None else ""
            numero_apont  = str(rows[1]) if rows[1] is not None else ""
            tipo_de_apont = str(rows[2]) if rows[2] is not None else ""
            campo_texto   = str(rows[3]) if rows[3] is not None else ""

            print(inserir_data, numero_apont, tipo_de_apont, campo_texto)
            
            cadastrar(matricula, numero_apont, tipo_de_apont, inserir_data, campo_texto)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao extrair dados: {e}")

def iniciar_programa():
    matricula = entrada_matricula.get()
    if not matricula:
        messagebox.showerror("Erro", "Digite o número da matrícula.")
        return
    
    if caminho_entrada == "":
        selecionar_entrada()
    
    if caminho_entrada:
        extrair_dados()
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

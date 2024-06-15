import pyautogui
import time
from openpyxl import Workbook
import pyperclip
from tkinter import messagebox
from tkinter import filedialog
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Inicializa a lista de matrículas
matriculas = []

# Coordenadas dos elementos da aplicação
app_coords = {'campo_montar': (526, 40),'campo_mat': (265, 206), 'buscar_mat': (387, 195), 'campo_copiar': (1239, 75)}

# Função para buscar a matrícula
def buscar_matricula(matricula):
    pyautogui.click(app_coords['campo_montar'])
    time.sleep(0.5)
    pyautogui.click(app_coords['campo_mat'])
    time.sleep(0.3)
    pyautogui.press('backspace')
    time.sleep(0.3)
    pyautogui.typewrite(matricula)
    pyautogui.click(app_coords['buscar_mat'])
    time.sleep(2.5)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.click(app_coords['campo_copiar'])
    time.sleep(0.2)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.4)
    conteudo_copiado = pyperclip.paste()
    return conteudo_copiado

# Função chamada quando o botão Salvar é pressionado
def salvar_matriculas():
    try:
        # Recebe o número inicial da matrícula e a quantidade de matrículas a copiar
        mat = int(entry_mat.get())
        contador = int(entry_quant.get())
        
        # Verifica se os valores são válidos
        if contador <= 0:
            messagebox.showerror("Erro", "A quantidade deve ser maior que zero.")
            return
        
        # Loop para incrementar e salvar as matrículas
        for _ in range(contador):
            mat += 1
            matriculas.append(str(mat))
        
        # Inicia o processo de busca e salvamento
        wb = Workbook()
        ws = wb.active
        conteudos_copiados = []
        time.sleep(2)
        for matricula in matriculas:
            resultado = buscar_matricula(matricula)
            conteudos_copiados.append(resultado)
            ws.append([matricula, resultado])
        
        # Pergunta ao usuário onde salvar o arquivo
        arquivo = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                               filetypes=[("Planilhas do Excel", "*.xlsx"), ("Todos os arquivos", "*.*")])
        if arquivo:  # Se um arquivo foi selecionado
            wb.save(arquivo)
            messagebox.showinfo("Sucesso", "Matrículas salvas com sucesso!")
        else:
            messagebox.showwarning("Cancelado", "Operação de salvamento cancelada.")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, digite números inteiros válidos.")

# Criação da interface gráfica
root = ttk.Window()
style = ttk.Style("vapor")
root.title("Copiar Matrículas v2")
label = ttk.Label(root, text="Copiar Matrículas v2")
label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
label.config(font=('Courier New',16, 'bold'))

# Campo de entrada para matrícula
label_mat = ttk.Label(root, text="Matrícula:")
label_mat.grid(row=1, column=0, padx=10, pady=10)
entry_mat = ttk.Entry(root)
entry_mat.grid(row=1, column=1, padx=10, pady=10)

# Campo de entrada para quantidade
label_quant = ttk.Label(root, text="Quantidade:")
label_quant.grid(row=2, column=0, padx=10, pady=10)
entry_quant = ttk.Entry(root)
entry_quant.grid(row=2, column=1, padx=10, pady=10)

# Botão para salvar matrículas
button_salvar = ttk.Button(root, text="Salvar Matrículas", command=salvar_matriculas, bootstyle=PRIMARY)
button_salvar.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Inicia o loop principal da interface gráfica
root.mainloop()
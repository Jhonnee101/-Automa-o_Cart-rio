import pyautogui
import time
from openpyxl import Workbook
import pyperclip  # Importa a biblioteca pyperclip


# Inicializa o contador e a lista de matrículas
cont = 0
matriculas = []

# Recebe o número inicial da matrícula e a quantidade de matrículas a copiar
mat = int(input("Digite a partir de qual matricula vc quer buscar: "))
contador = int(input("Digite quantas matriculas voce quer copiar: "))

# Loop para incrementar e salvar as matrículas
while cont < contador:
    cont += 1
    mat += 1
    matriculas.append(str(mat))  # Converte o número da matrícula para string

app_coords = {'campo_busca': (359, 365), 'botao_buscar': (937, 386), 'campo_resultado': (480, 403)}

wb = Workbook()
ws = wb.active


def buscar_matricula(matricula):
    time.sleep(2)
    pyautogui.click(app_coords['campo_busca'])
    pyautogui.typewrite(matricula)
    pyautogui.click(app_coords['botao_buscar'])
    

    time.sleep(2)
    

    pyautogui.click(app_coords['campo_resultado'])
    pyautogui.hotkey('ctrl', 'c')
    

    time.sleep(1)
    

    conteudo_copiado = pyperclip.paste()
    return conteudo_copiado


conteudos_copiados = []

for matricula in matriculas:
    resultado = buscar_matricula(matricula)
    conteudos_copiados.append(resultado)  
    ws.append([matricula, resultado])


wb.save('Matriculas.xlsx')




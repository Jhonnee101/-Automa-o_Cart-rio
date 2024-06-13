import pyautogui
import time
from openpyxl import Workbook

# Inicializa o contador e a lista de matrículas
cont = 0
matriculas = []

# Recebe o número31 inicial da matrícula e a quantidade de matrículas a copiar
mat = int(input("Digite a partir de qual matricula vc quer buscar: "))
contador = int(input("Digite quantas matriculas voce quer copiar: "))

# Loop para incrementar e salvar as matrículas
while cont < contador:
    cont += 1
    mat += 1
    matriculas.append(str(mat))  # Converte o número da matrícula para string

# Converte a lista de matrículas em uma tupla
matriculas_tupla = tuple(matriculas)

# Coordenadas dos elementos da interface do aplicativo
app_coords = {'campo_busca': (537, 314), 'botao_buscar': (937, 386), 'campo_resultado': (1708, 322)}

# Inicializa o livro do Excel
wb = Workbook()
ws = wb.active

# Função para buscar e copiar matrícula
def buscar_matricula(matricula):
    time.sleep(2)
    # Clica no campo de busca e digita a matrícula
    pyautogui.click(app_coords['campo_busca'])
    pyautogui.typewrite(matricula)
    pyautogui.click(app_coords['botao_buscar'])
    
    # Espera o resultado ser exibido
    time.sleep(2)
    
    # Clica no campo do resultado e copia o conteúdo
    pyautogui.click(app_coords['campo_resultado'])
    pyautogui.hotkey('ctrl', 'c')
    
    # Espera um pouco para garantir que o texto foi copiado
    time.sleep(1)
    
    # Retorna o conteúdo copiado da área de transferência
    return pyautogui.hotkey('ctrl', 'v')

# Loop para buscar cada matrícula e salvar no Excel
for matricula in matriculas_tupla:
    resultado = buscar_matricula(matricula)
    ws.append([matricula, resultado])

# Salva o arquivo do Excel
wb.save('matriculas.xlsx')

print(matriculas)
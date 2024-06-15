import pyautogui as pg
from time import sleep

sleep(3)  # Pausa a execução por 3 segundos
posicao_mouse = pg.position()  # Obtém a posição atual do mouse
pg.hotkey('ctrl', 'a')
pg.press('backspace')  # Simula a pressão da tecla Enter
pg.press('enter')  # Simula a pressão da tecla Enter
print(posicao_mouse)  # Imprime a posição do mouse


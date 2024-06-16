import pyautogui as pg
from time import sleep

sleep(3) 
posicao_mouse = pg.position()  # Obtém a posição atual do mouse
print(posicao_mouse)  # Imprime a posição do mouse


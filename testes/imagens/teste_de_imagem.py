import pyautogui
import time


imagem = pyautogui.locateOnScreen('testes/imagens/teste5.png')

    # Verifica se a imagem foi encontrada
if imagem:
    print("Imagem encontrada!")
        # Coloque aqui o código que deve ser executado se a imagem for encontrada
else:
    print("Imagem não encontrada.")
        # Coloque aqui o código que deve ser executado se a imagem não for encontrada



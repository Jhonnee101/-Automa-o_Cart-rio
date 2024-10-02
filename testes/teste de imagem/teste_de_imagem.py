import pyautogui
import time

try:
    # Tenta localizar a imagem na tela
    imagem = pyautogui.locateOnScreen('testes/teste de imagem/teste.png')

    # Verifica se a imagem foi encontrada
    if imagem:
        print("Imagem encontrada!")
        # Coloque aqui o código que deve ser executado se a imagem for encontrada
    else:
        print("Imagem não encontrada.")
        # Coloque aqui o código que deve ser executado se a imagem não for encontrada

except pyautogui.ImageNotFoundException:
    print("Erro: A imagem não foi encontrada ou o caminho está incorreto.")

except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")

import pyautogui
import cv2
import time

try:
    imagem = pyautogui.locateOnScreen('testes/imagens/teste.png')
except Exception as e:
    print(f"Erro ao procurar a primeira imagem: {e}")
    imagem = None

try:
    imagem2 = pyautogui.locateOnScreen('testes/imagens/R1-azul.png')
except Exception as e:
    print(f"Erro ao procurar a segunda imagem: {e}")
    imagem2 = None

# Verifica se a primeira imagem foi encontrada
if imagem:
    print("Primeira imagem (R1-branco) encontrada!")
    # Coloque aqui o código que deve ser executado se a primeira imagem for encontrada
else:
    print("Primeira imagem (R1-branco) não encontrada.")

# Verifica se a segunda imagem foi encontrada
if imagem2:
    print("Segunda imagem (R1-azul) encontrada!")
    # Coloque aqui o código que deve ser executado se a segunda imagem for encontrada
else:
    print("Segunda imagem (R1-azul) não encontrada.")
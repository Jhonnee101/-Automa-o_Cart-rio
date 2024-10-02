import pyautogui

# Tenta localizar a imagem na tela
imagem = pyautogui.locateOnScreen('testes/teste de imagem/teste3.png')

# Verifica se a imagem foi encontrada
if imagem is True:
    print("Imagem encontrada!")
    # Coloque aqui o código que deve ser executado se a imagem for encontrada
else:
    print("Imagem não encontrada.")
    # Coloque aqui o código que deve ser executado se a imagem não for encontrada

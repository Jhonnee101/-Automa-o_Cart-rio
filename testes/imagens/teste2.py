import pyautogui

# Função que localiza todas as imagens e retorna as localizadas
def localizar_todas_imagens(lista_imagens):
    imagens_encontradas = {}
    
    for imagem in lista_imagens:
        try:
            # Tentativa de localizar a imagem
            localizacao = pyautogui.locateOnScreen(imagem, confidence=0.8)
            if localizacao:
                imagens_encontradas[imagem] = localizacao
                print(f"Imagem '{imagem}' encontrada!")
            else:
                print(f"Imagem '{imagem}' não encontrada.")
        
        except Exception as e:
            # Captura qualquer exceção e continua com o próximo item da lista
            print(f"Erro ao tentar localizar a imagem '{imagem}': {e}")
    
    return imagens_encontradas  # Retorna um dicionário com as imagens encontradas

# Lista de imagens a procurar
imagens = ['testes/imagens/R1-branco.png', 'testes/imagens/R1-azul.png']

# Chama a função para localizar todas as imagens
imagens_encontradas = localizar_todas_imagens(imagens)

if imagens_encontradas:
    print(f"\nImagens encontradas: {imagens_encontradas}")
else:
    print("Nenhuma imagem encontrada.")

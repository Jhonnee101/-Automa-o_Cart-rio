'''
# VERIRIFICAR SE O ARQUIVO EXISTE,
# SE EXISTIR, SALVAR O Nº DA MATRICULA,
# SE NÃO EXISTIR, SALVAR O NUMERO DA MATRICULA E SOMAR +1 NA QUANTIDADE DE MATRICULAS A VERIFICAR,
'''
import pyautogui
import time

# Função para entrada de dados
def entrada():
    mat = int(input('Digite o número da matrícula: '))
    quantidade = int(input('Digite a quantidade de matrículas a verificar: '))
    return mat, quantidade

# Função para contar matrículas e verificar as imagens
def contador():
    mat_concluidas = 0
    mat_para_fazer = 0
    mat_concluidas_lista = []
    mat_para_fazer_lista = []

    # Lista de imagens a procurar
    lista_imagens = ['testes/imagens/R1-branco.png', 'testes/imagens/R1-azul.png']

    matricula, quantidade = entrada()
    ultima_matricula = matricula + quantidade

    time.sleep(1)

    while matricula < ultima_matricula:
        time.sleep(0.5)

        # Variável para marcar se a matrícula foi concluída
        mat_existe = False
        
        for imagem in lista_imagens:
            try:
                # Tentativa de localizar a imagem
                localizacao = pyautogui.locateOnScreen(imagem, confidence=0.8)
                if localizacao:
                    mat_existe = True
                    break  # Sai do loop ao encontrar a primeira imagem

            except Exception as e:
                # Captura qualquer exceção e continua com a próxima imagem
                print(f"Erro ao tentar localizar a imagem '{imagem}': {e}")

        # Verifica se a matrícula foi concluída
        if mat_existe:
            mat_concluidas += 1
            mat_concluidas_lista.append(matricula)
            print(f'Matrícula {matricula} concluída com sucesso')
        else:
            mat_para_fazer += 1
            mat_para_fazer_lista.append(matricula)
            print(f'Matrícula {matricula} não concluída')

        matricula += 1

    # Exibir os resultados finais
    print("\nResultado final:")
    print(f"Matrículas concluídas: {mat_concluidas_lista}")
    print(f"Matrículas não concluídas: {mat_para_fazer_lista}")
    print(f'Quantidade de matrículas concluídas: {mat_concluidas}')
    print(f'Quantidade de matrículas não concluídas: {mat_para_fazer}')
    
# Executa o contador
contador()



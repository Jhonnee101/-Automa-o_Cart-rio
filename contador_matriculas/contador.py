'''
# VERIRIFICAR SE O ARQUIVO EXISTE,
# SE EXISTIR, SALVAR O Nº DA MATRICULA,
# SE NÃO EXISTIR, SALVAR O NUMERO DA MATRICULA E SOMAR +1 NA QUANTIDADE DE MATRICULAS A VERIFICAR,
'''
import pyautogui
import time

def entrada():
    mat = int(input('Digite o número da matrícula: '))
    quantidade = int(input('Digite a quantidade de matrículas a verificar: '))
    return mat, quantidade

def contador():
    mat_concluidas = 0
    mat_concluidas_lista = []
    mat_para_fazer = 0
    mat_para_fazer_lista = []
    
    matricula, quantidade = entrada()
    ultima_matricula = matricula + quantidade

    time.sleep(1)

    while matricula < ultima_matricula:
        #pyautogui.click(100, 100)
        #pyautogui.write(str(matricula))
        #pyautogui.press('enter')
        time.sleep(0.5)
        try:
            mat_existe = pyautogui.locateOnScreen('testes/imagens/teste6.png')

            if mat_existe:
                mat_concluidas += 1
                mat_concluidas_lista.append(matricula)
                print(f'Matrícula {matricula} concluída')
                print("Imagem encontrada!")


        except Exception:
            mat_para_fazer += 1
            mat_para_fazer_lista.append(matricula)
            print(f'Matrícula {matricula} não concluída')
            print("Imagem não encontrada!")
            pass
        
        matricula += 1

    # Exibir os resultados finais
    print("\nResultado final:")
    print(f"Matrículas concluídas: {mat_concluidas_lista}")
    print(f"Matrículas não concluídas: {mat_para_fazer_lista}")

contador()


'''
# VERIRIFICAR SE O ARQUIVO EXISTE,
# SE EXISTIR, SALVAR O Nº DA MATRICULA,
# SE NÃO EXISTIR, SALVAR O NUMERO DA MATRICULA E SOMAR +1 NA QUANTIDADE DE MATRICULAS A VERIFICAR,
'''
import pyautogui
import time


def entrada():
    mat = int(input('Digite o número da matricula: '))
    quantidade = int(input('Digite a quantidade de matriculas a verificar: '))
    return mat, quantidade

def contador():
    mat_concluidas = 0
    mat_para_fazer = 0
    matricula, quantidade = entrada()
    ultima_matricula = matricula+quantidade

    time.sleep(1)

    while matricula < ultima_matricula:
        pyautogui.click(100, 100)
        pyautogui.write(str(matricula))
        pyautogui.press('enter')
        time.sleep(0.5)
        mat_existe = pyautogui.locateOnScreen('matricula_existe.png')
        mat_nao_existe = pyautogui.locateOnScreen('matricula_nao_existe.png')
        if mat_existe is True:
            mat_concluidas += 1
        
        if mat_nao_existe is True:
            mat_para_fazer += 1
            #pyautogui.press('enter') verificar qual dos dois
            #pyautogui.clic(100, 100)

        print(contador)

contador()

import PySimpleGUI as sg

sg.theme("Reddit")
layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario')],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*')],
    [sg.Checkbox("Salvar Senha?")],
    [sg.Button("Entrar")]  # Adicionei um botão chamado "Entrar"
]

janela = sg.Window("Tela de Login", layout)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break

    if eventos == "Entrar":  # Verifica se o botão "Entrar" foi pressionado
        if valores["usuario"] == 'jhonatan' and valores["senha"] == "1234":
            print("Bem-vindo!")
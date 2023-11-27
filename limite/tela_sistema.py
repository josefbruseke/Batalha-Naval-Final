import PySimpleGUI as sg

class TelaSistema:
    def __init__(self) -> None:
        sg.theme("DarkAmber")

    def mostra_opcoes(self):
        layout = [
            [sg.Text('MENU INICIAL')],
            [sg.Text('Selecione a opção desejada')],
            [sg.Button('Login', key='1', size=(20, 2))],
            [sg.Button('Cadastro', key='2', size=(20, 2))],
            [sg.Button('Ranking', key='3', size=(20, 2))],
            [sg.Button('Encerrar o sistema', key='0', size=(20, 2))],
        ]

        window = sg.Window('Menu Inicial', layout, size=(400, 300), grab_anywhere=True, element_justification='center')

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED or event == '0':
                return 0

            if event in ['1', '2', '3']:
                window.close()
                return int(event)

    def confirma_encerramento(self):
        layout = [
            [sg.Text('Deseja realmente encerrar o sistema?')],
            [sg.Button('Sim'), sg.Button('Não')]
        ]

        window = sg.Window('Confirmação', layout)

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED or event == 'Não':
                window.close()
                return False

            if event == 'Sim':
                window.close()
                return True



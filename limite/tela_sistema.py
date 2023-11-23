"""class TelaSistema:
    def mostra_opcoes(self):
        print("------MENU INICIAL------")
        print("Selecione a opção desejada")
        print("1 - Login")
        print("2 - Cadastro")
        print("3 - Ranking")
        print("0 - Encerrar o sistema")
        opcao = int(input("Escolha a opção: "))
        return opcao

    def mostra_mensagem(self, msg):
        print(msg)
        
"""

import PySimpleGUI as sg

class TelaSistema:
    def mostra_opcoes(self):
        sg.theme('DarkBlue')

        layout = [
            [sg.Text('------MENU INICIAL------')],
            [sg.Text('Selecione a opção desejada')],
            [sg.Button('Login', key='1')],
            [sg.Button('Cadastro', key='2')],
            [sg.Button('Ranking', key='3')],
            [sg.Button('Encerrar o sistema', key='0')],
        ]

        window = sg.Window('Menu Inicial', layout, size=(600, 400), grab_anywhere=True)

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED:
                break

            if event in ['1', '2', '3', '0']:
                window.close()
                return int(event)

        window.close()


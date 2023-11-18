"""class TelaSistema:
    def mostra_opcoes(self):
        print("------Batalha Naval------")
        print("Selecione a opção desejada")
        print("1 - Fazer Login")
        print("2 - Fazer Cadastro")
        print("3 - Remover Cadastro")
        print("0 - Encerrar o sistema")
        opcao = int(input("Escolha a opção: "))
        return opcao
"""

import PySimpleGUI as sg

class TelaSistema:
    def mostra_opcoes(self):
        sg.theme('DarkBlue')
        layout = [
            [sg.Text('------Batalha Naval------')],
            [sg.Text('Selecione a opção desejada')],
            [sg.Button('Fazer Login')],
            [sg.Button('Fazer Cadastro')],
            [sg.Button('Remover Cadastro')],
            [sg.Button('Alterar Cadastro')],
            [sg.Button('Encerrar o sistema')],
        ]

        window = sg.Window('Batalha Naval', layout)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Fazer Login':
                window.close()
                return 1
            elif event == 'Fazer Cadastro':
                window.close()
                return 2
            elif event == 'Remover Cadastro':
                window.close()
                return 3
            elif event == 'Alterar Cadastro':
                window.close()
                return 4
            elif event == 'Encerrar o sistema':
                window.close()
                return 0

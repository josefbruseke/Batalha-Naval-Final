import PySimpleGUI as sg

class TelaOceano:
    def __init__(self):
        sg.theme('DarkAmber')

    def recebe_tamanho(self):
        layout = [
            [sg.Text('Digite o tamanho do oceano:'), sg.Input(key='-TAMANHO-')],
            [sg.Button('OK'), sg.Button('Voltar')],
        ]

        window = sg.Window('Tamanho do Oceano', layout, auto_size_text=True, auto_size_buttons=True, element_justification='center')

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED:
                window.close()
                return 'Fechar'
            
            if event == 'Voltar':
                window.close()
                return 'Voltar'
    
            if event == 'OK':
                try:
                    tamanho = int(values['-TAMANHO-'])
                    window.close()
                    return tamanho
                except ValueError:
                    sg.popup_error("Digite um número válido para o tamanho do oceano")


    def mostra_oceano_jogador(self):
        pass

    def mostra_oceano_computador(self):
        pass

    def mostra_mensagem(self, msg):
        sg.popup(msg)

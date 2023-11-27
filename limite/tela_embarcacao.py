import PySimpleGUI as sg

class TelaEmbarcacao:
    def mostra_embarcacoes(self):
        sg.popup('Embarcações:', 'Porta-Aviões (P) - Tamanho: 7', 'Fragata (F) - Tamanho: 10',
                 'Submarino (S) - Tamanho: 4', 'Bote (B) - Tamanho: 20')

    def recebe_posicao_embarcacao(self):
        sg.theme('DarkAmber')
        layout = [
            [sg.Text('Informe a posição para inserir o barco:')],
            [sg.Text('Linha:'), sg.Input(key='-LINHA-')],
            [sg.Text('Coluna:'), sg.Input(key='-COLUNA-', size=(5, 1))],
            [sg.Button('Inserir Barco')],
        ]

        window = sg.Window('Posição do Barco', layout, auto_size_text=True, auto_size_buttons=True)

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED:
                window.close()
                return None

            if event == 'Inserir Barco':
                linha = int(values['-LINHA-'])
                coluna = values['-COLUNA-'].upper()
                window.close()
                return linha, coluna
             
    def mostra_embarcacoes_disponiveis(self, embarcacoes):
        sg.popup('Embarcações disponíveis:', ', '.join(embarcacoes))

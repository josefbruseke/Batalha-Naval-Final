"""class TelaOceano:
   
    def recebe_tamanho(self):
        print("-----TAMANHO DO OCEANO-----")
        tamanho = int(input("Informe o tamanho do oceano da partida: "))
        return tamanho
        
    def mostra_oceano_jogador(self):
        pass
    
    def mostra_oceano_computador(self):
        pass
    
    def mostra_mensagem(self, msg):
        print(msg)
        """
        
import PySimpleGUI as sg

class TelaOceano:
    def __init__(self):
        sg.theme('DarkAmber')

    def recebe_tamanho(self):
        print("inicia tamanho oceano")
        layout = [
            [sg.Text('Digite o tamanho do oceano:'), sg.Input(key='-TAMANHO-')],
            [sg.Button('OK')],
        ]


        window = sg.Window('Tamanho do Oceano', layout, auto_size_text=True, auto_size_buttons=True)

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED:
                window.close()
                return None

            if event == 'OK':
                tamanho = int(values['-TAMANHO-'])
                window.close()
                return tamanho

    def mostra_oceano_jogador(self):
        pass

    def mostra_oceano_computador(self):
        pass

    def mostra_mensagem(self, msg):
        sg.popup(msg)

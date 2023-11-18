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
        print(msg)"""
        
import PySimpleGUI as sg

class TelaOceano:
   
    def recebe_tamanho(self):
        layout = [
            [sg.Text('-----TAMANHO DO OCEANO-----')],
            [sg.Text('Informe o tamanho do oceano da partida:'), sg.Input(key='-TAMANHO-')],
            [sg.Button('OK')],
        ]

        window = sg.Window('Tamanho do Oceano', layout)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'OK':
                tamanho = int(values['-TAMANHO-'])
                window.close()
                return tamanho

    def mostra_oceano_jogador(self, oceano_jogador):
        pass
    
    def mostra_oceano_computador(self, oceano_computador):
        pass
    
    def mostra_mensagem(self, msg):
        sg.popup(msg)

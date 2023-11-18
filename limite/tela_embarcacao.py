from entidade.oceano import Oceano
'''
class TelaEmbarcacao:
    def mostra_embarcacoes(self):
       embarcacoes = Oceano.embarcacoes()
       return embarcacoes 
    
    def recebe_posicao_embarcacao(self):
        print("Informe a posição para inserir o barco: ")
        linha = int(input("Linha: "))
        coluna = input("Coluna: ").upper()
        return linha, coluna
            
    def mostra_embarcacoes_disponiveis(self, embarcacoes):
        pass'''
        
import PySimpleGUI as sg

class TelaEmbarcacao:
    def mostra_embarcacoes(self):
        embarcacoes = Oceano.embarcacoes()
        return embarcacoes 
    
    def recebe_posicao_embarcacao(self):
        layout = [
            [sg.Text('Informe a posição para inserir o barco:')],
            [sg.Text('Linha:'), sg.Input(key='-LINHA-')],
            [sg.Text('Coluna:'), sg.Input(key='-COLUNA-')],
            [sg.Button('OK')],
        ]

        window = sg.Window('Posição do Barco', layout)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'OK':
                linha = int(values['-LINHA-'])
                coluna = values['-COLUNA-'].upper()
                window.close()
                return linha, coluna
            
    def mostra_embarcacoes_disponiveis(self, embarcacoes):
        pass

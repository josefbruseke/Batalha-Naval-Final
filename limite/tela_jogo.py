"""class TelaJogo:
    def recebe_login(self):
        print("------LOGIN-------")
        recebe_nome = input("Digite seu nome: ")
        recebe_senha = input("Digite sua senha: ")
        return{"recebe_nome": recebe_nome, "recebe_senha": recebe_senha}

    def mostra_resultado_jogo(self):
        pass

    def mostra_resultado_rodada(self, jogador, resultado):
        print(f"{jogador} {resultado} o tiro")

    def mostra_opcoes(self):
        print("------MENU JOGO------")
        print("Selecione a opção desejada")
        print("1 - Iniciar partida")
        print("2 - Ver ranking")
        print("0 - Voltar")
        opcao = int(input("Escolha a opção: "))
        return opcao


    def mostra_mensagem(self, msg):
        print(msg)

    def voltar(self):
        opcao = input("Deseja voltar? [S/N]").upper()
        return opcao"""
        
import PySimpleGUI as sg

class TelaJogo:
    def __init__(self):
        sg.theme('DarkBlue')

    def recebe_login(self):
        layout = [
            [sg.Text('------LOGIN-------')],
            [sg.Text('Digite seu nome:'), sg.Input(key='-NOME-')],
            [sg.Text('Digite sua senha:'), sg.Input(key='-SENHA-', password_char='*')],
            [sg.Button('Login')],
        ]

        window = sg.Window('Login', layout)

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED:
                break

            if event == 'Login':
                nome = values['-NOME-']
                senha = values['-SENHA-']
                window.close()
                return {"recebe_nome": nome, "recebe_senha": senha}

    def mostra_resultado_jogo(self):
        pass

    def mostra_resultado_rodada(self, jogador, resultado):
        sg.popup(f"{jogador} {resultado} o tiro")

    def mostra_opcoes(self):
        layout = [
            [sg.Text('------MENU JOGO------')],
            [sg.Text('Selecione a opção desejada')],
            [sg.Button('Iniciar partida')],
            [sg.Button('Ver ranking')],
            [sg.Button('Voltar')],
        ]

        window = sg.Window('Menu Jogo', layout)

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED:
                break

            if event == 'Iniciar partida':
                window.close()
                return 1
            elif event == 'Ver ranking':
                window.close()
                return 2
            elif event == 'Voltar':
                window.close()
                return 0

    def mostra_mensagem(self, msg):
        sg.popup(msg)

    def voltar(self):
        opcao = sg.popup_yes_no('Deseja voltar?')
        return opcao == 'Yes'
        
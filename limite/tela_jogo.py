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
        print("---------------------")
        opcao = int(input("Escolha a opção: "))
        return opcao

    def mostra_resultados(self, duracao, vencedor, pontuacao_jogador, pontuacao_computador):
        print("------RESULTADOS------")
        print(f"Duração da partida: {duracao}")
        print(f"O vencedor da partida foi o: {vencedor}")
        print(f"Pontuação do jogador: {pontuacao_jogador}")
        print(f"Pontuação do computador: {pontuacao_computador}")
        print("---------------------")
    
    def mostra_opcoes_final(self):
        print("------------------------------")
        print("Selecione a sua opção final:")
        print("1 - Iniciar um novo jogo")
        print("2 - Voltar para o Menu Jogo")
        print("0 - Encerrar o sistema")
        print("------------------------------")
        opcao = int(input("Escolhe a opção: "))
        return opcao

    def mostra_mensagem(self, msg):
        print(msg)

    def voltar(self):
        opcao = input("Deseja voltar para o meu inicial? [S/N] ").upper()
        return opcao
        
"""

import PySimpleGUI as sg

class TelaJogo:
    def recebe_login(self):
        sg.theme('DarkBlue')
        layout = [
            [sg.Text('------LOGIN------')],
            [sg.Text('Digite seu nome:'), sg.Input(key='-NOME-')],
            [sg.Text('Digite sua senha:'), sg.Input(key='-SENHA-', password_char='*')],
            [sg.Button('Login')],
        ]

        window = sg.Window('Login', layout)

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED:
                window.close()
                return None

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
        sg.theme('DarkBlue')
        layout = [
            [sg.Text('------MENU JOGO------')],
            [sg.Text('Selecione a opção desejada')],
            [sg.Button('Iniciar Partida')],
            [sg.Button('Ver Ranking')],
            [sg.Button('Voltar')],
        ]

        window = sg.Window('Menu Jogo', layout)

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED:
                window.close()
                return 0

            if event == 'Iniciar Partida':
                window.close()
                return 1

            if event == 'Ver Ranking':
                window.close()
                return 2

            if event == 'Voltar':
                window.close()
                return 0

    def mostra_resultados(self, duracao, vencedor, pontuacao_jogador, pontuacao_computador):
        sg.popup(
            f"------RESULTADOS------\n"
            f"Duração da partida: {duracao}\n"
            f"O vencedor da partida foi o: {vencedor}\n"
            f"Pontuação do jogador: {pontuacao_jogador}\n"
            f"Pontuação do computador: {pontuacao_computador}\n"
            "---------------------"
        )

    def mostra_opcoes_final(self):
        sg.theme('DarkBlue')
        layout = [
            [sg.Text('------------------------------')],
            [sg.Text('Selecione a sua opção final:')],
            [sg.Button('Iniciar Novo Jogo')],
            [sg.Button('Voltar para o Menu Jogo')],
            [sg.Button('Encerrar o Sistema')],
        ]

        window = sg.Window('Opções Finais', layout)

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED:
                window.close()
                return 0

            if event == 'Iniciar Novo Jogo':
                window.close()
                return 1

            if event == 'Voltar para o Menu Jogo':
                window.close()
                return 2

            if event == 'Encerrar o Sistema':
                window.close()
                return 0

    def mostra_mensagem(self, msg):
        sg.popup(msg)

    def voltar(self):
        opcao = sg.popup_get_text('Deseja voltar para o menu inicial? (S/N)').upper()
        return opcao

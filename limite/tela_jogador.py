"""class TelaJogador:
    def recebe_cadastro(self):
        print("------REALIZA CADASTRO------")
        nome = input("Digite seu nome: ")
        data_nascimento = input("Digite sua data de nascimento (DD/MM/AAAA): ")
        senha = input("Digite a senha: ")
        return {"nome": nome, "data_nascimento": data_nascimento, "senha": senha}
    
    def seleciona_jogador(self):
        print("------CADASTRO------")
        nome = input("Digite o nome do Jogador: ")
        senha = input("Digite a senha: ")
        return {"nome": nome, "senha": senha}
    
    def opcoes_cadastro(self):
        print("------CADASTRO------")
        print("Selecione a opção desejada")
        print("1 - Fazer Cadastro")
        print("2 - Alterar Cadastro")
        print("3 - Remover Cadastro")
        print("0 - Voltar")
        print("--------------------")
        opcao = int(input("Escolha a opção: "))
        return opcao



    def mostra_historico(self):
        pass

    def mostra_pontuacao(self):
        pass
    
    def mostra_lista_jogadores(self):
        pass
 
    def mostra_mensagem(self, msg):
        print(msg)
"""

import PySimpleGUI as sg

class TelaJogador:
    def recebe_cadastro(self):
        sg.theme('DarkBlue')
        layout = [
            [sg.Text('------REALIZA CADASTRO------')],
            [sg.Text('Digite seu nome:'), sg.Input(key='-NOME-')],
            [sg.Text('Digite sua data de nascimento (DD/MM/AAAA):'), sg.Input(key='-DATA_NASCIMENTO-')],
            [sg.Text('Digite a senha:'), sg.Input(key='-SENHA-', password_char='*')],
            [sg.Button('Cadastrar')],
        ]

        window = sg.Window('Cadastro', layout)

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED:
                window.close()
                return None

            if event == 'Cadastrar':
                nome = values['-NOME-']
                data_nascimento = values['-DATA_NASCIMENTO-']
                senha = values['-SENHA-']
                window.close()
                return {"nome": nome, "data_nascimento": data_nascimento, "senha": senha}

    def seleciona_jogador(self):
        sg.theme('DarkBlue')
        layout = [
            [sg.Text('------SELECIONA JOGADOR------')],
            [sg.Text('Digite o nome do Jogador:'), sg.Input(key='-NOME-')],
            [sg.Text('Digite a senha:'), sg.Input(key='-SENHA-', password_char='*')],
            [sg.Button('Selecionar Jogador')],
        ]

        window = sg.Window('Selecionar Jogador', layout)

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED:
                window.close()
                return None

            if event == 'Selecionar Jogador':
                nome = values['-NOME-']
                senha = values['-SENHA-']
                window.close()
                return {"nome": nome, "senha": senha}

    def opcoes_cadastro(self):
        sg.theme('DarkBlue')
        layout = [
            [sg.Text('------CADASTRO------')],
            [sg.Text('Selecione a opção desejada')],
            [sg.Button('Fazer Cadastro')],
            [sg.Button('Alterar Cadastro')],
            [sg.Button('Remover Cadastro')],
            [sg.Button('Voltar')],
        ]

        window = sg.Window('Opções de Cadastro', layout)

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED:
                window.close()
                return 0

            if event == 'Fazer Cadastro':
                window.close()
                return 1

            if event == 'Alterar Cadastro':
                window.close()
                return 2

            if event == 'Remover Cadastro':
                window.close()
                return 3

            if event == 'Voltar':
                window.close()
                return 0

    def mostra_historico(self):
        sg.popup('Histórico não disponível.')

    def mostra_pontuacao(self):
        sg.popup('Pontuação não disponível.')

    def mostra_lista_jogadores(self):
        sg.popup('Lista de jogadores não disponível.')

    def mostra_mensagem(self, msg):
        sg.popup(msg)


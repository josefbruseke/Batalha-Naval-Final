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

    def opcoes_alteracao(self):
        print("-------ALTERAÇÃO-------")
        print("1 - Alterar senha")
        print("2 - Alterar nome")
        print("3 - Alterar data de nascimento")
        print("0 - voltar")
        print("-----------------------")
        opcao = int(input("Escolha a opção: "))
        return opcao
    
    def recebe_nova_senha(self):
        nova_senha = input("Digite sua nova senha: ")
        return nova_senha
    
    def recebe_novo_nome(self):
        novo_nome = input("Digite seu novo nome: ")
        return novo_nome

    def recebe_nova_data_nascimento(self):
        nova_data_nascimento = input("Digite sua nova data_de_nascimento: ")
        return nova_data_nascimento

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
            [sg.Text('Digite seu nome, sua data de nascimento e sua senha.')],
            [sg.Text('Digite seu nome:', size=(35, 1)), sg.Input(key='-NOME-')],
            [sg.Text('Digite sua data de nascimento (DD/MM/AAAA):',size=(35, 1)), sg.Input(key='-DATA_NASCIMENTO-')],
            [sg.Text('Digite a senha:', size=(35, 1)), sg.Input(key='-SENHA-', password_char='*')],
            [sg.Button('Cadastrar', size=(30, 1))],
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

    def opcoes_alteracao(self):
        sg.theme('DarkBlue')
        layout = [
            [sg.Text('------CADASTRO------')],
            [sg.Text('Selecione a opção desejada')],
            [sg.Button('Alterar Senha')],
            [sg.Button('Alterar Nome')],
            [sg.Button('Alterar Data de Nascimento')],
            [sg.Button('Voltar')],
        ]

        window = sg.Window('Alterar Cadastro', layout)

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED:
                window.close()
                return 0
            if event == 'Alterar Senha':
                window.close()
                return 1
            if event == 'Alterar Nome':
                window.close()
                return 2
            if event == 'Alterar Data de Nascimento':
                window.close()
                return 3
            if event == 'Voltar':
                window.close()
                return 0
            
    def recebe_nova_senha(self):
        layout = [
            [sg.Text('Digite a nova senha:'), sg.Input(key='-SENHA-')],
            [sg.Button('OK')],
        ]

        window = sg.Window('Jogo', layout)

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED:
                window.close()
                return None

            if event == 'OK':
                senha = values['-SENHA-']
                window.close()
                return senha

    def recebe_novo_nome(self):
        layout = [
            [sg.Text('Digite o novo nome:'), sg.Input(key='-NOME-')],
            [sg.Button('OK')],
        ]

        window = sg.Window('Jogo', layout)

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED:
                window.close()
                return None

            if event == 'OK':
                nome = values['-NOME-']
                window.close()
                return nome

    def recebe_nova_data_nascimento(self):
        layout = [
            [sg.Text('Digite a nova data de nascimento:'), sg.Input(key='-DATA-DE-NASCIMENTO-')],
            [sg.Button('OK')],
        ]

        window = sg.Window('Jogo', layout)

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED:
                window.close()
                return None

            if event == 'OK':
                data_de_nascimento = values['-DATA-DE-NASCIMENTO-']
                window.close()
                return data_de_nascimento
   
    def mostra_pontuacao(self):
        sg.popup('Pontuação não disponível.')


    def mostra_mensagem(self, msg):
        sg.popup(msg)
    
    def mostra_ranking(self, jogadores_ordenados):
        dados_tabela = [[jogador.nome, jogador.pontuacao] for jogador in jogadores_ordenados]
        layout = [
            [sg.Table(values=dados_tabela,
                      headings=['Nome', 'Pontuação'],
                      auto_size_columns=False,
                      justification='right',
                      display_row_numbers=False,
                      num_rows=min(25, len(dados_tabela)),
                      key='-TABLE-')],
            [sg.Button('Fechar')]
        ]
        window = sg.Window('Ranking', layout)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Fechar':
                break
        window.close()

    def mostra_lista_jogadores(self, jogadores):
        layout = [
            [sg.Table(values=jogadores,
                      headings=['Nome'],
                      auto_size_columns=False,
                      justification='right',
                      display_row_numbers=False,
                      num_rows=min(25, len(jogadores)),
                      key='-TABLE-')],
            [sg.Button('Fechar')]
        ]
        window = sg.Window('Lista jogadores', layout)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Fechar':
                break
        window.close()


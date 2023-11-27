import PySimpleGUI as sg

class TelaJogador:
    def recebe_cadastro(self):
        sg.theme('DarkAmber')
        layout = [
            [sg.Text('Digite seu nome, sua data de nascimento e sua senha.')],
            [sg.Text('Digite seu nome:', size=(35, 1)), sg.Input(key='-NOME-')],
            [sg.Text('Digite sua data de nascimento (DD/MM/AAAA):',size=(35, 1)), sg.Input(key='-DATA_NASCIMENTO-')],
            [sg.Text('Digite a senha:', size=(35, 1)), sg.Input(key='-SENHA-', password_char='*')],
            [sg.Button('Cadastrar', size=(30, 1))],
        ]

        window = sg.Window('Cadastro', layout, auto_size_text=True, auto_size_buttons=True, element_justification='center')

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

    def abre_login(self):
        sg.theme('DarkAmber')
        layout = [
            [sg.Text('LOGIN')],
            [sg.Text('Digite seu nome: '), sg.Input(key='-NOME-')],
            [sg.Text('Digite sua senha:'), sg.Input(key='-SENHA-', password_char='*')],
            [sg.Button('Entrar'), sg.Button('Voltar')],
        ]

        window = sg.Window('Login', layout, auto_size_text=True, auto_size_buttons=True, element_justification='center')

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED:
                return 'Encerrar Sistema'
            
            elif event == 'Voltar':
                window.close()
                return 'Voltar'

            if event == 'Entrar':
                nome = values['-NOME-']
                senha = values['-SENHA-']
                window.close()
                return {"recebe_nome": nome, "recebe_senha": senha}
            

    def opcoes_cadastro(self):
        sg.theme('DarkAmber')
        layout = [
            [sg.Text('CADASTRO')],
            [sg.Text('Selecione a opção desejada')],
            [sg.Button('Fazer Cadastro'  , size=(20, 2))],
            [sg.Button('Alterar Cadastro', size=(20, 2))],
            [sg.Button('Remover Cadastro', size=(20, 2))],
            [sg.Button('Voltar', size=(20, 2))],
        ]

        window = sg.Window('Opções de Cadastro', layout, auto_size_text=True, auto_size_buttons=True, element_justification='center')

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
        sg.theme('DarkAmber')
        layout = [
            [sg.Text('------CADASTRO------')],
            [sg.Text('Selecione a opção desejada', size=(20, 2))],
            [sg.Button('Alterar Senha', size=(20, 2))],
            [sg.Button('Alterar Nome', size=(20, 2))],
            [sg.Button('Alterar Data de Nascimento', size=(20, 2))],
            [sg.Button('Voltar', size=(20, 2))],
        ]

        window = sg.Window('Alterar Cadastro', layout, element_justification='center')

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

        window = sg.Window('Jogo', layout, auto_size_text=True, auto_size_buttons=True, element_justification='center')


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
            [sg.Text('Digite a nova data de nascimento: (DD/MM/AAAA)'), sg.Input(key='-DATA-DE-NASCIMENTO-')],
            [sg.Button('OK')],
        ]

        window = sg.Window('Jogo', layout, auto_size_text=True, auto_size_buttons=True, element_justification='center')

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
        window = sg.Window('Ranking', layout, auto_size_text=True, auto_size_buttons=True)
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


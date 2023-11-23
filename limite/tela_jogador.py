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

    def mostra_historico(self):
        sg.popup('Histórico não disponível.')

    def mostra_pontuacao(self):
        sg.popup('Pontuação não disponível.')

    def mostra_lista_jogadores(self):
        sg.popup('Lista de jogadores não disponível.')

    def mostra_mensagem(self, msg):
        sg.popup(msg)
    
    def mostra_ranking(self, jogadores_ordenados):
        dados_tabela = [[jogador.nome, jogador.pontuacao] for jogador in jogadores_ordenados]

        # Criar layout para a interface gráfica com a tabela
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

        # Criar janela
        window = sg.Window('Ranking', layout)

        # Loop de evento para interagir com a interface gráfica
        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED or event == 'Fechar':
                break

        # Fechar a janela ao sair do loop
        window.close()



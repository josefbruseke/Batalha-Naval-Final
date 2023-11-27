import PySimpleGUI as sg

class TelaJogo:
    def recebe_login(self):
        sg.theme('DarkAmber')
        layout = [
            [sg.Text('LOGIN')],
            [sg.Text('Digite seu nome:'), sg.Input(key='-NOME-')],
            [sg.Text('Digite sua senha:'), sg.Input(key='-SENHA-', password_char='*')],
            [sg.Button('Login'), sg.Button('Voltar')],
        ]

        window = sg.Window('Login', layout, auto_size_text=True, auto_size_buttons=True, element_justification='center')

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED:
                return 'Encerrar Sistema'
            
            elif event == 'Voltar':
                window.close()
                return 'Voltar'

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
        sg.theme('DarkAmber')
        layout = [
            [sg.Text('MENU JOGO')],
            [sg.Text('Selecione a opção desejada')],
            [sg.Button('Iniciar Partida', size=(20, 2))],
            [sg.Button('Histórico jogador', size=(20, 2))],
            [sg.Button('Histórico geral', size=(20, 2))],
            [sg.Button('Voltar', size=(20, 2))],
        ]

        window = sg.Window('Menu Jogo', layout, auto_size_text=True, auto_size_buttons=True, element_justification='center')

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED:
                window.close()
                return 0

            if event == 'Iniciar Partida':
                window.close()
                return 1

            if event == 'Histórico jogador':
                window.close()
                return 2
            
            if event == 'Histórico geral':
                window.close()
                return 3

            if event == 'Voltar':
                window.close()
                return 0
                
    def mostra_historico_geral(self, historico_geral):
        dados_tabela = [[jogo.id, jogo.data, jogo.duracao, jogo.jogador.nome, jogo.vencedor, jogo.pontuacao_partida] for jogo in historico_geral]

        # Criar layout para a interface gráfica com a tabela
        layout = [
            [sg.Table(values=dados_tabela,
                    headings=['ID', 'Data', 'Duração', 'Jogador', 'Vencedor', 'Pontuação'],
                    auto_size_columns=False,
                    justification='right',
                    display_row_numbers=False,
                    num_rows=min(25, len(dados_tabela)),
                    key='-TABLE-')],
            [sg.Button('Fechar')]
        ]

        # Criar janela
        window = sg.Window('Histórico Geral', layout, auto_size_text=True, auto_size_buttons=True, element_justification='center')

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED or event == 'Fechar':
                break

        # Fechar a janela ao sair do loop
        window.close()
    
    def mostra_historico_jogador(self, jogos_jogador):
        dados_tabela = [[jogo.id, jogo.data, jogo.duracao, jogo.jogador.nome, jogo.vencedor, jogo.pontuacao_partida] for jogo in jogos_jogador]

        # Criar layout para a interface gráfica com a tabela
        layout = [
            [sg.Table(values=dados_tabela,
                    headings=['ID', 'Data', 'Duração', 'Jogador', 'Vencedor', 'Pontuação'],
                    auto_size_columns=False,
                    justification='right',
                    display_row_numbers=False,
                    num_rows=min(25, len(dados_tabela)),
                    key='-TABLE-')],
            [sg.Button('Fechar')]
        ]

        # Criar janela
        window = sg.Window('Histórico do Jogador', layout, auto_size_text=True, auto_size_buttons=True)

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED or event == 'Fechar':
                break
        # Fechar a janela ao sair do loop
        window.close()

    def mostra_resultados(self, duracao, vencedor, pontuacao_jogador, pontuacao_computador):
        sg.popup(
            f"------RESULTADOS------\n"
            f"Duração da partida: {duracao}\n"
            f"O vencedor da partida foi o: {vencedor}\n"
            f"Pontuação do jogador: {pontuacao_jogador}\n"
            f"Pontuação do computador: {pontuacao_computador}\n"
        )

    def mostra_opcoes_final(self):
        sg.theme('DarkAmber')
        layout = [
            [sg.Text('------------------------------')],
            [sg.Text('Selecione a sua opção final:')],
            [sg.Button('Iniciar Novo Jogo', size=(20, 2))],
            [sg.Button('Voltar para o Menu Jogo', size=(20, 2))],
            [sg.Button('Encerrar o Sistema', size=(20, 2))],
        ]

        window = sg.Window('Opções Finais', layout, size=(600, 400), auto_size_text=True, auto_size_buttons=True, element_justification='center')

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
    
    def imprimir_tabuleiro(self, tamanho, oceano, embarcacao):
        print("inicia imprimir tabuleiro")
        letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        layout = []

        # Cabeçalho das colunas
        layout.append([sg.Text("   " + " ".join(letras[:tamanho]))])

        for i, linha in enumerate(oceano):
            # Número da linha
            linha_layout = [sg.Text("{:2} ".format(i))]
            
            for posicao in linha:
                if isinstance(posicao, embarcacao):
                    linha_layout.append(sg.Text(posicao.sigla, size=(2, 1)))
                else:
                    linha_layout.append(sg.Text(posicao, size=(2, 1)))

            layout.append(linha_layout)

        # Letras das colunas no final
        layout.append([sg.Text("  " + "  ".join(letras[:tamanho]))])

        # Adicione um botão "Continuar"
        layout.append([sg.Button("Continuar")])

        # Crie a janela
        window = sg.Window('Tabuleiro', layout)
        event, values = window.read()
        if event == "Continuar":
            window.close()

    def layout_tabuleiro(self, tamanho, oceano, embarcacao):
        letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        layout_tabuleiro = []

        # Adiciona a linha de letras (coordenadas das colunas)
        header = [sg.Text(" ", size=(2, 1))] + [sg.Text(letra, size=(3, 1), justification='center') for letra in letras[:tamanho]]
        layout_tabuleiro.append(header)

        for i in range(tamanho):
            linha_layout = [sg.Text(str(i), size=(2, 1))]

            for j in range(tamanho):
                posicao = oceano[i][j]

                # Cria um botão para cada posição
                button = sg.Button(posicao.sigla if isinstance(posicao, embarcacao) else posicao, size=(3, 1), key=(i, j))
                linha_layout.append(button)

            layout_tabuleiro.append(linha_layout)

        return layout_tabuleiro



    def imprimir_tabuleiro_gui(self, tamanho, oceano, funcao, classe_embarcacao, nome_embarcacao=None, tamanho_embarcacao=None):
        print("TELA: iniciou imprimir tabuleiro_gui")
        letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        layout_tabuleiro = []

        # Adiciona a linha de letras (coordenadas das colunas)
        header = [sg.Text(" ", size=(2, 1))] + [sg.Text(letra, size=(3, 1), justification='center') for letra in letras[:tamanho]]
        layout_tabuleiro.append(header)

        for i in range(tamanho):
            linha_layout = [sg.Text(str(i), size=(2, 1))]

            for j in range(tamanho):
                posicao = oceano[i][j]

                # Cria um botão para cada posição
                button = sg.Button(posicao.sigla if isinstance(posicao, classe_embarcacao) else posicao, size=(3, 1), key=(i, j))
                linha_layout.append(button)

            layout_tabuleiro.append(linha_layout)
        
        print("criou tabuleiro básico")

        # Layout das coordenadas
        if funcao == 'coloca_embarcacoes':
            layout_coordenadas = [
                [sg.Text(f"Selecione as coordenadas da embarcação a ser posicionada")],
                [sg.Text(f"Embarcação: {nome_embarcacao}")],
                [sg.Text(f"Tamanho: {tamanho_embarcacao}")],
            ]
        if funcao == 'faz_tiro':
            layout_coordenadas = [
                [sg.Text("Selecione a coordenada do tiro")],
            ]

        # Layout geral com duas colunas
        layout = [
            [sg.Column(layout_tabuleiro), sg.Column(layout_coordenadas)],
        ]

        print("Criou layout")
        # Crie a janela
        window = sg.Window('Batalha Naval', layout)
        print("criou a window")

        coordinates = self.get_coordinates(window, funcao)

        if funcao == 'coloca_embarcacoes' and coordinates[0] is not None:
            coordinates[1] = self.get_coordinates(window, funcao)[0]

        window.close()

        if None not in coordinates:
            print(f'Coordenadas selecionadas: {coordinates}')
            return coordinates
      

    def get_coordinates(self, window, funcao):
        print("inicia get_coodinates")
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            return None
        return [event] if funcao == 'faz_tiro' else [event, None]
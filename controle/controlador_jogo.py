from datetime import datetime
from entidade.jogo import Jogo
from limite.tela_jogo import TelaJogo
import random
from controle.controlador_excessao import ControladorExcessao
from entidade.jogo_dao import JogoDAO
from entidade.embarcacao import Embarcacao
import PySimpleGUI as sg


class ControladorJogo:
    def __init__(self, controlador_sistema) -> None:
        self.__controlador_sistema = controlador_sistema
        self.__tela_jogo = TelaJogo()
        self.__controlador_excessao = ControladorExcessao()
        self.__pontuacao_partida_jogador = 0
        self.__pontuacao_partida_computador = 0
        self.__hora_inicio = None
        self.__hora_fim = None
        self.__vencedor = None
        self.__jogo_dao = JogoDAO()
        self.__jogadas = []

    @property
    def jogos(self):
        return self.__jogo_dao.get_all()

    def faz_login(self):
        dados_login = self.__tela_jogo.recebe_login()
        recebe_nome, recebe_senha = dados_login["recebe_nome"], dados_login["recebe_senha"]
        jogador = self.__controlador_sistema.retorna_estah_cadastrado(recebe_nome, recebe_senha)
        if jogador == False or jogador == None:
            self.__tela_jogo.mostra_mensagem("Jogador não encontrado!")
            self.faz_login()
        else:
            self.inicia_jogo(jogador)

    def inicia_jogo(self, jogador):
        self.abre_menu_jogo(jogador)

    def voltar(self):
        self.__controlador_sistema.abre_opcoes()


    def abre_menu_jogo(self, jogador):
        try:
            lista_opcoes = {1: self.inicia_partida, 
                            2: self.__controlador_sistema.controlador_jogador.historico_jogador,
                            3: self.historico_geral,
                            0: self.voltar}
            opcao_selecionada = self.__tela_jogo.mostra_opcoes()
            if opcao_selecionada == 0:
                funcao_escolhida = lista_opcoes[opcao_selecionada]
                funcao_escolhida()
            else:
                funcao_escolhida = lista_opcoes[opcao_selecionada]
                funcao_escolhida(jogador)
        except Exception as e:
            mensagem = "Digite um número entre 0-3, conforme a opção desejada"
            self.__controlador_excessao.handle_value_error(e, mensagem)
            self.abre_menu_jogo(jogador)
    
    def abre_menu_final(self, jogador):
        try:
            lista_opcoes = {1: self.inicia_partida,
                            2: self.abre_menu_jogo,
                            3: self.historico_geral,
                            0: self.__controlador_sistema.encerra_sistema}
            opcao_selecionada = self.__tela_jogo.mostra_opcoes_final()
            if opcao_selecionada == 0:
                funcao_escolhida = lista_opcoes[opcao_selecionada]
                funcao_escolhida()
            else:
                funcao_escolhida = lista_opcoes[opcao_selecionada]
                funcao_escolhida(jogador)
        except Exception as e:
            mensagem = "Digite um número entre 0-3, coforme a opção desejada"
            self.__controlador_excessao.handle_value_error(e, mensagem)
            self.abre_menu_final(jogador)

    def historico_geral(self, jogador):
        self.__tela_jogo.mostra_historico_geral(self.jogos)
        self.abre_menu_jogo(jogador)
        
    def abre_voltar(self, acao_sim, acao_nao, jogador):
        try:
            opcao = self.__tela_jogo.voltar()
            if opcao.upper() == "S":
                acao_sim(jogador)
            elif opcao.upper() == "N":
                acao_nao(jogador)
            else:
                self.__tela_jogo.mostra_mensagem("Digite uma opção válida")
        except Exception as e:
            mensagem = "Digite corretamente a opção desejada: 'S' (para sim) ou 'N' (para nao)"
            self.__controlador_excessao.handle_value_error(e, mensagem)
            self.abre_voltar()

    def remover_historico(self):
        self.historico_geral()
        id = input("Digite o id: ")
        self.__jogo_dao.remove(id)
        print("jogo removido")
        self.historico_geral()
        opcao = input("deseja remover de novo? ")
        if opcao == 'S':
            self.remover_historico()

    def mostrar_data(self):
        data_atual = datetime.now()
        data_formatada = data_atual.strftime("%d/%m/%Y %H:%M:%S")
        return data_formatada

    def inicia_partida(self, jogador_logado):
        self.__hora_inicio = datetime.now().replace(microsecond=0)
        self.__tela_jogo.mostra_mensagem("Partida iniciada!")
        self.partida(jogador_logado)

    def imprimir_tabuleiro(self, tamanho, oceano):
        letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        layout = []

        # Cabeçalho das colunas
        layout.append([sg.Text("   " + " ".join(letras[:tamanho]))])

        for i, linha in enumerate(oceano):
            # Número da linha
            linha_layout = [sg.Text("{:2} ".format(i))]
            
            for posicao in linha:
                if isinstance(posicao, Embarcacao):
                    linha_layout.append(sg.Text(posicao.sigla, size=(2, 1)))
                else:
                    linha_layout.append(sg.Text(posicao, size=(2, 1)))

            layout.append(linha_layout)

        # Letras das colunas no final
        layout.append([sg.Text("    " + "     ".join(letras[:tamanho]))])

        # Adicione um botão "Continuar"
        layout.append([sg.Button("Continuar")])

        # Crie a janela
        window = sg.Window('Tabuleiro', layout)
        event, values = window.read()
        # Se o botão "Continuar" for pressionado, feche a janela
        if event == "Continuar":
            window.close()

    def imprimir_tabuleiro_gui(self, tamanho, oceano):
        print("imprimir_tabuleiro")
        letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        # Layout do tabuleiro
        layout_tabuleiro = []
        layout_tabuleiro.append([sg.Text("      " + "     ".join(letras[:tamanho]))])

        for i, linha in enumerate(oceano):
            linha_layout = [sg.Text("{:2} ".format(i))]

            for posicao in linha:
                if isinstance(posicao, Embarcacao):
                    linha_layout.append(sg.Text(posicao.sigla, size=(2, 1)))
                else:
                    linha_layout.append(sg.Text(posicao, size=(2, 1)))

            layout_tabuleiro.append(linha_layout)

        layout_tabuleiro.append([sg.Text("      " + "     ".join(letras[:tamanho]))])

        # Layout das coordenadas
        layout_coordenadas = [
            [sg.Text("Digite a coordenada da Embarcação")],
            [sg.Text("Coordenada Inicial"), sg.InputText(key='coordenada-inicial', size=(5, 1)), sg.Text("Coordenada Final"), sg.InputText(key='coordenada-final', size=(5, 1))],
            [sg.Button("OK")]
        ]

        # Layout geral com duas colunas
        layout = [
            [sg.Column(layout_tabuleiro), sg.Column(layout_coordenadas)],
        ]

        # Crie a janela
        window = sg.Window('Tabuleiro', layout)

        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED:
                window.close()
                return None

            if event == "OK":
                try:
                    linha = values['coordenada-inicial']
                    coluna = values['coordenada-final']
                    window.close()
                    return linha, coluna
                except ValueError:
                    sg.popup_error("Digite coordenadas válidas.")


    def mapear_letra_numero(self, valor):
        if isinstance(valor, int) and 0 <= valor <= 9:
            alfabeto = {i: chr(65 + i) for i in range(26)}
            if valor in alfabeto:
                return alfabeto[valor]
        elif isinstance(valor, str) and len(valor) == 1 and valor.isalpha():
            valor = valor.upper()  # Converte a letra para maiúscula
            alfabeto = {chr(65 + i): i for i in range(26)}
            if valor in alfabeto:
                return alfabeto[valor]  
        return None
    
    def recebe_coordenada_gui(self, msg=None):

        layout = [
            [sg.Text(f'Digite a coordenada {msg} desejada: '), sg.InputText(key='coordenada')],
            [sg.Button('OK')]
        ]

        window = sg.Window('Recebe Coordenada', layout)

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED:
                window.close()
                return None

            if event == 'OK':
                coordenada = values['coordenada']
                window.close()
                return coordenada
    
    def trata_coordenada(self, tamanho_oceano, oceano_jogador):
       print('inicia trata coordenda')
       while True:
        try:
            coordenada_1, coordenada_2 = self.imprimir_tabuleiro_gui(tamanho_oceano, oceano_jogador)

            if len(coordenada_1) < 2 or not coordenada_1[1:].isdigit() or not coordenada_1[0].isalpha() or \
               len(coordenada_2) < 2 or not coordenada_2[1:].isdigit() or not coordenada_2[0].isalpha():
                raise ValueError("Digite coordenadas válidas")

            linha1 = int(coordenada_1[1:])
            coluna1 = self.mapear_letra_numero(coordenada_1[0])

            linha2 = int(coordenada_2[1:])
            coluna2 = self.mapear_letra_numero(coordenada_2[0])

            if 0 <= linha1 < tamanho_oceano and 0 <= coluna1 < tamanho_oceano and \
               0 <= linha2 < tamanho_oceano and 0 <= coluna2 < tamanho_oceano:
                return (linha1, coluna1), (linha2, coluna2)
            else:
                self.__tela_jogo.mostra_mensagem("Coordenadas fora dos limites do tabuleiro. Tente novamente.")
        except ValueError as e:
            self.__tela_jogo.mostra_mensagem(e)
        

    def posiciona_embarcacao(self, tamanho_oceano, oceano, embarcacao):
        tamanho_embarcacao = embarcacao.vida
        while True:
            print("inicia while posiciona embarcação")
            (linha_inicial, coluna_inicial), (linha_final, coluna_final) = self.trata_coordenada(tamanho_oceano, oceano)
            print("Coordenada 1:")
            print("Linha:", linha_inicial)
            print("Coluna:", coluna_inicial)

            print("Coordenada 2:")
            print("Linha:", linha_final)
            print("Coluna:", coluna_final)
            break
        if (linha_inicial == linha_final and coluna_final - coluna_inicial == tamanho_embarcacao - 1) or \
            (coluna_inicial == coluna_final and linha_final - linha_inicial == tamanho_embarcacao - 1):
            for linha in range(linha_inicial, linha_final + 1):
                for coluna in range(coluna_inicial, coluna_final + 1):
                    if oceano[linha][coluna] != "~":
                        self.__tela_jogo.mostra_mensagem("Posição já ocupada. Tente novamente.")
                        return False

                for linha in range(linha_inicial, linha_final + 1):
                    for coluna in range(coluna_inicial, coluna_final + 1):
                        oceano[linha][coluna] = embarcacao   #TO DO colocar embarcacao
                return True
        else:
            self.__tela_jogo.mostra_mensagem("Posição inválida. Tente novamente.")

    def posiciona_embarcacao_computador(self, tamanho_oceano, oceano, embarcacao):
        tamanho_embarcacao = embarcacao.vida

        while True:
            linha_inicial = random.randint(0, tamanho_oceano)
            coluna_inicial = random.randint(0, tamanho_oceano)
            orientacao = random.choice(["horizontal", "vertical"])

            if orientacao == "horizontal":
                linha_final = linha_inicial
                coluna_final = coluna_inicial + tamanho_embarcacao - 1
            else:
                linha_final = linha_inicial + tamanho_embarcacao - 1
                coluna_final = coluna_inicial

            if (0 <= linha_inicial < tamanho_oceano) and (0 <= coluna_inicial < tamanho_oceano) and \
            (0 <= linha_final < tamanho_oceano) and (0 <= coluna_final < tamanho_oceano):
                valido = True
                for linha in range(linha_inicial, linha_final + 1):
                    for coluna in range(coluna_inicial, coluna_final + 1):
                        if oceano[linha][coluna] != "~":
                            valido = False
                            break

                if valido:
                    for linha in range(linha_inicial, linha_final + 1):
                        for coluna in range(coluna_inicial, coluna_final + 1):
                            oceano[linha][coluna] = embarcacao 
                    return True

    def faz_tiro_jogador(self, tamanho_oceano, oceano_tiros_jogador, oceano_computador):
        linha, coluna = self.trata_coordenada(tamanho_oceano, "do tiro")

        if oceano_tiros_jogador[linha][coluna] == "O" or oceano_tiros_jogador[linha][coluna] == "X":
            self.__tela_jogo.mostra_mensagem("O tiro foi repetido!")
            return False 

        if oceano_computador[linha][coluna] != "~":
            embarcacao = oceano_computador[linha][coluna]
            tiro_acertou = True
            self.__tela_jogo.mostra_resultado_rodada("Você", "acertou")
            embarcacao.vida -= 1
            if embarcacao.vida == 0:
                self.__tela_jogo.mostra_mensagem(f"{embarcacao.nome} afundou!")
                self.__pontuacao_partida_jogador += 3
            self.__pontuacao_partida_jogador += 1
        else:
            tiro_acertou = False
            self.__tela_jogo.mostra_resultado_rodada("Você", "não acertou")

        oceano_tiros_jogador[linha][coluna] = "X" if tiro_acertou else "O"

        coluna = self.mapear_letra_numero(coluna)
        linha = str(linha)
        self.__jogadas.append((linha + coluna, "acertou" if tiro_acertou else "errou"))

        return tiro_acertou
    
    def faz_tiro_computador(self, tamanho, oceano_jogador, oceano_tiros_computador):
        self.__tela_jogo.mostra_mensagem("Turno do computador:")
        while True:
            linha, coluna = random.randint(0, tamanho-1), random.randint(0, tamanho-1)
            if oceano_tiros_computador[linha][coluna] == "~":
                if oceano_jogador[linha][coluna] != "~":
                    embarcacao = oceano_jogador[linha][coluna]
                    self.__tela_jogo.mostra_resultado_rodada("O computador", "acertou")
                    embarcacao.vida -= 1
                    print("tira vida da embaracao", embarcacao.vida)
                    tiro_acertou = True
                    if embarcacao.vida == 0:
                        self.__tela_jogo.mostra_mensagem(f"{embarcacao.nome} afundou!")
                        self.__pontuacao_partida_computador += 3
                    self.__pontuacao_partida_computador += 1 
                else:
                    oceano_tiros_computador[linha][coluna] = "O"
                    self.__tela_jogo.mostra_resultado_rodada("O computador", "errou")
                    tiro_acertou = False
                oceano_tiros_computador[linha][coluna] = "X" if tiro_acertou else "O"
                break


    def todas_embarcacoes_afundadas(self, tabuleiro):
        atingidas = 0
        for linha in tabuleiro:
            for simbolo in linha:
                if simbolo == "X":
                    atingidas += 1
        if atingidas ==  17:
            return True
    
    def vencedor_computador(self, oceano_tiros_computador):
        if self.todas_embarcacoes_afundadas(oceano_tiros_computador):
            self.__vencedor = "computador"
            return True
        return False

    def vencedor_jogador(self, oceano_tiros_jogador):
        if self.todas_embarcacoes_afundadas(oceano_tiros_jogador):
            self.__vencedor = "jogador"
            return True
        return False
    
    

    def partida(self, jogador_logado): 
        tamanho = self.__controlador_sistema.retorna_recebe_tamanho_oceano()
        oceano_jogador = self.__controlador_sistema.retorna_cria_oceano(tamanho)
        oceano_computador = self.__controlador_sistema.retorna_cria_oceano(tamanho)
        oceano_tiros_jogador = self.__controlador_sistema.retorna_cria_oceano(tamanho)
        oceano_tiros_computador = self.__controlador_sistema.retorna_cria_oceano(tamanho)
        self.imprimir_tabuleiro(tamanho, oceano_jogador.matriz)
        for embarcacao in oceano_jogador.embarcacoes:  
            quantidade = embarcacao.quantidade
            nome_embarcacao = embarcacao.nome
            tamanho_embarcacao = embarcacao.vida
            self.__tela_jogo.mostra_mensagem(f"Quantidade de {nome_embarcacao} para serem posicionados: {quantidade}")
            self.__tela_jogo.mostra_mensagem(f"Posicione o {nome_embarcacao} (tamanho {tamanho_embarcacao})")
            while True:
                if self.posiciona_embarcacao(tamanho, oceano_jogador.matriz, embarcacao):
                    break
            self.posiciona_embarcacao_computador(tamanho, oceano_computador.matriz, embarcacao)  

        while not (self.vencedor_jogador(oceano_tiros_jogador.matriz) or \
                   self.vencedor_computador(oceano_tiros_computador.matriz)):  
            self.imprimir_tabuleiro(tamanho, oceano_tiros_jogador.matriz) 
            self.imprimir_tabuleiro(tamanho, oceano_computador.matriz) 
            while self.faz_tiro_jogador(tamanho, oceano_tiros_jogador.matriz, oceano_computador.matriz):
                if self.vencedor_jogador(oceano_tiros_jogador.matriz):
                    break
                self.imprimir_tabuleiro(tamanho, oceano_tiros_jogador.matriz)
            while self.faz_tiro_computador(tamanho, oceano_jogador.matriz, oceano_tiros_computador.matriz):
                self.faz_tiro_computador(tamanho, oceano_jogador.matriz, oceano_tiros_computador.matriz)
        self.termina_jogo(jogador_logado)

    def termina_jogo(self, jogador_logado):
        vencedor = self.__vencedor
        self.__hora_fim = datetime.now().replace(microsecond=0)
        duracao = self.__hora_fim - self.__hora_inicio
        data = self.mostrar_data()
        jogo = Jogo(jogador_logado, data, duracao, vencedor, self.__pontuacao_partida_jogador, self.__jogadas)
        self.__controlador_sistema.controlador_jogador.adiciona_jogo(jogador_logado, jogo)
        self.__jogo_dao.add(jogo)
        self.__tela_jogo.mostra_resultados(duracao, vencedor, self.__pontuacao_partida_jogador,
                                            self.__pontuacao_partida_computador)
        jogo.adiciona_na_pontuacao_geral(self.__pontuacao_partida_jogador)
        self.__controlador_sistema.controlador_jogador.atualiza_jogador(jogador_logado)
        self.abre_menu_final(jogador_logado)


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

    def inicia_jogo(self):
        jogador = self.__controlador_sistema.controlador_jogador.faz_login()
        if jogador == None:
            self.inicia_jogo()
        if jogador == 'Voltar':
            return self.voltar()
        else:
            self.abre_menu_jogo(jogador)

    def voltar(self):
        self.__controlador_sistema.abre_opcoes()


    def abre_menu_jogo(self, jogador):
        try:
            lista_opcoes = {1: self.inicia_partida, 
                            2: self.historico_jogador,
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
    
    def abre_menu_final(self, jogador=None):
        try:
            lista_opcoes = {1: self.inicia_partida,
                            2: self.abre_menu_jogo,
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
    
    def historico_jogador(self, jogador):
        lista_jogos_jogador = jogador.jogos
        if len(lista_jogos_jogador) == 0:
            self.__tela_jogo.mostra_mensagem("O jogador ainda não possui nenhum jogo!")
        self.__tela_jogo.mostra_historico_jogador(lista_jogos_jogador)
        self.abre_menu_jogo(jogador)


    def mostrar_data(self):
        data_atual = datetime.now()
        data_formatada = data_atual.strftime("%d/%m/%Y %H:%M:%S")
        return data_formatada

    def inicia_partida(self, jogador_logado):
        self.__hora_inicio = datetime.now().replace(microsecond=0)
        self.__tela_jogo.mostra_mensagem("Partida iniciada!")
        self.partida(jogador_logado)


    def abre_imprimir_tabuleiro_gui(self, tamanho, oceano, funcao, nome_embarcacao=None, tamanho_embarcacao=None, oceano_tiros_computador=None):
        classe_embarcacao = Embarcacao
        if funcao == 'faz_tiro':
            layout_computador = self.__tela_jogo.layout_tabuleiro(tamanho, classe_embarcacao, oceano=oceano_tiros_computador)
            coordendas = self.__tela_jogo.imprimir_tabuleiro_gui(tamanho, oceano, funcao, classe_embarcacao, nome_embarcacao, tamanho_embarcacao, layout_computador)
        else:
            coordendas = self.__tela_jogo.imprimir_tabuleiro_gui(tamanho, oceano, funcao, classe_embarcacao, nome_embarcacao, tamanho_embarcacao)
        return coordendas

    def abre_imprimir_tabuleiro(self, tamanho, oceano):
        embarcacao = Embarcacao
        self.__tela_jogo.imprimir_tabuleiro(tamanho, oceano, embarcacao)

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
    
    
    def trata_coordenada(self, tamanho_oceano, oceano_jogador, funcao,embarcacao=None, oceano_tiros_computador=None):
        while True:
                if funcao == 'faz_tiro':
                    coordenadas = self.abre_imprimir_tabuleiro_gui(tamanho_oceano, oceano_jogador, funcao, oceano_tiros_computador=oceano_tiros_computador)
                    linha = coordenadas[0][0]
                    coluna = coordenadas[0][1]
                    return linha, coluna
                if funcao == 'coloca_embarcacoes':
                    tamanho_embarcacao = embarcacao.vida
                    nome_embarcacao = embarcacao.nome 
                    coordenada_1, coordenada_2 = self.abre_imprimir_tabuleiro_gui(tamanho_oceano,oceano_jogador, funcao, nome_embarcacao, tamanho_embarcacao)
                    linha1 = coordenada_1[0]
                    coluna1 = coordenada_1[1]
                    linha2 = coordenada_2[0]
                    coluna2 = coordenada_2[1]
                    return (linha1, coluna1), (linha2, coluna2)

        

    def posiciona_embarcacao(self, tamanho_oceano, oceano, embarcacao):
        tamanho_embarcacao = embarcacao.vida
        while True:
            (linha_inicial, coluna_inicial), (linha_final, coluna_final) = self.trata_coordenada(tamanho_oceano, oceano, 'coloca_embarcacoes', embarcacao)
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
                        oceano[linha][coluna] = embarcacao   
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

    def faz_tiro_jogador(self, tamanho_oceano, oceano_tiros_jogador, oceano_computador, oceano_tiros_computador):
        tiro_acertou = False
        afundou = False
        nome_embarcacao = None
        linha, coluna = self.trata_coordenada(tamanho_oceano, oceano_tiros_jogador, 'faz_tiro', oceano_tiros_computador=oceano_tiros_computador)
        if oceano_tiros_jogador[linha][coluna] == "O" or oceano_tiros_jogador[linha][coluna] == "X":
            self.__tela_jogo.mostra_mensagem("O tiro foi repetido!")
            return self.faz_tiro_jogador(tamanho_oceano, oceano_tiros_jogador, oceano_computador, oceano_tiros_computador)
        if oceano_computador[linha][coluna] != "~":
            embarcacao = oceano_computador[linha][coluna]
            nome_embarcacao = embarcacao.nome 
            tiro_acertou = True
            embarcacao.vida -= 1
            self.__pontuacao_partida_jogador += 1
            afundou = False
            if embarcacao.vida == 0:
                self.__pontuacao_partida_jogador += 3
                afundou = True
        self.__tela_jogo.mostra_resultado_rodada("Jogador", tiro_acertou, afundou, nome_embarcacao=nome_embarcacao)
        oceano_tiros_jogador[linha][coluna] = "X" if tiro_acertou else "O"
        return tiro_acertou
    
    def faz_tiro_computador(self, tamanho, oceano_jogador, oceano_tiros_computador):
        tiro_acertou = False
        afundou = False
        nome_embarcacao = None
        self.__tela_jogo.mostra_mensagem("Turno do computador:")
        while True:
            linha, coluna = random.randint(0, tamanho-1), random.randint(0, tamanho-1)
            if oceano_tiros_computador[linha][coluna] != "~":
                embarcacao = oceano_jogador[linha][coluna]
                nome_embarcacao = embarcacao.nome
                embarcacao.vida -= 1
                tiro_acertou = True
                self.__pontuacao_partida_computador += 1
                afundou = False
                if embarcacao.vida == 0:
                    self.__pontuacao_partida_computador += 3
                    afundou = True
            self.__tela_jogo.mostra_resultado_rodada("O computador", tiro_acertou, afundou, nome_embarcacao)
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
    
    def reinicia_vidas(self, embarcacoes):
        for embarcacao in embarcacoes:
            embarcacao.vida = embarcacao.vida_max
        
    

    def partida(self, jogador_logado):
        tamanho = self.__controlador_sistema.retorna_recebe_tamanho_oceano()
        oceano_jogador = self.__controlador_sistema.retorna_cria_oceano(tamanho)
        oceano_computador = self.__controlador_sistema.retorna_cria_oceano(tamanho)
        oceano_tiros_jogador = self.__controlador_sistema.retorna_cria_oceano(tamanho)
        oceano_tiros_computador = oceano_jogador
        for embarcacao in oceano_jogador.embarcacoes: 
            while True:
                if self.posiciona_embarcacao(tamanho, oceano_jogador.matriz, embarcacao):
                    break
            self.posiciona_embarcacao_computador(tamanho, oceano_computador.matriz, embarcacao)  

        while not (self.vencedor_jogador(oceano_tiros_jogador.matriz) or \
                   self.vencedor_computador(oceano_tiros_computador.matriz)):  
            self.abre_imprimir_tabuleiro(tamanho, oceano_computador.matriz) 
            while self.faz_tiro_jogador(tamanho, oceano_tiros_jogador.matriz, oceano_computador.matriz, oceano_tiros_computador.matriz):
                if self.vencedor_jogador(oceano_tiros_jogador.matriz):
                    break
            while self.faz_tiro_computador(tamanho, oceano_jogador.matriz, oceano_tiros_computador.matriz):
                if self.vencedor_computador(oceano_tiros_computador.matriz):
                    break
        self.reinicia_vidas(oceano_jogador.embarcacoes)
        self.reinicia_vidas(oceano_computador.embarcacoes)
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


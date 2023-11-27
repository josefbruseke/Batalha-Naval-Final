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
        if dados_login == 'Encerrar Sistema':
            if not self.__controlador_sistema.encerra_sistema():
                self.faz_login()
        if dados_login == 'Voltar':
            self.voltar()       
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
    
    def abre_menu_final(self, jogador):
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

    def abre_imprimir_tabuleiro(self, tamanho, oceano):
        embarcacao = Embarcacao
        self.__tela_jogo.imprimir_tabuleiro(tamanho, oceano, embarcacao)


    def abre_imprimir_tabuleiro_gui(self, tamanho, oceano, funcao, nome_embarcacao=None, tamanho_embarcacao=None):
        print("iniciou abre_imprimir_tabuleiro_gui")
        classe_embarcacao = Embarcacao
        coordendas = self.__tela_jogo.imprimir_tabuleiro_gui(tamanho, oceano, funcao, classe_embarcacao, nome_embarcacao, tamanho_embarcacao)
        return coordendas


    def mapear_letra_numero(self, valor):
        print("inicia mapear_letra_numero")
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
    
    
    def trata_coordenada(self, tamanho_oceano, oceano_jogador, funcao, embarcacao=None):
        print('Inicia trata coordenada')
        while True:
                if funcao == 'faz_tiro':
                    coordenadas = self.abre_imprimir_tabuleiro_gui(tamanho_oceano, oceano_jogador, funcao)
                    print("Coordenada de trata coordenada:", coordenadas)
                    print(coordenadas)
                    print(len(coordenadas))
                    linha = coordenadas[0][0]
                    print(linha)
                    coluna = coordenadas[0][1]
                    print(coluna)
                    return linha, coluna
                if funcao == 'coloca_embarcacoes':
                    tamanho_embarcacao = embarcacao.vida
                    nome_embarcacao = embarcacao.nome 
                    coordenada_1, coordenada_2 = self.abre_imprimir_tabuleiro_gui(tamanho_oceano,oceano_jogador, funcao, nome_embarcacao, tamanho_embarcacao)
                    print(coordenada_1, coordenada_2)
                    linha1 = coordenada_1[0]
                    coluna1 = coordenada_1[1]
                    linha2 = coordenada_2[0]
                    coluna2 = coordenada_2[1]
                    print((linha1, coluna1), (linha2, coluna2))
                    return (linha1, coluna1), (linha2, coluna2)

        

    def posiciona_embarcacao(self, tamanho_oceano, oceano, embarcacao):
        print("inicia posiciona embarcação")
        tamanho_embarcacao = embarcacao.vida
        while True:
            (linha_inicial, coluna_inicial), (linha_final, coluna_final) = self.trata_coordenada(tamanho_oceano, oceano, 'coloca_embarcacoes', embarcacao)
            print(linha_inicial, coluna_inicial, linha_final, coluna_final)
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

    def faz_tiro_jogador(self, tamanho_oceano, oceano_tiros_jogador, oceano_computador):
        print("Faz tiro jogador inicado")
        linha, coluna = self.trata_coordenada(tamanho_oceano, oceano_tiros_jogador, 'faz_tiro')
        print("coordenada de faz tiro jgaodor recebbida de trata_coodernada:", linha, coluna)
        if oceano_tiros_jogador[linha][coluna] == "O" or oceano_tiros_jogador[linha][coluna] == "X":
            self.__tela_jogo.mostra_mensagem("O tiro foi repetido!")
            self.faz_tiro_jogador(self, tamanho_oceano, oceano_tiros_jogador, oceano_computador)

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

        return tiro_acertou
    
    def faz_tiro_computador(self, tamanho, oceano_jogador, oceano_tiros_computador):
        self.__tela_jogo.mostra_mensagem("Turno do computador:")
        while True:
            linha, coluna = random.randint(0, tamanho-1), random.randint(0, tamanho-1)
            if oceano_tiros_computador[linha][coluna] != "~":
                embarcacao = oceano_jogador[linha][coluna]
                self.__tela_jogo.mostra_resultado_rodada("O computador", "acertou")
                embarcacao.vida -= 1
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
    
    def reinicia_vidas(self, embarcacoes):
        for embarcacao in embarcacoes:
            embarcacao.vida = embarcacao.vida_max
        
    

    def partida(self, jogador_logado):
        print("inicia partida")
        
        tamanho = self.__controlador_sistema.retorna_recebe_tamanho_oceano()
        oceano_jogador = self.__controlador_sistema.retorna_cria_oceano(tamanho)
        oceano_computador = self.__controlador_sistema.retorna_cria_oceano(tamanho)
        oceano_tiros_jogador = self.__controlador_sistema.retorna_cria_oceano(tamanho)
        oceano_tiros_computador = oceano_jogador
        for embarcacao in oceano_jogador.embarcacoes: 
            print("inicia o for")
            while True:
                if self.posiciona_embarcacao(tamanho, oceano_jogador.matriz, embarcacao):
                    break
            self.posiciona_embarcacao_computador(tamanho, oceano_computador.matriz, embarcacao)  

        while not (self.vencedor_jogador(oceano_tiros_jogador.matriz) or \
                   self.vencedor_computador(oceano_tiros_computador.matriz)):  
            self.abre_imprimir_tabuleiro(tamanho, oceano_computador.matriz) 
            while self.faz_tiro_jogador(tamanho, oceano_tiros_jogador.matriz, oceano_computador.matriz):
                if self.vencedor_jogador(oceano_tiros_jogador.matriz):
                    break
            while self.faz_tiro_computador(tamanho, oceano_jogador.matriz, oceano_tiros_computador.matriz):
                self.faz_tiro_computador(tamanho, oceano_jogador.matriz, oceano_tiros_computador.matriz)
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


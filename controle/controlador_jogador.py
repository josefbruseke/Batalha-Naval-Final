from limite.tela_jogador import TelaJogador
from entidade.jogador import Jogador
from controle.controlador_excessao import ControladorExcessao
from entidade.jogador_dao import JogadorDAO
import datetime


class ControladorJogador:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_jogador = TelaJogador()
        self.__controlador_execessao = ControladorExcessao()
        self.__jogador_dao = JogadorDAO()

    @property
    def jogadores(self):
        return self.__jogador_dao.get_all()

    def cadastra_jogador(self):
        dados_jogador = self.__tela_jogador.recebe_cadastro()

        try:
            data_nascimento = datetime.datetime.strptime(dados_jogador["data_nascimento"], "%d/%m/%Y")
        except ValueError:
            self.__tela_jogador.mostra_mensagem("Formato de data de nascimento inválido. Tente novamente.")
            self.cadastra_jogador()
            return

        for jogador in self.jogadores:
            if dados_jogador["nome"] == jogador.nome and data_nascimento == jogador.data_nascimento:
                self.__tela_jogador.mostra_mensagem("Jogador já cadastrado!")
                self.__controlador_sistema.abre_opcoes()
                return

        jogador = Jogador(dados_jogador["nome"], data_nascimento, dados_jogador["senha"], pontuacao=0)
        self.__jogador_dao.add(jogador)
        self.__tela_jogador.mostra_mensagem("\nCadastro realizado com sucesso!")
        self.__tela_jogador.mostra_mensagem("Faça Login para jogar! \n")
        
    def pega_jogador_por_nome_e_senha(self, nome: str, senha: str):
        for jogador in self.jogadores:
            if jogador.nome == nome and jogador.senha == senha:
                return jogador
        return None

    def altera_cadastro(self):
        self.lista_jogadores()
        dados =  self.__tela_jogador.seleciona_jogador()
        player = self.pega_jogador_por_nome_e_senha(dados["nome"], dados["senha"])

        if player is not None:
            novos_dados_jogador =  self.__tela_jogador.pega_dados_jogador()
            player.nome = novos_dados_jogador["nome"]
            player.nascimento =  novos_dados_jogador["nascimento"]
            player.senha = novos_dados_jogador["senha"]
            self.lista_jogadores()
            self.__controlador_sistema.abre_opcoes()
        else:
            self.__tela_jogador.mostra_mensagem("Jogador não existe")
            self.altera_cadastro()

    def remove_jogador(self):
        self.lista_jogadores()
        dados = self.__tela_jogador.seleciona_jogador()
        jogador = self.pega_jogador_por_nome_e_senha(dados["nome"], dados["senha"])
        
        if jogador is not None:
            self.__jogador_dao.remove(jogador)
            self.__tela_jogador.mostra_mensagem("Jogador removido!")
            self.lista_jogadores()
            self.__controlador_sistema.abre_opcoes()
        else:
            self.__tela_jogador.mostra_mensagem("Jogador não encontrado!")
            self.__controlador_sistema.abre_opcoes()

    def ordena_ranking(self):
        self.lista_jogadores.sort(key=lambda jogador: (
            jogador.pontuacao, jogador.nome))

    def lista_jogadores(self):
        for jogador in self.jogadores:
            self.__tela_jogador.mostra_mensagem({"nome": jogador.nome})

    def estah_cadastrado(self, nome, senha):
        for jogador in self.jogadores:
            if jogador.nome == nome and jogador.senha == senha:
                return True

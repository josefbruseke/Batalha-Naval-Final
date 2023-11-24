from limite.tela_sistema import TelaSistema
from controle.controlador_jogador import ControladorJogador
from controle.controlador_jogo import ControladorJogo
from controle.controlador_oceano import ControladorOceano
from controle.controlador_excessao import ControladorExcessao

class ControladorSistema:
    def __init__(self) -> None:
        self.__controlador_jogador = ControladorJogador(self)
        self.__controlador_jogo = ControladorJogo(self)
        self.__controlador_oceano = ControladorOceano(self)
        self.__tela_sistema = TelaSistema()
        self.__controlador_excessao = ControladorExcessao()

    @property
    def controlador_jogador(self) -> ControladorJogador:
        return self.__controlador_jogador
    
    @property
    def controlador_jogo(self) -> ControladorJogo:
        return self.__controlador_jogo
    
    @property
    def controlador_oceano(self) -> ControladorOceano:
        return self.__controlador_oceano
    
    def jogador_logado(self, jogador_logado):
        self.__jogador_logado = jogador_logado
    
    def inicia_cadastro(self):
        self.__controlador_jogador.abre_opcoes_cadastro()
        self.abre_opcoes()

    def inicia_login(self):
        self.__controlador_jogo.faz_login()

    def retorna_ordena_ranking(self):         
        return self.__controlador_jogador.ordena_ranking()

    def retorna_estah_cadastrado(self, recebe_nome, recebe_senha):
        return self.__controlador_jogador.estah_cadastrado(recebe_nome, recebe_senha)
    

    def retorna_cria_oceano(self, tamanho):
        return self.__controlador_oceano.cria_oceano(tamanho)

    def retorna_recebe_tamanho_oceano(self):
        return self.__controlador_oceano.recebe_tamanho_oceano()

    def ver_ranking(self):
        self.__controlador_jogador.ordena_ranking()
        self.abre_opcoes()
        

    def inicializa_sistema(self):
        self.abre_opcoes()

    def abre_opcoes(self):
        try: 
            lista_opcoes = {1: self.inicia_login, 
                            2: self.inicia_cadastro,
                            3: self.ver_ranking,
                            0: self.encerra_sistema}
            opcao_selecionada = self.__tela_sistema.mostra_opcoes()
            funcao_escolhida = lista_opcoes[opcao_selecionada]
            funcao_escolhida()
        except Exception as e:
            mensagem = "Digite um número entre 0-2, coforme a opção desejada"
            self.__controlador_excessao.handle_value_error(e, mensagem)
            self.abre_opcoes()

    def encerra_sistema(self):
        exit(0)

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
    
    def inicia_cadastro(self):
        self.__controlador_jogador.cadastra_jogador()
        self.abre_opcoes()
        
    def remove_cadastro(self):
        self.__controlador_jogador.remove_jogador()
        
    def altera_cadastro(self):
        self.controlador_jogador.altera_cadastro()

    def inicia_login(self):
        self.__controlador_jogo.faz_login()

    def ordena_ranking(self):
        pass

    def retorna_lista_jogadores(self):
        return self.__controlador_jogador.lista_jogadores()
    
    
    def retorna_estah_cadastrado(self, recebe_nome, recebe_senha):
        return self.__controlador_jogador.estah_cadastrado(recebe_nome, recebe_senha)
    
    
    def retorna_armazena_tamanho_oceano(self):
        return self.__controlador_oceano.cria_oceano_jogador()


    def inicializa_sistema(self):
        self.abre_opcoes()

    def abre_opcoes(self):
        try: 
            lista_opcoes = {1: self.inicia_login, 
                            2: self.inicia_cadastro,
                            3: self.remove_cadastro,
                            4: self.altera_cadastro,
                            0: self.encerra_sistema}
            opcao_selecionada = self.__tela_sistema.mostra_opcoes()
            funcao_escolhida = lista_opcoes[opcao_selecionada]
            funcao_escolhida()
        except Exception as e:
            mensagem = "Digite um número entre 0-4, coforme a opção desejada"
            self.__controlador_excessao.handle_value_error(e, mensagem)
            self.abre_opcoes()

    def encerra_sistema(self):
        exit(0)
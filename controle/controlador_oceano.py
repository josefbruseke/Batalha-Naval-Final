from limite.tela_embarcacao import TelaEmbarcacao
from limite.tela_oceano import TelaOceano
from entidade.oceano import Oceano
from entidade.fragata import Fragata
from entidade.porta_avioes import PortaAvioes
from entidade.bote import Bote
from entidade.submarino import Submarino
from controle.controlador_excessao import ControladorExcessao

class ControladorOceano:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_oceano = TelaOceano()
        self.__embarcacoes = [
            PortaAvioes(7),
            Fragata(10),
            Fragata(10),
            Submarino(4),
            Submarino(4),
            Bote(20),
            Bote(20),
            Bote(20)
        ]
    

    
    def recebe_tamanho_oceano(self):
        try:
            tamanho = self.__tela_oceano.recebe_tamanho()
            if tamanho == 'Voltar':
                return self.__controlador_sistema.controlador_jogo.abre_menu_inicial()
            if tamanho == 'Fechar':
                if not self.__controlador_sistema.encerra_sistema():
                    self.recebe_tamanho_oceano()
            if tamanho is not None and 6 <= tamanho <= 26:
                return tamanho
            else:
                self.__tela_oceano.mostra_mensagem("Tamanho inválido! Forneça um tamanho entre 6 e 26.")
                self.recebe_tamanho_oceano()
        except Exception as e:
            mensagem = "Erro ao receber o tamanho do oceano."
            self.__tela_oceano.mostra_mensagem(mensagem)



    def cria_oceano(self, tamanho):
        matriz = [["~" for _ in range(tamanho)] for _ in range(tamanho)]
        oceano = Oceano(tamanho, matriz, self.__embarcacoes)
        return oceano  
        
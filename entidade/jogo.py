class Jogo:
    def __init__(self, jogador, data, duracao: str, vencedor: str,
                  pontucao_partida: int, jogadas: list):
        self.__id = None
        self.__jogador = jogador
        self.__data = data
        self.__duracao = duracao
        self.__vencedor = vencedor
        self.__pontuacao_partida = pontucao_partida
        self.__jogadas = jogadas

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id   

    @property
    def jogador(self):
        return self.__jogador

    @jogador.setter
    def jogador(self, jogador):
        self.__jogador = jogador    
 
    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def duracao(self):
        return self.__duracao

    @duracao.setter
    def duracao(self, duracao):
        self.__duracao = duracao

    @property
    def vencedor(self):
        return self.__vencedor

    @vencedor.setter
    def vencedor(self, vencedor):
        self.__vencedor = vencedor

    @property
    def pontuacao_partida(self):
        return self.__pontuacao_partida

    @pontuacao_partida.setter
    def pontuacao_partida(self, pontuacao_partida):
        self.__pontuacao_partida = pontuacao_partida

    @property
    def jogadas(self):
        return self.__jogadas

    @jogadas.setter
    def jogadas(self, jogadas):
        self.__jogadas = jogadas

    def adiciona_na_pontuacao_geral(self, pontuacao_partida):
        self.__jogador.pontuacao += pontuacao_partida
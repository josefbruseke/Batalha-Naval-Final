class Jogo:
    def __init__(self, data, duracao, vencedor, pontucao_partida, jogadas):
        self.__data = data
        self.__duracao = duracao
        self.__vencedor = vencedor
        self.__pontuacao_partida = pontucao_partida

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

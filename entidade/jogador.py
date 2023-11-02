#from entidade.oceano import Oceano

class Jogador:
    def __init__(self, nome:str, data_nascimento, senha, pontuacao):
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__senha = senha
        self.__pontuacao = pontuacao
        #self.__oceano = Oceano
        self.historico = []

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @nome.setter
    def nome(self, data_nascimento):
        self.__data_nascimento = data_nascimento

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha):
        self.__senha = senha

    @property
    def pontuacao(self):
        return self.__pontuacao

    @pontuacao.setter
    def pontuacao(self, pontuacao):
        self.__pontuacao = pontuacao

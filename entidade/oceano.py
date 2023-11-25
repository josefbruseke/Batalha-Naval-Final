from entidade.embarcacao import Embarcacao


class Oceano:
    def __init__(self, tamanho_oceano: int, matriz, embarcacoes):
        self.__tamanho_oceano = tamanho_oceano
        self.__matriz = matriz

    
    @property
    def tamanho_oceano(self):
        return self.__tamanho_oceano
    
    @property
    def matriz(self):
        return self.__matriz
        
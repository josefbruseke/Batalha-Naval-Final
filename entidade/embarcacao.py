from abc import ABC, abstractmethod

class Embarcacao(ABC):
    @abstractmethod
    def __init__(self, nome, sigla, vida, vida_max, quantidade):
        self.__nome = nome
        self.__sigla = sigla
        self.__vida = vida
        self.__vida_max = vida_max
        self.__quantidade = quantidade
     

    @property
    def sigla(self):
        return self.__sigla
    
    @sigla.setter
    def sigla(self, sigla: int):
        self.__sigla = sigla

    @property
    def vida(self):
        return self.__vida
    
    @vida.setter
    def vida(self, vida: int):
        self.__vida = vida


    @property
    def vida_max(self):
        return self.__vida_max
    
    @vida_max.setter
    def vida_max(self, vida_max: int):
        self.vida_max = vida_max
    
    @property
    def nome(self):
        return self.__nome
        
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def quantidade(self):
        return self.__quantidade
        
    @quantidade.setter
    def quantidade(self, quantidade: int):
        self.__quantidade = quantidade

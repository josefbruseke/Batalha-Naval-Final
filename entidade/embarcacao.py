from abc import ABC, abstractmethod

class Embarcacao(ABC):
    @abstractmethod
    def __init__(self, nome, sigla, vida, quantidade):
        self.nome = nome
        self.sigla = sigla
        self.vida = vida  
        self.quantidade = quantidade
     

    def vida(self):
        return self.__vida
    
    @vida.setter
    def vida(self, vida: int):
        self.__vida = vida
    
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
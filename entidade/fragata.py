from entidade.embarcacao import Embarcacao

class Fragata(Embarcacao):
    def __init__(self, num_canhoes: int):
        super().__init__("Fragata", "F", 3, 3, 2)
        self.__num_canhoes = num_canhoes
        
    @property
    def num_canhoes(self):
        return self.__num_canhoes
    
    @num_canhoes.setter
    def num_canhoes(self, num_canhoes):
        self.__num_canhoes = num_canhoes
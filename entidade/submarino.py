from entidade.embarcacao import Embarcacao

class Submarino(Embarcacao):
    def __init__(self, profundidade: int):
        super().__init__("Submarino", "S", 2, 2, 2)
        self.__profundidade = profundidade
        
    @property 
    def profundidade(self):
        return self.__profundidade
    
    @profundidade.setter
    def profundidade(self, profundidade):
        self.__profundidade = profundidade
from entidade.embarcacao import Embarcacao

class Bote(Embarcacao):
    def __init__(self, num_coletes: int):
        super().__init__("Bote", "B", 1, 1, 3)
        self.__num_coletes = num_coletes
        
    @property
    def num_coletes(self):
        return self.__num_coletes
    
    @num_coletes.setter
    def num_coletes(self, num_coletes):
        self.__num_coletes = num_coletes
        
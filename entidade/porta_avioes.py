from entidade.embarcacao import Embarcacao

class PortaAvioes(Embarcacao):
    def __init__(self, num_avioes: int):
        super().__init__("Porta-Aviões", "P", 4, 4, 1)
        self.__num_avioes = num_avioes
        
    @property
    def num_avioes(self):
        return self.__num_avioes
    
    @num_avioes.setter
    def num_avioes(self, num_avioes):
        self.__num_avioes = num_avioes
        
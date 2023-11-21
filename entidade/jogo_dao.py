from entidade.dao import DAO
from entidade.jogo import Jogo

class JogoDAO(DAO):
    def __init__(self):
        super().__init__('jogo.pkl')

    def add(self, jogo:Jogo):
        max_id = 0
        for jogo in self.get_all():
            if max_id < jogo.id:
                max_id = jogo.id
        jogo.id = max_id + 1
        return super().add(jogo.id, jogo)
    
    def get(self, id:int):
        return super().get(id)
    
    def remove(self, jogo):
        super().remove(jogo.id)
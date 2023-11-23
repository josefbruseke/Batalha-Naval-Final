from entidade.dao import DAO
from entidade.jogo import Jogo

class JogoDAO(DAO):
    def __init__(self):
        super().__init__('jogo.pkl')

    def add(self, novo_jogo: Jogo):
        max_id = 0
        for jogo_existente in self.get_all():
            if max_id < jogo_existente.id:
                max_id = jogo_existente.id
        novo_jogo.id = max_id + 1
        print("jogo adicionado com id:", novo_jogo.id)
        return super().add(novo_jogo.id, novo_jogo)
    
    def get(self, id:int):
        return super().get(id)
    
    def remove(self, id):
        super().remove(id)
from entidade.oceano import Oceano

class TelaEmbarcacao:
    def mostra_embarcacoes(self):
       embarcacoes = Oceano.embarcacoes()
       return embarcacoes 
    
    def recebe_posicao_embarcacao(self):
        print("Informe a posição para inserir o barco: ")
        linha = int(input("Linha: "))
        coluna = input("Coluna: ").upper()
        return linha, coluna
        
    
    def mostra_embarcacoes_disponiveis(self, embarcacoes):
        pass
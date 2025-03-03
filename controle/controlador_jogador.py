from limite.tela_jogador import TelaJogador
from entidade.jogador import Jogador
from controle.controlador_excessao import ControladorExcessao
from entidade.jogador_dao import JogadorDAO
import datetime


class ControladorJogador:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_jogador = TelaJogador()
        self.__controlador_excessao = ControladorExcessao()
        self.__jogador_dao = JogadorDAO()

    @property
    def jogadores(self):
        return self.__jogador_dao.get_all()
    
    def abre_opcoes_cadastro(self):
        try: 
            lista_opcoes = {1: self.cadastra_jogador,
                            2: self.altera_cadastro,
                            3: self.remove_jogador,
                            0: self.__controlador_sistema.abre_opcoes}
            opcao_selecionada = self.__tela_jogador.opcoes_cadastro()
            funcao_escolhida = lista_opcoes[opcao_selecionada]
            funcao_escolhida()
        except Exception as e:
            mensagem = "Digite um número entre 0-3, coforme a opção desejada"
            self.__controlador_excessao.handle_value_error(e, mensagem)
            self.abre_opcoes_cadastro()

    def cadastra_jogador(self):
        dados_jogador = self.__tela_jogador.recebe_cadastro()
        try:
            data_nascimento = datetime.datetime.strptime(dados_jogador["data_nascimento"], "%d/%m/%Y")
        except ValueError:
            self.__tela_jogador.mostra_mensagem("Formato de data de nascimento inválido. Tente novamente.")
            self.cadastra_jogador()
            return

        for jogador in self.jogadores:
            if dados_jogador["nome"] == jogador.nome and data_nascimento == jogador.data_nascimento:
                self.__tela_jogador.mostra_mensagem("Jogador já cadastrado!")
                self.__controlador_sistema.abre_opcoes()
                return

        jogador = Jogador(dados_jogador["nome"], data_nascimento, dados_jogador["senha"],pontuacao=0)
        self.__jogador_dao.add(jogador)
        self.__tela_jogador.mostra_mensagem("\nCadastro realizado com sucesso!")
        self.__tela_jogador.mostra_mensagem("Faça Login para jogar! \n")
        
    def estah_cadastrado(self, nome, senha):
        for jogador in self.jogadores:
            if jogador.nome == nome:
                if jogador.senha == senha:
                    return jogador
                else:
                    self.__tela_jogador.mostra_mensagem("Senha Incorreta!")
                    return None
        self.__tela_jogador.mostra_mensagem(f"O jogador {nome} não está cadastrado!") 
        return None
    
    def faz_login(self):
        dados_login = self.__tela_jogador.abre_login()
        if dados_login == 'Encerrar Sistema':
            if not self.__controlador_sistema.encerra_sistema():
                self.faz_login()
        if dados_login == 'Voltar':
            return 'Voltar'      
        recebe_nome, recebe_senha = dados_login["recebe_nome"], dados_login["recebe_senha"]
        jogador = self.estah_cadastrado(recebe_nome, recebe_senha)
        return jogador

    
    
    def altera_cadastro(self):
        self.lista_jogadores()
        jogador = self.faz_login()
        if jogador == "Voltar":
            return self.abre_opcoes_cadastro()
        if jogador is not(None):
            opcao = self.__tela_jogador.opcoes_alteracao()
            if opcao == 1:  # Alterar senha
                nova_senha = self.__tela_jogador.recebe_nova_senha()
                jogador.senha = nova_senha
                self.__tela_jogador.mostra_mensagem("Senha alterada com sucesso!")
            elif opcao == 2:  # Alterar nome
                novo_nome = self.__tela_jogador.recebe_novo_nome()
                jogador.nome = novo_nome
                self.__tela_jogador.mostra_mensagem("Nome alterado com sucesso!")
            elif opcao == 3:  # Alterar data de nascimento
                nova_data_nascimento = self.__tela_jogador.recebe_nova_data_nascimento()
                try:
                    jogador.data_nascimento = datetime.datetime.strptime(nova_data_nascimento, "%d/%m/%Y")
                    self.__tela_jogador.mostra_mensagem("Data de nascimento alterada com sucesso!")
                except ValueError:
                    self.__tela_jogador.mostra_mensagem("Formato de data de nascimento inválido.")
                    self.altera_cadastro()
            else:
                self.__tela_jogador.mostra_mensagem("Opção inválida. Alteração cancelada.")   
            self.__controlador_sistema.abre_opcoes()
        else:
            self.altera_cadastro()

    def remove_jogador(self):
        self.lista_jogadores()
        jogador = self.estah_cadastrado()
        if jogador is not(None):
            self.__jogador_dao.remove(jogador)
            self.__tela_jogador.mostra_mensagem("Jogador removido!")
            self.lista_jogadores()
            self.__controlador_sistema.abre_opcoes()
        else:
            self.remove_jogador()

    def atualiza_jogador(self, jogador):
        self.__jogador_dao.add(jogador)

    def adiciona_jogo(self, jogador, jogo):
        jogador.jogos.append(jogo)
        self.atualiza_jogador(jogador)


    def ordena_ranking(self):
        jogadores_ordenados = sorted(self.jogadores, key=lambda jogador: jogador.pontuacao, reverse=True)
        return self.__tela_jogador.mostra_ranking(jogadores_ordenados)

    def lista_jogadores(self):
        lista_jogadores = []
        for jogador in self.jogadores:
            lista_jogadores.append(jogador.nome)
        return self.__tela_jogador.mostra_lista_jogadores(lista_jogadores)
    

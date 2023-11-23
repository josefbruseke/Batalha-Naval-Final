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
                            2: self.remove_jogador,
                            3: self.altera_cadastro,
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
        
    def pega_jogador_por_nome_e_senha(self, nome: str, senha: str):
        for jogador in self.jogadores:
            if jogador.nome == nome and jogador.senha == senha:
                return jogador
        return None

    def altera_cadastro(self):
        for jogador in self.jogadores:
            print(jogador.nome, jogador)
        dados = self.__tela_jogador.seleciona_jogador()
        jogador = self.pega_jogador_por_nome_e_senha(dados["nome"], dados["senha"])
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
                    self.__tela_jogador.mostra_mensagem("Formato de data de nascimento inválido. Alteração cancelada.")
            else:
                self.__tela_jogador.mostra_mensagem("Opção inválida. Alteração cancelada.")   
            self.atualiza_jogador(jogador)
            self.__controlador_sistema.abre_opcoes()
        else:
            self.__tela_jogador.mostra_mensagem("Jogador não encontrado!")
            self.__controlador_sistema.abre_opcoes()

    def remove_jogador(self):
        self.lista_jogadores()
        dados = self.__tela_jogador.seleciona_jogador()
        jogador = self.pega_jogador_por_nome_e_senha(dados["nome"], dados["senha"])
        if jogador is not(None):
            self.__jogador_dao.remove(jogador)
            self.__tela_jogador.mostra_mensagem("Jogador removido!")
            self.lista_jogadores()
            self.__controlador_sistema.abre_opcoes()
        else:
            self.__tela_jogador.mostra_mensagem("Jogador não encontrado!")
            self.__controlador_sistema.abre_opcoes()

    def historico_jogador(self, jogador):
        lista_jogos = jogador.jogos
        for jogo in lista_jogos:
            print(jogo.id)


    def atualiza_jogador(self, jogador):
        self.__jogador_dao.add(jogador)

    def adiciona_jogo(self, jogador, jogo):
        jogador.jogos.append(jogo)
        self.atualiza_jogador(jogador)


    def ordena_ranking(self):
        jogadores_ordenados = sorted(self.jogadores, key=lambda jogador: jogador.pontuacao, reverse=True)
        return self.__tela_jogador.mostra_ranking(jogadores_ordenados)

    def lista_jogadores(self):
        for jogador in self.jogadores:
            self.__tela_jogador.mostra_mensagem(f"nome: {jogador.nome}")

    def estah_cadastrado(self, nome, senha):
        for jogador in self.jogadores:
            if jogador.nome == nome and jogador.senha == senha: 
                return jogador
        return False

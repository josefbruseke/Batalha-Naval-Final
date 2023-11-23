class TelaJogador:
    def recebe_cadastro(self):
        print("------REALIZA CADASTRO------")
        nome = input("Digite seu nome: ")
        data_nascimento = input("Digite sua data de nascimento (DD/MM/AAAA): ")
        senha = input("Digite a senha: ")
        return {"nome": nome, "data_nascimento": data_nascimento, "senha": senha}
    
    def seleciona_jogador(self):
        nome = input("Digite o nome do Jogador: ")
        senha = input("Digite a senha: ")
        return {"nome": nome, "senha": senha}
    
    def opcoes_cadastro(self):
        print("------CADASTRO------")
        print("Selecione a opção desejada")
        print("1 - Fazer Cadastro")
        print("2 - Remover Cadastro")
        print("3 - Alterar Cadastro")
        print("0 - Voltar")
        print("--------------------")
        opcao = int(input("Escolha a opção: "))
        return opcao

    def opcoes_alteracao(self):
        print("-------ALTERAÇÃO-------")
        print("1 - Alterar senha")
        print("2 - Alterar nome")
        print("3 - Alterar data de nascimento")
        print("0 - voltar")
        print("-----------------------")
        opcao = int(input("Escolha a opção: "))
        return opcao
    
    def recebe_nova_senha(self):
        nova_senha = input("Digite sua nova senha: ")
        return nova_senha
    
    def recebe_novo_nome(self):
        novo_nome = input("Digite seu novo nome: ")
        return novo_nome

    def recebe_nova_data_nascimento(self):
        nova_data_nascimento = input("Digite sua nova data_de_nascimento: ")
        return nova_data_nascimento

    def mostra_historico(self):
        pass

    def mostra_pontuacao(self):
        pass
    
    def mostra_lista_jogadores(self):
        pass
 
    def mostra_mensagem(self, msg):
        print(msg)

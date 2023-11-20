class TelaJogo:
    def recebe_login(self):
        print("------LOGIN-------")
        recebe_nome = input("Digite seu nome: ")
        recebe_senha = input("Digite sua senha: ")
        return{"recebe_nome": recebe_nome, "recebe_senha": recebe_senha}

    def mostra_resultado_jogo(self):
        pass

    def mostra_resultado_rodada(self, jogador, resultado):
        print(f"{jogador} {resultado} o tiro")

    def mostra_opcoes(self):
        print("------MENU JOGO------")
        print("Selecione a opção desejada")
        print("1 - Iniciar partida")
        print("2 - Ver ranking")
        print("0 - Voltar")
        print("---------------------")
        opcao = int(input("Escolha a opção: "))
        return opcao

    def mostra_resultados(self, duracao, vencedor, pontuacao_jogador, pontuacao_computador):
        print("------RESULTADOS------")
        print(f"Duração da partida: {duracao}")
        print(f"O vencedor da partida foi o: {vencedor}")
        print(f"Pontuação do jogador: {pontuacao_jogador}")
        print(f"Pontuação do computador: {pontuacao_computador}")
        print("---------------------")
    
    def mostra_opcoes_final(self):
        print("------------------------------")
        print("Selecione a sua opção final:")
        print("1 - Iniciar um novo jogo")
        print("2 - Voltar para o Menu Jogo")
        print("0 - Encerrar o sistema")
        print("------------------------------")
        opcao = int(input("Escolhe a opção: "))
        return opcao

    def mostra_mensagem(self, msg):
        print(msg)

    def voltar(self):
        opcao = input("Deseja voltar para o meu inicial? [S/N] ").upper()
        return opcao
class TelaSistema:
    def mostra_opcoes(self):
        print("------MENU INICIAL------")
        print("Selecione a opção desejada")
        print("1 - Login")
        print("2 - Cadastro")
        print("3 - Ranking")
        print("0 - Encerrar o sistema")
        opcao = int(input("Escolha a opção: "))
        return opcao

    def mostra_mensagem(self, msg):
        print(msg)
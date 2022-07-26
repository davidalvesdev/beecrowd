def exibir(dados_exibicao):
    dados_exibicao = sorted(dados_exibicao)

    dados_exibicao = [str(dado) for dado in dados_exibicao]

    mensagem = ' '.join(dados_exibicao)
    print(mensagem)


dados = input()

dados = [int(n) for n in dados.split()]

while True:

    try:
        acao = input().split()

        if acao[0] == "encerrar":
            exibir(dados)
            break

        if acao[0] == "exibir":
            exibir(dados)

        if acao[0] == "adicionar":
            dados.append(int(acao[1]))

        if acao[0] == "remover":

            achou_dado = False
            acao[1] = int(acao[1])
            for dado in dados:
                if dado == acao[1]:
                    achou_dado = True

            if achou_dado:
                dados.remove(acao[1])
            else:
                print(f"código {acao[1]} não encontrado")
    except EOFError:
        break
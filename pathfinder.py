from time import sleep


class No(object):

    def __init__(self, pai=None, posicao=None):
        self.pai = pai
        self.posicao = posicao

        self.g = 0
        self.h = 0
        self.f = 0


def a_estrela(labr, inicio, fim, num_linhas):

    no_fim = No(None, inicio)
    no_inicio = No(None, fim)

    abertos = []
    fechados = []

    abertos.append(no_inicio)

    while len(abertos) > 0:

        no_atual = abertos[0]
        indice_atual = 0
        for item in abertos:
            if item.f < no_atual.f:
                no_atual = item
                indice_atual = abertos.index(no_atual)

        abertos.pop(indice_atual)
        fechados.append(no_atual)

        if no_atual.posicao == no_fim.posicao:
            final(labr, no_atual, inicio, num_linhas)
            return

        filhos = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                no_posicao = (no_atual.posicao[0] + i, no_atual.posicao[1] + j)

                if no_posicao[0] > (len(labr) - 1) or no_posicao[0] < 0 or no_posicao[1] > (len(labr[0]) - 1) or no_posicao[1] < 0:
                    continue

                if labr[no_posicao[0]][no_posicao[1]] != 0:
                    continue

                filhos.append (No(no_atual, no_posicao))

        for filho in filhos:

            filho.g = no_atual.g + 1
            filho.h = ((filho.posicao[0] - no_fim.posicao[0]) ** 2) + ((filho.posicao[1] - no_fim.posicao[1]) ** 2)
            filho.f = filho.g + filho.h

            abertos.append(filho)


def final(labr, no_atual, inicio, num_linhas):
    caminho = []
    atual = no_atual
    while atual is not None:
        caminho.append(atual.posicao)
        atual = atual.pai
    mostra_labr(labr, caminho, inicio, num_linhas)
    return


def mostra_labr(labr, caminho, inicio, num_linhas):
    pos_ant = inicio
    for pos in caminho:
        labr[pos_ant[0]][pos_ant[1]] = 0
        labr[pos[0]][pos[1]] = 'º'
        pos_ant = pos

        for i in range(num_linhas):
            print(labr[i])
        print('\n\n')
        sleep(1)
    print ("\033[33mcaminho:\033[m \n{}\n\n".format(caminho))


def verifica(labr, inicio, fim, num_lin, num_col):
    if len(labr) != num_lin or len(labr[0]) != num_col:
        print('numero de linhas ou colunas esta errado')
        exit()
    for i in range(2):
        if inicio[i] < 0 or fim[i] < 0 or inicio[i] > num_lin or fim[i] > num_lin or inicio[i] > num_col or fim[i] > num_col:
            print("erro nos valores de entrada")
            exit()


def main():
    '''
    num_lin = 5
    num_col = 5

    labr = [[0, 1, 1, 1, 1],
            [0, 0, 1, 1, 1],
            [0, 1, 1, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0]]

    inicio = (0, 0)
    fim = (4, 4)
    '''
    num_lin = 8
    num_col = 7
    
    labr = [[0, 1, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 1, 1, 0],
            [0, 0, 0, 1, 1, 1, 0],
            [0, 1, 0, 1, 1, 1, 0],
            [0, 1, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 1, 0, 0],
            [0, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 0]]

    inicio = (0, 0)
    fim = (7, 6)

    verifica(labr, inicio, fim, num_lin, num_col)
    a_estrela(labr, inicio, fim, num_lin)


if __name__ == '__main__':
    main()
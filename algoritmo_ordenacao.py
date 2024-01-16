from typing import *
# Class de ordenação e pesquisa binaria dentro de listas de inteiros
# Parametro: Conjunto(lista de inteiros), Ordenação(1:Ordenada; 0:Não ordenada), Sentido(1:Crescente; -1:Decrescente)


class ALGORITMOS_BINARIOS:

    def __init__(self, conjunto: list, ordenacao: int, sentido: int):
        self.conjunto = conjunto
        self.comprimento = len(self.conjunto)
        if ordenacao == 1:
            self.ord = True
        else:
            self.ord = False
        self.sentido = sentido

    def pesquisa(self, n: int) -> bool and int:

        if self.ord and self.sentido == 1:  # Ordenação da lista de forma crescente
            a = 0
            b = self.comprimento-1
            while a < b:
                if n < self.conjunto[a + ((b-a) // 2)+1]:
                    b = a + ((b-a) // 2)
                elif n == self.conjunto[a + ((b-a)//2)+1]:
                    return True, (a + ((b-a)//2)+1)
                else:
                    a += (b-a) // 2
                if b-a == 1 and n != (self.conjunto[a] or self.conjunto[b]):
                    return False
            return True, a

        elif self.ord and self.sentido == -1:   # Ordenação com lista de forma decrescente
            a = 0
            b = self.comprimento - 1
            while a < b:
                if n > self.conjunto[a + ((b - a) // 2) + 1]:
                    b = a + ((b - a) // 2)
                elif n == self.conjunto[a + ((b - a) // 2) + 1]:
                    return True, (a + ((b - a) // 2) + 1)
                else:
                    a += (b - a) // 2
                if b - a == 1 and n != (self.conjunto[a] or self.conjunto[b]):
                    return False
            return True, a

        else:
            raise ValueError("Lista não ordenada!")

    def isertion_sort_cres(self, n: int):

        if n == -1:  # Organizacao de forma crescente com n igual ao valor do sentido necessario
            for k in range(1, self.comprimento):
                j = k
                while j > 0:
                    if self.conjunto[j] > self.conjunto[j-1]:
                        self.conjunto[j], self.conjunto[j-1] = self.conjunto[j-1], self.conjunto[j]
                    else:
                        j = 0
                    j -= 1
            self.ord = True
            self.sentido = -1

        elif n == 1:    # Organizacao de forma decrescente com n igual ao valor do sentido necessario
            for k in range(1, self.comprimento):
                j = k
                while j > 0:
                    if self.conjunto[j] < self.conjunto[j-1]:
                        self.conjunto[j], self.conjunto[j-1] = self.conjunto[j-1], self.conjunto[j]
                    else:
                        j = 0
                    j -= 1
            self.ord = True
            self.sentido = 1

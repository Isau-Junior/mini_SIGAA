"""
Implementação da classe Disciplina. A classe disciplina é a classe que quada os dados das displinas ministradas
pelos professores e cursada pelos alunos. no projeto MiniSIGAA
"""

class Disciplina:
    def __init__(self, ID='', Nome='',  Professor = '', Alunos = ''):
        self.__ID = ID
        self.__Nome = Nome
        self.__Professor = Professor
        self.__Alunos = Alunos

    def Set_aluno(self, Alunos):
        self.__Alunos = Alunos

    def Set_professor(self, Professor):
        self.__Professor = Professor

    def Set_nome(self, Nome):
        self.__Nome = Nome

    def Set_id(self, ID):
        self.__ID = ID

    
    def guarda_dados(self):
        arq = open('Dados_salvos/Disciplinas/'+str(self.__ID)+'.txt', 'w+')

        DadosParaSalvar = [self.__ID, self.__Nome, self.__Professor[0], self.__Professor[1]]

        for posisao in DadosParaSalvar:
            arq.write(str(posisao))
            arq.write('\t')

        for chave, nota in self.__Alunos.items():
            arq.write('\n')
            arq.write(str(chave[0]))
            arq.write('\t')
            arq.write(chave[1])
            arq.write('\t')
            arq.write(str(nota))
        arq.close()


    def PrintObjeto(self):
        print(self.__ID)
        print(self.__Nome)
        print(self.__Professor)
        print(self.__Alunos)

dicAlunos = {(20210073124, 'Isau'): 8, (20211239847, 'Wagner'): 8, (20213218974, 'Tateu'): 8}
Prof = (2022349586, 'Yuri')

poo = Disciplina()
poo.Set_id('DCO5362')
poo.Set_nome('Programacao orientada a objetos')
poo.Set_aluno(dicAlunos)
poo.Set_professor(Prof)
poo.PrintObjeto()

poo.guarda_dados()
    
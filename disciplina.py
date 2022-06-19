"""
Implementação da classe Disciplina. A classe disciplina é a classe que quada os dados das displinas ministradas
pelos professores e cursada pelos alunos. no projeto MiniSIGAA
"""
from manip_arq import Carregar_arquivo

pathDisciplinas = 'dados/disciplinas/'

class Disciplina:
    def __init__(self, ID='', Nome='',  Professor = '', Alunos = ''):
        self.__ID = ID
        self.__Nome = Nome
        self.__Professor = Professor
        self.__Alunos = Alunos

    #metodos para receber os atribudos do objeto
    def Set_alunos(self, Alunos):
        self.__Alunos = Alunos

    def Set_professor(self, Professor):
        self.__Professor = Professor

    def Set_nome(self, Nome):
        self.__Nome = Nome

    def Set_id(self, ID):
        self.__ID = ID

    #metodos que retornam os atributos do objeto
    def Get_id(self):
        return self.__ID

    def Get_nome(self):
        return self.__Nome

    def Get_professor(self):
        return self.__Professor

    def Get_aluno(self):
        return self.__Alunos

    # Metodos de manipulação de arquivos
    def Salvar_dados(self):
        arq = open(pathDisciplinas+str(self.__ID)+'.txt', 'w+')

        DadosParaSalvar = [self.__ID, self.__Nome, self.__Professor[0], self.__Professor[1]]

        for dado in DadosParaSalvar:
            arq.write(str(dado))
            arq.write('\t')

        for chave, nota in self.__Alunos.items():
            arq.write('\n')
            arq.write(str(chave[0]))
            arq.write('\t')
            arq.write(chave[1])
            arq.write('\t')
            arq.write(str(nota))
        arq.close()

    def Carregar_dados(self, ID):
        dados = Carregar_arquivo(pathDisciplinas, ID, 'r+')
        listaDadosDisciplina = dados.split('\n')

        dadosgerais = listaDadosDisciplina[0].split('\t')
        dadosgerais.pop()

        dadosalunos = listaDadosDisciplina[1::]
        dicAlunos = {}
        for aluno in dadosalunos:
            listaluno = aluno.split('\t')
            dicAlunos.update({(int(listaluno[0]), listaluno[1]): int(listaluno[2])})

        #print(listaDadosDisciplina, type(listaDadosDisciplina))
        #print(dadosgerais)
        #print(dicAlunos)
        self.Set_id(dadosgerais[0])
        self.Set_nome(dadosgerais[1])
        self.Set_professor((dadosgerais[2], dadosgerais[3]))
        self.Set_alunos(dicAlunos)


    def PrintObjeto(self):
        print(self.__ID)
        print(self.__Nome)
        print(self.__Professor)
        print(self.__Alunos)

dicAlunos = {(20210073124, 'Isau'): 8, (20211239847, 'Wagner'): 8}
Prof = (2022349586, 'Yuri')

poo = Disciplina()
poo.Set_id('DCO1030')
poo.Set_nome('Variavel aleatoria')
poo.Set_alunos(dicAlunos)
poo.Set_professor(Prof)
#poo.PrintObjeto()

poo.Salvar_dados()

#poo.Carregar_dados('DCO5362')
#poo.PrintObjeto()
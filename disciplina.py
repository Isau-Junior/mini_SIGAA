"""
Implementação da classe Disciplina. A classe disciplina é a classe que quada os dados das displinas ministradas
pelos professores e cursada pelos alunos. no projeto MiniSIGAA
"""
from mailbox import NotEmptyError
from manip_arq import Carregar_arquivo

pathDisciplinas = 'dados/disciplinas/'

class Disciplina:
    def __init__(self, ID='', Nome=''):
        self.__ID = ID
        self.__Nome = Nome
        self.__Professor = {}
        self.__Alunos = {}

    #metodos para receber os atribudos do objeto
    def Set_alunos(self, ID = '', nome = '', nota =''):
        self.__Alunos.update({ID: [nome, nota]})

    def Set_professor(self, ID = '', nome = ''):
        self.__Professor = (ID, nome)

    def Set_nome(self, Nome):
        self.__Nome = Nome

    def Set_id(self, ID):
        self.__ID = ID

    def Altera_nota(self, ID, nota):
        nome = self.__Alunos[ID]
        self.__Alunos[ID] = [nome[0], nota]

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
        with open(pathDisciplinas+str(self.__ID)+'.txt', 'w+') as arq:
            DadosParaSalvar = [self.__ID, self.__Nome, self.__Professor[0], self.__Professor[1]]

            for dado in DadosParaSalvar:
                arq.write(str(dado))
                arq.write(':')

            for chave, nome_nota in self.__Alunos.items():
                arq.write('\n')
                arq.write(str(chave))
                arq.write(':')
                arq.write(nome_nota[0])
                arq.write(':')
                arq.write(str(nome_nota[1]))

    def Carregar_dados(self, ID):
        dados = Carregar_arquivo(pathDisciplinas, ID, 'r+')
        listaDadosDisciplina = dados.split('\n')

        dadosgerais = listaDadosDisciplina[0].split(':')
        dadosgerais.pop()

        dadosalunos = listaDadosDisciplina[1::]
        dicAlunos = {}
        for aluno in dadosalunos:
            listaluno = aluno.split(':')
            self.Set_alunos(listaluno[0], listaluno[1], listaluno[2])

        del self.__Alunos['']

        #print(listaDadosDisciplina, type(listaDadosDisciplina))
        #print(dadosgerais)
        #print(dicAlunos)
        self.Set_id(dadosgerais[0])
        self.Set_nome(dadosgerais[1])
        self.Set_professor(dadosgerais[2], dadosgerais[3])


    def PrintObjeto(self):
        print(self.__ID)
        print(self.__Nome)
        print(self.__Professor)
        print(self.__Alunos)




poo = Disciplina()
poo.Set_id('DCO1032')
poo.Set_nome('POO')
poo.Set_alunos('', '', '')
poo.Set_alunos('123456789', 'Isau', '8')
poo.Set_professor('', '')
poo.PrintObjeto()

poo.Salvar_dados()

poo.Carregar_dados('DCO1032')
poo.Altera_nota('123456789', '7')
poo.PrintObjeto()
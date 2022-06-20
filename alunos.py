
from pessoa import Pessoa
from manip_arq import Buscar_arquivo

pathDisciplina_sistema = 'dados/disciplinas.txt'
pathHistorico = 'dados/alunos/historico_'

class Aluno(Pessoa):
    def __init__(self, ID='', Nome='', Senha='', dic_historico={}):
        super().__init__(ID, Nome, Senha)
        self.__dic_historico = dic_historico

    #Metodo para aluno poder escolher disciplina para se cadastrar
    def set_materias(self, ID_materia):
        with open(pathDisciplina_sistema, 'r') as file:
            conteudo_file = file.read()
            lista_disciplinas = conteudo_file.split('\n')
            lista_disciplinas.pop()

            dicDiciplinas = {}
            for disciplina in lista_disciplinas:
                dadosDisciplina = disciplina.split('\t')
                dicDiciplinas.update({dadosDisciplina[0]: dadosDisciplina[1]})

        cont = 0
        for chave in dicDiciplinas.keys():
            if ID_materia == chave:
                disciplina_valida = ID_materia
                cont += 1

        if cont == 0:
            print('Esta disciplina não esta cadastrada no sistema!!!')
        else:
            with open(pathHistorico + self.get_matricula() + '.txt', 'a') as file:
                file.write(ID_materia)
                file.write('\t')
                file.write(dicDiciplinas[ID_materia])
                file.write('\n')

    #Metodo para ler  e immprimir historico_ID.txt de cada aluno com as notas das respectivas disciplinas
    def get_historico(self):
        if Buscar_arquivo(pathHistorico+f'{self.get_matricula()}'):
            with open(pathHistorico + f'{self.get_matricula()}' + '.txt', 'r+') as file:
                file_conteudo = file.read()
                listaDisciplinas = file_conteudo.split('\n')
                listaDisciplinas.pop()

                for disciplina in listaDisciplinas:
                    dadosDisciplinas = disciplina.split('\t')
                    self.__dic_historico.update({dadosDisciplinas[0]: dadosDisciplinas[1]})

            # para cada disciplina do historico, verifica se exite nota do aluno cadastrada na respectiva disciplina
            notas = {}  
            for chave in self.__dic_historico.keys():
                with open(f'dados/disciplinas/{chave}.txt', 'r+') as file:
                    dados = file.read()
                    listaDadosDisciplina = dados.split('\n')

                    dadosalunos = listaDadosDisciplina[1::]
                    dicAlunos = {}
                    for aluno in dadosalunos:
                        listaluno = aluno.split('\t')
                        dicAlunos.update({int(listaluno[0]): int(listaluno[2])})
                    
                    for matricula_alunos in dicAlunos:
                        if matricula_alunos == int(self.get_matricula()):
                            notas.update({chave: dicAlunos[int(self.get_matricula())]})

                if chave in notas:
                    print(chave, self.__dic_historico[chave],notas[chave])
                else:
                    print(chave, self.__dic_historico[chave])
        else:
            print('Historico não encontrado')
    
    #Metodo para guardar informações do aluno:
    def salvar_dados(self):
        with open('dados/alunos/' + str(self.get_ID()) + '.txt', 'w+') as file:
            listadados = [self.get_ID(), self.get_nome(), self.get_senha(), self.get_data()]
            print(listadados)

            for dado in listadados:
                file.write(str(dado))
                file.write('\t')

    def carregar_dados(self, ID):
        arq = open('dados/alunos/'+str(ID)+'.txt', 'r')
        dados = arq.read()
        dados.replace('\n', ' ')
        dadosaluno = dados.split('\t')
        dadosaluno.pop()
        self.Set_matricula(dadosaluno[0])
        self.Set_nome(dadosaluno[1])
        self.Set_senha(dadosaluno[2])
        self.Set_DataUltimoAcesso(dadosaluno[3])
    
    #Metodo para imprimir a declaração do aluno
    def get_declaracao(self):
        print('-------------------- D E C L A R A Ç Ã O ------------------------')
        print('     Declaramos, para os fins que se fizerem necessários, que')
        print(f'{self.get_nome()} é aluno(a) REGULAR vinculado(a) a esta instituição,')
        print(f'sob a matricula: {self.get_matricula()}. Seu atual estado de matrícula')
        print('é CURSANDO.')
        print('-----------------------------------------------------------------')


if __name__ == '__main__': 
    Tadeu = Aluno()
    Tadeu.Set_nome('Tadeu')
    Tadeu.Set_ID('20211234')
    Tadeu.Set_senha('123456')

    print(Tadeu.get_nome(), type(Tadeu.get_nome()))
    print(Tadeu.get_ID(), type(Tadeu.get_ID()))
    print(Tadeu.get_senha(), type(Tadeu.get_senha()))

    #Tadeu.salvar_dados()
    #Tadeu.salvar_dados()
    #Tadeu.carregar_dados(20211234)
    #print(Tadeu.get_nome())
    #Tadeu.get_declaracao()
    #Tadeu.set_materias('DCO1031')
    #Tadeu.get_historico()

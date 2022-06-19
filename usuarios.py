import os
from manip_arq import *
from pessoa import Pessoa
#Usar o txt como sendo uma lista ou matriz

class Administrador(Pessoa):
    def __init__(self, ID = '', Nome = '', Senha = '', DataUltimoAcesso = ''):
        super().__init__(Nome, Senha, ID, DataUltimoAcesso)

    def Excluir_usuario(self, path, ID, modo):
        if modo == 1:
            path == 'dados/alunos'
        elif modo == 2:
            path == 'dados/professores'
        if Buscar_arquivo(path, ID):
            os.remove(path + '/' + ID + '.txt')
        else:
            print('Arquivo não encontrado')

    def Excluir_disciplina(self, path, ID):
        if Buscar_arquivo(path, ID):
            os.remove(path + '/' + ID + '.txt')
        else:
            print('Arquivo não encontrado')

        with open('Dados_salvos\Sistema\Disciplinas.txt', 'r') as arq:
            conteudoarq = arq.read()
            print(conteudoarq)
            lista_disciplinas = conteudoarq.split('\n')
            lista_disciplinas.pop()
            dicDiciplinas = {}
            for disciplina in lista_disciplinas:
                dadosDisciplina = disciplina.split('\t')
                dicDiciplinas.update({dadosDisciplina[0]:dadosDisciplina[1]})
            del dicDiciplinas[ID]

        with open('Dados_salvos/Sistema/Disciplinas.txt', 'w+') as arq:
            for disciplina in dicDiciplinas.keys():
                arq.write(disciplina)
                arq.write('\t')
                arq.write(dicDiciplinas[disciplina])
                arq.write('\n')

    def guardar_dado(self):
        info = [str(self.get_ID()), str(self.get_nome()), self.get_senha(), self.get_data()]
        file = open('dados/admin.txt', 'w+')
        for i in info:
            file.write(str(i))
            file.write('\n')
        file.close()

    def carregar_dados(self):
        file1 = open('dados/admin.txt', 'r')
        info = file1.readlines()
        aux = []
        for i in range(len(info)):
            aux.append(str(info[i].strip('\n')))
        self.Set_nome(aux[0])
        self.Set_ID(aux[1])
        self.Set_senha(aux[2])
        self.Set_DataUltimoAcesso(aux[3])
        file1.close()

class Professor(Pessoa):

    def __init__(self, ID = '', Nome='', Senha='',  Disciplinas = {}):
        super().__init__(ID, Nome, Senha)
        self.__Disciplinas = Disciplinas

    def guarda_disciplina(self):
        with open('dados/professores/' + self.get_ID()+ '.txt', 'a') as arq:
            for IDdisciplina in self.__Disciplinas:
                arq.write(IDdisciplina + '\t' + self.__Disciplinas[IDdisciplina])
                arq.write('\n')

    def mostrardisciplinas(self):
            print(self.__Disciplinas)

    def Set_Disciplina(self, ID):
        cont = 0
        with open('dados/disciplinas.txt', 'r') as temp_file:
            dados = temp_file.read()
            listadisciplinas = dados.split('\n')
            listadisciplinas.pop()
            dicDisciplinas = {}
            for disciplinas in listadisciplinas:
                tupladisciplina = disciplinas.split(' ')
                dicDisciplinas.update({tupladisciplina[0]:tupladisciplina[1]})
            for key in dicDisciplinas.keys():
                if ID == key:
                    self.__Disciplinas.update({key:dicDisciplinas[key]})
                    print(self.__Disciplinas)
                    cont += 1
            if cont == 0:
                print('Não existe essa disciplina')
                cont = 0

    def guardar_dado(self):
        self.gerar_DataUltimoAcesso()
        info = [str(self.get_ID()), str(self.get_nome()), self.get_senha(), self.get_data()]
        file = open(f'dados/professores/{self.get_ID()}.txt', 'w+')
        for i in info:
            file.write(str(i))
            file.write('\n')
        file.close()

    def carregar_dados(self):
        file1 = open(f'dados/professores/{self.get_ID()}.txt', 'r+')
        info = file1.readlines()
        aux = []
        for i in range(len(info)):
            aux.append(str(info[i].strip('\n')))
        self.Set_nome(aux[0])
        self.Set_ID(aux[1])
        self.Set_senha(aux[2])
        self.Set_DataUltimoAcesso(aux[3])
        file1.close()

"""
wagner = Professor('1234', 'Yuri', '123')
#wagner.guardar_dado()
wagner.carregar_dados()
wagner.PrintObjeto()
#wagner.PrintObjeto()
#wagner.addusuario('Yuri', '1234', '123')
#wagner.addusuario('Yuri', '1890', '123')
#wagner.adddisciplina('Teste', 'DCO5362')
#wagner.adddisciplina('Teste1', 'DCO5364')
#wagner.adddisciplina('Teste2', 'DCO5366')
#wagner.Excluir_disciplina('Dados_salvos\Disciplinas\DisciplinasID', 'DCO5362')
#wagner.lerprof('123')
#wagner.Set_login('Wagner.barboza.113')
#wagner.excluirprof('123')
#wagner1 = Professor('Wagner', '123', '12')
#wagner1.setlista('15')
#wagner1.Set_Disciplina('DCO1010')
#wagner1.guarda_disciplina()
#wagner1.mostrardisciplinas('15')
"""
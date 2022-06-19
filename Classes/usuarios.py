import os
import classpessoa
from datetime import datetime

#Usar o txt como sendo uma lista ou matriz

class Administrador(Pessoa):
    def __init__(self, Nome = '', Login = '', Senha = '', Matricula = '', DataUltimoAcesso = ''):
        super().__init__(self, Nome = '', Login = '', Senha = '', Matricula = '', DataUltimoAcesso = '')

    def addprof(self, nome, login, senha, ID):
        data = datetime.today()
        dados = [nome, login, senha, ID, data]
        with open(ID+'.txt', 'w') as temp_file:
            for item in dados:
                temp_file.write(str(item))
                temp_file.write('\t')

    def addaluno(self, nome, login, senha, ID):
        dados = [nome, login, senha, ID]
        with open('Alunos.txt', 'w') as temp_file:
            for item in dados:
                temp_file.write("%s " % item + '\n')

    def adddisciplina(self, nome, login, senha, ID):
        dados = [nome, login, senha, ID]
        with open('Disciplinas.txt', 'a') as temp_file:
            for item in dados:
                temp_file.write("%s " % item + '\n')

    def lerprof(self, ID):
            file = open(ID+'.txt', 'r')
            dados = file.readline()
            dados.replace('\n', ' ')
            dadosusuarios = dados.split('\t')
            dadosusuarios.pop()
            print(dadosusuarios)

    def excluirprof(self, ID):
        os.remove(ID+'.txt')

class Professor:

    def __init__(self, nome, login, senha, ID, acesso):
        self.nome = nome
        self.login = login
        self.senha = senha
        self.ID = ID
        self.acesso = acesso

    def verdisciplinas(self, ID):
        file = open('Disciplinas' + ID + '.txt', 'r')
        print(file.read())

    def darnota(self, ID, Disciplina, Nota):
        with open('Notas' + ID + '.txt', 'a') as temp_file:
            temp_file.write(Disciplina + ' ' + Nota + '\n')

    #def selecdisciplina(self):




wagner = Administrador('Wagner', 'Wagnerbbz', 123, 12, 'ADM')
wagner.addprof('Wagner', 'Wagnerbbz', '123', '16')
wagner.addprof('Yuri', 'Yuriufrn', '123', '123')
wagner.lerprof('123')
#wagner.excluirprof('123')
#wagner1 = Professor('Wagner', 'Wagnerbbz', 123, 12, 'Professor')
#wagner1.darnota('12', 'Algebra Linear', '10')
#wagner1.verdisciplinas('12')


'''
        def verdisciplinas(self, ID):
        file = open('Disciplinas' + ID + '.txt', 'r')
        print(file.read())

    def cadastrardisciplina(self, ID, Disciplina):
        with open('Disciplinas' + ID + '.txt', 'a') as temp_file:
            temp_file.write(Disciplina + '\n')

    def vernotas(self, ID):
    
   Função para transformar o txt de 1 linha em lista 
    
   file = open(ID+'.txt', 'r')
            dados = file.readline()
            dados.replace('\n', ' ')
            dadosusuarios = dados.split('\t')
            dadosusuarios.pop()
            print(dadosusuarios) 
    
    '''
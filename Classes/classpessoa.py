"""
Implementação da classe pessoa. A classe pessoa é a classe pai das classes Aluno, Professora e Adiministrador
no projeto MiniSIGAA
"""
import os
import datetime

class Pessoa:
    def __init__(self, Nome = '', Login = '', Senha = '', Matricula = '', DataUltimoAcesso = ''):
        self.__Nome = Nome
        self.__Login = Login
        self.__Senha = Senha
        self.__Matricula = Matricula
        self.__DataUltimoAcesso = DataUltimoAcesso

    def Set_nome(self, Nome):
        self.__Nome = Nome

    def Set_login(self, Login):
        self.__Login = Login

    def Set_senha(self, Senha):
        self.__Senha = Senha
    
    def Set_matricula(self, Matricula):
        if Matricula.isdigit():
            self.__Matricula = Matricula
        else:
            raise ValueError("Amatricula do usuario deve conter apenas números")

    def Set_DataUltimoAcesso(self, DataUltimoAcesso=''):
        if DataUltimoAcesso == '':
            data = datetime.datetime.now()
            self.__DataUltimoAcesso = data.strftime("%d/%m/%y %H:%M:%S")
        else:
            self.__DataUltimoAcesso = DataUltimoAcesso


    def get_nome(self):
        return self.__Nome

    def get_login(self):
        return self.__Login

    def get_senha(self):
        return self.__Senha

    def get_matricula(self):
        return self.__Matricula

    def PrintObjeto(self):
        print(self.__Nome)
        print(self.__Login)
        print(self.__Matricula)
        print(self.__Senha)
        print(self.__DataUltimoAcesso)

    def guarda_dados(self):
        arq = open('Dados_salvos/'+str(self.__Matricula)+'.txt', 'w+')

        DadosParaSalvar = [self.__Matricula, self.__Nome, self.__Login, self.__Senha, self.__DataUltimoAcesso]

        for posisao in DadosParaSalvar:
            arq.write(posisao)
            arq.write('\t')

        arq.close

    def carregar_dados(self, matricula):
        arq = open('Dados_salvos/'+matricula+'.txt', 'r')
        dados = arq.readline()
        dados.replace('\n', ' ')
        dadosusuarios = dados.split('\t')
        dadosusuarios.pop()
        self.Set_matricula(dadosusuarios[0])
        self.Set_nome(dadosusuarios[1])
        self.Set_login(dadosusuarios[2])
        self.Set_senha(dadosusuarios[3])
        self.Set_DataUltimoAcesso(dadosusuarios[4])

    def excluir_usuario(self):
        os.remove('Dados_salvos/'+self.__Matricula+'.txt')

#Isau = Pessoa()
#Isau.Set_nome('Isau')
#Isau.Set_login('Isau.Junior')
#Isau.Set_senha('123456')
#Isau.Set_matricula('202232648')
#Isau.Set_DataUltimoAcesso()

#Isau.PrintObjeto()
#Isau.guarda_dados()

#Isau.carregar_dados('202232648')
#Isau.excluir_usuario()

#Isau.PrintObjeto()

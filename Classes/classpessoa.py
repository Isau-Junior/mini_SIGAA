"""
Implementação da classe pessoa. A classe pessoa é a classe pai das classes Aluno, Professora e Adiministrador
no projeto MiniSIGAA
"""
import datetime

class Pessoa:
    def __init__(self, Nome = '', Senha = '', Matricula = ''):
        self.__Nome = Nome
        self.__Senha = Senha
        self.__Matricula = Matricula
        self.__DataUltimoAcesso = ''

    def Set_nome(self, Nome):
        self.__Nome = Nome

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

    def get_senha(self):
        return self.__Senha

    def get_matricula(self):
        return self.__Matricula

    def get_DataUltimoAcesso(self):
        return self.__DataUltimoAcesso

    def PrintObjeto(self):
        print(self.__Nome)
        print(self.__Matricula)
        print(self.__Senha)
        print(self.__DataUltimoAcesso)

    def guarda_dados(self):
        arq = open('Dados_salvos/'+str(self.__Matricula)+'.txt', 'w+')

        DadosParaSalvar = [self.__Matricula, self.__Nome, self.__Senha, self.__DataUltimoAcesso]

        for posisao in DadosParaSalvar:
            arq.write(posisao)
            arq.write('\t')

        arq.close


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

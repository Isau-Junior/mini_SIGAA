"""
Implementação da classe pessoa. A classe pessoa é a classe pai das classes Aluno, Professora e Adiministrador
no projeto MiniSIGAA
"""
import datetime

class Pessoa:
    def __init__(self, ID = '', Nome = '', Senha = '', DataUltimoAcesso = ''):
        self.__ID = ID
        self.__Nome = Nome
        self.__Senha = Senha
        self.__DataUltimoAcesso = DataUltimoAcesso

    def Set_ID(self, ID):
        self.__ID = ID

    def Set_nome(self, Nome):
        self.__Nome = Nome

    def Set_senha(self, Senha):
        self.__Senha = Senha

    def Set_DataUltimoAcesso(self, DataUltimoAcesso):
        self.__DataUltimoAcesso = DataUltimoAcesso


    def gerar_DataUltimoAcesso(self, DataUltimoAcesso=''):
        if DataUltimoAcesso == '':
            data = datetime.datetime.now()
            self.__DataUltimoAcesso = data.strftime("%d/%m/%y %H:%M:%S")
        else:
            self.__DataUltimoAcesso = DataUltimoAcesso

    def get_ID(self):
        return self.__ID

    def get_nome(self):
        return self.__Nome

    def get_senha(self):
        return self.__Senha

    def get_data(self):
        return self.__DataUltimoAcesso

    def PrintObjeto(self):
        print(self.__ID)
        print(self.__Nome)
        print(self.__Senha)
        print(self.__DataUltimoAcesso)

    #def guarda_dados(self):
        #arq = open('dados/'+str(self.__ID)+'.txt', 'w+')
        #DadosParaSalvar = [self.#__Matricula, self.__Nome, self.__Login, self.__Senha, self.__DataUltimoAcesso]
        #for posisao in DadosParaSalvar:
            #arq.write(posisao)
            #arq.write('\t')
        #arq.close

    #def carregar_dados(self, matricula):
        #arq = open('dados/'+matricula+'.txt', 'r')
        #dados = arq.readline()
        #dados.replace('\n', ' ')
        #dadosusuarios = dados.split('\t')
        #dadosusuarios.pop()
        #self.Set_matricula(dadosusuarios[0])
        #self.Set_nome(dadosusuarios[1])
        #self.Set_login(dadosusuarios[2])
        #self.Set_senha(dadosusuarios[3])
        #self.Set_DataUltimoAcesso(dadosusuarios[4])

"""
isau = Pessoa()
isau.Set_nome('Ricardo')
isau.Set_ID('D1323')
isau.Set_senha('123213213')
isau.PrintObjeto()
"""
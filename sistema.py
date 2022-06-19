#from usuarios import Administrador, Professor

class Sistema:
    disciplinas = {}
    def __init__(self):
        self.qnt_usuarios = 0
        self.qnt_disciplinas = 0
        self.ID_admin ='admin'
        self.senha_admin ='admin'

    #testado
    def get_qnt_usuarios(self):
        return self.qnt_usuarios

    #testado
    def get_qnt_disciplinas(self):
        return self.qnt_disciplinas

    #testado
    def set_ID_admin(self, ID):
        self.ID_admin = ID

    # testado
    def set_senha_admin(self, senha):
        self.senha_admin = senha

    # testado
    def log_admin(self, ID, senha):
        if(self.ID_admin == ID and self.senha_admin == senha):
            return True
        else:
            return False

    # testado
    def gerar_IDusuaio(self):
            self.qnt_usuarios += 1
            ID = '20220' + str(self.qnt_usuarios)
            return ID

    # testado
    def gerar_IDdisciplina(self):
            self.qnt_disciplinas += 1
            ID = '22D' + str(self.qnt_disciplinas)
            return ID

    #testado
    def set_disciplinas(self, nome, ID):
        self.disciplinas.update({ID: nome})

    # testado
    def print_disciplinas(self):
        print(self.disciplinas)

    #testado
    def del_disciplina(self, ID):
        self.disciplinas.pop(ID)

    #testado
    def get_disciplina(self, ID):
        print(self.disciplinas[ID])

    def gravarSistema(self):
        # salva infor sistema
        info = [str(self.qnt_usuarios), str(self.qnt_disciplinas), self.ID_admin, self.senha_admin]
        with open('dados/sistema.txt', 'w+') as file:
            for i in info:
                file.write(str(i))
                file.write('\n')

    # testado
    def gravarDisciplinas(self):
        # salva info disciplinas
        with open("dados/disciplinas.txt", 'w+') as file:
            for key, value in self.disciplinas.items():
                file.write('%s:%s\n' % (key, value))

    # testado
    def gravarTudo(self): #grava tudo, informações sistema e discionario disciplinas
        #salva infor sistema
        info1 = [str(self.qnt_usuarios), str(self.qnt_disciplinas), self.ID_admin, self.senha_admin]
        with open('dados/sistema.txt', 'w+') as file1:
            for i in info1:
                file1.write(str(i))
                file1.write('\n')

        #salva info disciplinas
        with open("dados/disciplinas.txt", 'w+') as file2:
            for key, value in self.disciplinas.items():
                file2.write('%s:%s\n' % (key, value))

    # testado
    def carregarSistema(self):
        with open('dados/sistema.txt', 'r') as file:
            info = file.readlines()

            aux = []
            for i in range(len(info)):
                aux.append(str(info[i].strip('\n')))

            self.qnt_usuarios = int(aux[0])
            self.qnt_disciplinas = int(aux[1])
            self.ID_admin = aux[2]
            self.ID_admin = aux[3]

    # testado
    def carregarDisciplinas(self):
        with open('dados/disciplinas.txt', 'r') as file:
            info = file.readlines()

            aux = []
            for i in range(len(info)):
                aux.append(str(info[i].strip('\n')))

            for i in range(len(aux)):
                aux2 = aux[i].split(':')
                self.disciplinas[aux2[0]] = aux2[1]

    # testado
    def carregarTudo(self):
            with open('dados/sistema.txt', 'r') as file1:
                info = file1.readlines()
                aux = []
                for i in range(len(info)):
                    aux.append(str(info[i].strip('\n')))

                self.qnt_usuarios = int(aux[0])
                self.qnt_disciplinas = int(aux[1])
                self.ID_admin = aux[2]
                self.ID_admin = aux[3]

            with open('dados/disciplinas.txt', 'r') as file2:
                info = file2.readlines()

                aux = []
                for i in range(len(info)):
                    aux.append(str(info[i].strip('\n')))

                for i in range(len(aux)):
                    aux2 = aux[i].split(':')
                    self.disciplinas[aux2[0]] = aux2[1]




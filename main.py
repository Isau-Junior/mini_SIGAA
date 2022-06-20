import os
from validacoes import validar_inputs
from menus import *
from manip_arq import Excluir_arquivo

# Importando as classes
from sistema import Sistema
from alunos import Aluno
from usuarios import Administrador, Professor
from disciplina import Disciplina


pathAlunos = 'dados/alunos/'
pathDisciplinas = 'dados/disciplinas/'
pathProfessores = 'dados/professores/'

clear = lambda: os.system('cls')
sistema = Sistema()
sistema.carregarTudo()
ficar = True #boleano para controlar o laço principal
while(ficar): #laço principal
  menu_inicial()
  opc_geral = validar_inputs('Indique a opção desejada: ', 1, 4)
  clear() #Função para linpar o terminal

  match opc_geral:
    case 1:
      ficar_admin = True
      while(ficar_admin):
        menu_login()
        opc_admin = validar_inputs('Indique a opção desejada: ', 1, 2)

        match opc_admin:
          case 1:
              ID = input("Insira seu ID: ")
              senha = input("insira sua senha: ")
              logado = sistema.log_admin(ID,senha)
              clear() #Função para linpar o terminal

              if logado:
                adm = Administrador() #cria o objeto administrador
                adm.carregar_dados() #carrega todos os dados do arquivo
                func_admin = True
                while func_admin:
                  menu_admin()
                  func = validar_inputs('Indique a opção desejada: ',1, 5)
                  clear()

                  # dicionar um novo usuario ao sitema
                  if func == 1: 
                    menu_escolher_usuarios()
                    usu = validar_inputs('Indique o tipo de usuario: ', 1, 2)

                    # adiciona um novo aluno ao sitema
                    if usu == 1:
                      aluno = Aluno()
                      aluno.Set_ID(sistema.gerar_IDusuaio())
                      aluno.Set_nome(input('Informe o nome do aluno que deseja cadastrar: '))
                      aluno.Set_senha('123456') # cria uma senha inicial temporaria para o primeiro acesso do aluno
                      clear()

                      print('O seguinte Aluno será cadastrado no sitema:')
                      print('Matricula:'.ljust(10), 'nome:'.center(15), 'senha:'.rjust(10))
                      matricula = aluno.get_ID()
                      nome = aluno.get_nome()
                      senha = aluno.get_senha()
                      print(matricula.ljust(10), nome.center(15), senha.rjust(10))

                      menu_confirma_cadastro()
                      conf = validar_inputs('Indique a opção desejada: ', 1, 2)
                      if conf == 1:
                        aluno.salvar_dados()
                        clear()
                        print('Aluno cadastrado com sucesso!!!!')
                      else:
                        print('Cadastro de novo Aluno cancelado!!!')

                    # adiciona um novo professor ao sistema
                    else:
                      professor = Professor()
                      professor.Set_ID(sistema.gerar_IDusuaio())
                      professor.Set_nome(input('Informe o nome do novo professor que deseja cadastrar: '))
                      professor.Set_senha('123456') # cria uma senha inicial temporaria para o primeiro acesso do professor
                      clear()

                      print('O seguinte professor será cadastrado no sitema:')
                      print('Matricula:'.ljust(10), 'nome:'.center(15), 'senha:'.rjust(10))
                      matricula = professor.get_ID()
                      nome = professor.get_nome()
                      senha = professor.get_senha()
                      print(matricula.ljust(10), nome.center(15), senha.rjust(10))

                      menu_confirma_cadastro()
                      conf = validar_inputs('Indique a opção desejada: ', 1, 2)
                      if conf == 1:
                        professor.salvar_dados()
                        clear()
                        print('Professor cadastrado com sucesso!!!!')
                      else:
                        print('Cadastro de novo professor cancelado!!!!')
                      
                  #exclui usuarios
                  elif func == 2:
                    menu_escolher_usuarios()
                    usu = validar_inputs('Indique o tipo de usuario: ', 1, 2)

                    if usu == 1:
                      matricula = input('Digite a matricula do aluno que deseja excluir do sistema: ')
                      adm.Excluir_usuario(pathAlunos, matricula, 1)
                    else:
                      matricula = input('Digite a matricula do professor que deseja excluir do sistema: ')
                      adm.Excluir_usuario(pathProfessores, matricula, 2)

                  elif func == 3: # Registra um disciplina no sistema
                    cabecalho('Criar disciplina')
                    nome = input('Digite o nome da disciplina que deseja criar: ')
                    ID_diciplina = sistema.gerar_IDdisciplina()
                    sistema.set_disciplinas(nome, ID_diciplina)
                    clear()

                    print('A seguinte didciplina será cadastrado no sitema:')
                    print('ID da disciplina:'.ljust(20), 'nome:'.center(30))
                    nome = sistema.get_disciplina(ID_diciplina)
                    print(ID_diciplina.ljust(20), nome.center(30))

                    menu_confirma_cadastro()
                    conf = validar_inputs('Indique a opção desejada: ', 1, 2)
                    if conf == 1:
                      sistema.gravarDisciplinas()
                      clear()
                      print('Disciplina cadastrada com sucesso!!!!')
                    else:
                      print('Cadastro de disciplina cancelado!!!')

                  #excluir disciplina
                  elif func == 4:
                    cabecalho('Excluir Disciplina')
                    ID_disciplina = input("Insira o ID da disciplina que deseja excluir: ")
                    clear()

                    print('A disciplina a seguinte será excluida do sistema junto com todos os dados desta:')
                    print('ID da disciplina:'.ljust(20), 'nome:'.center(30))
                    nome = sistema.get_disciplina(ID_disciplina)
                    print(ID_disciplina.ljust(20), nome.center(30))

                    menu_confirmar_ação()
                    conf = validar_inputs('Indique a opção desejada: ', 1, 2)
                    if conf == 1:
                      adm.Excluir_disciplina(pathDisciplinas, ID_disciplina)
                      clear()
                      print('Disciplina excluida com sucesso!!!!')
                    else:
                      print('Ação cancelada!!')

                  #sair das funções administradoras
                  else:
                    func_admin = False

              #caso incorretas
              else:
                print("Login ou senha incorrentos... Tente novamente!")
                break

          #encerrando o login do administradir e retornado ao menu princial
          case 2:
            clear()
            #print("Encerrando a função administradora... Retornando ao menu inicial")
            ficar_admin = False
    case 2:
      #Doscente
      pass
    case 3:
      #Discete
      pass
    case 4:
        print("Finalizando o sistema... Obrigado!!")
        sistema.gravarSistema()
        ficar = False

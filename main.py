from sistema import Sistema
from pessoa import Pessoa
from alunos import Aluno
from usuarios import Administrador, Professor
from disciplina import Disciplina


sistema = Sistema()
sistema.carregarTudo()
ficar = True #boleano para controlar o laço principal
while(ficar): #laço principal
  print("1 - Usuario Administrador")
  print("2 - Usuario Doscente")
  print("3 - Usuario Discente")
  print("4 - Sair do sistema")
  opc_geral = int(input("Indique a opção desejada: "))
  match opc_geral:
    case 1:
      ficar_admin = True
      while(ficar_admin):
        print("1 - Login")
        print("2 - Voltar ao menu principal")
        opc_admin = int(input("Indique a opção desejada: "))
        match opc_admin:
          case 1:
              ID = input("Insira seu ID: ")
              senha = input("insira sua senha: ")
              logado = sistema.log_admin(ID,senha)
              if logado:
                print("Você esta logado")
                #adm = administador() #cria o objeto administrador
                #adm.carregar_dados("administrador.txt") #carrega todos os dados do arquivo
                func_admin = True
                while(func_admin):
                  print("1 - Adicionar Usuario")
                  print("2 - Excluir usuario")
                  print("3 - Adicionar Disciplina")
                  print("4 - Excluir Disciplina")
                  print("5 - Sair do sistema")
                  func = int(input("Indique a opção desejada: "))
                  if func == 1:
                    print("1 - Aluno")
                    print("2 - Professor")
                    usu = int(input("Indique o tipo de usuario: "))
                    if usu == 1:
                      usuario = Aluno()

                    elif usu == 2:
                      usuario = Professor()
                    #else:
                      #print("Opção indicada não existe...")
                      #break

                    # Inicia os valores do objeto usuario pela primeira vez

                    # Gera o ID do usuario
                    ID = sistema.gerar_IDusuaio()
                    usuario.Set_ID(ID)
                    print(usuario.get_ID())
                    # Adm digita o nome do usuario
                    nome = input("Insira o nome do usuario: ")
                    # adm digita a senha
                    senha = input("Insira a senha do usuario: ")
                    usuario.set_senha(senha)

                    #salva todas as informações no arquivo do usuario
                    usuario.guardar_dados()

                  #exclui usuarios
                  elif func == 2:
                    #pega o ID do usuario que deseja excluir
                    ID = input("Insira o ID do Usuario que deseja excluir: ")
                    #exclui o arquivo
                    adm.excluir_arquivo(ID)

                  #cria disciplina
                  elif func == 3:

                    #cria o objeto disciplina
                    disciplima = disciplina()

                    #gera o ID para a disciplina
                    ID = oSistema.gerar_IDdisciplina()
                    disciplina.set_ID(ID)

                    #pega o nome da disciplina
                    nome = input("Insira o nome da disciplina: ")
                    disciplina.set_nome(nome)

                    #salva todas as infomações no arquivo da disciplina
                    disciplina.guardar_dados()

                  #excluir disciplina
                  elif func == 4:
                    # pega o ID da disciplina que deseja excluir
                    ID = input("Insira o ID da disciplina que deseja excluir: ")
                    # exclui o arquivo
                    adm.excluir_arquivo(ID)

                  #sair das finções administradoras
                  elif func == 5:
                    print("Função administrador encerrada!!")

                    #encera o laço das funções
                    func_admin = False

                  #indica que o administrador escolheu uma função inexistente
                  else:
                    print("Opção indicada não existe...")

              #caso incorretas
              else:
                print("Login ou senha incorrentos... Tente novamente!")
                break

          #encerrando o login do administradir e retornado ao menu princial
          case 2:
            print("Encerrando a função administradora... Retornando ao menu inicial")
            ficar_admin = False
    #case 2:
      #Doscente
    #case 3:
      #Discete
    case 2:
        print("Finalizando o sistema... Obrigado!!")
        ficar = False

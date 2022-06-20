"""
Quarda todas as telas de menu do sistema
"""
from pprint import pprint


simbolo = '-'
multiplicador = 50

print_divisor = lambda: print(str(simbolo)*multiplicador)

def cabecalho(texto):
    print_divisor()
    print(texto.title().center(50))
    print_divisor()

def menu_inicial():
    cabecalho('menu inicial')
    print("1 - Usuario Administrador")
    print("2 - Usuario Doscente")
    print("3 - Usuario Discente")
    print("4 - Sair do sistema")
    print_divisor()

def menu_login():
    cabecalho('menu de login')
    print("1 - Login")
    print("2 - Voltar ao menu principal")
    print_divisor()

def menu_admin():
    cabecalho('menu do administrador')
    print("1 - Adicionar Usuario")
    print("2 - Excluir usuario")
    print("3 - Adicionar Disciplina")
    print("4 - Excluir Disciplina")
    print("5 - Logout")
    print_divisor()

def menu_escolher_usuarios():
    print_divisor()
    print("1 - Aluno")
    print("2 - Professor")
    print_divisor()

def menu_confirma_cadastro():
    print_divisor()
    print("1 - confirmar cadastro")
    print("2 - cancelar")
    print_divisor()

def menu_confirmar_ação():
    cabecalho('Tem certeza que deseja executar esta ação?')
    print('1 - Sim')
    print('2 - Não')
    print_divisor()

if __name__ == '__main__':
    menu_inicial()
    menu_login()
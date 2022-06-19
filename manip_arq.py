import os

def Buscar_arquivo(path, nome):
    """
    Verifica se o arquivo existe no caminho informado.

    param: path -> Caminho onde se encontra o arquivo (tipo: str)
    param: nome -> Nome do arquivo 
    return: retorna True se o arquivo existir e False caso não exista
    """
    try:
        with open(path + '/' + nome + '.txt'):
            pass
    except FileNotFoundError:
        return False
    else:
        return True

def Excluir_arquivo(path, nome):
    """
    Exclui o arquivo .txt cujo nome e caminho foram informados 

    param: path -> Camonho onde se encontra o arquivo (tipo: str)
    param: nome -> Nome do arquivo (tipo: str)
    """
    if Buscar_arquivo(path, nome):
        os.remove(path + '/' + nome + '.txt')
    else:
        print('Arquivo não encontrado')

def Carregar_arquivo(path, nome, modo):
    """
    Abre um arquivo .txt com o nome indicado e salvo no caminho indicado e retorna essesdados para ser
    carregado em uma variavel

    param: path -> Caminho do arquivo (tipo: str)
    param: nome -> Nome do arquivo sem extenção (tipo: str)
    param: modo -> Modo no qual se deseja abrir o arquivo (tipo: str)
    return: retorna uma string como os dados contidos no arquivo
    """
    with open(path+ '/' + nome +'.txt', modo) as arq:
            return arq.read()
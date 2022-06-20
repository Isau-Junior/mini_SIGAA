"""
Funções responsaveis por validar os dados que entram no sistema
"""

def validar_inputs(msg, min, max):
    valido = False
    while not valido:
        dado = input(msg)
        if dado.isdigit():
            if int(dado)>= min and int(dado)<= max:
                return int(dado)
                valido = True
            else:
                print('opção invalida!!!!!')
        else:
            print('opção invalida!!!!!')
        

if __name__ == '__main__':
    dado = validar_inputs(1, 4)
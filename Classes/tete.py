
disc = {"DCO1062": 'Programacao orientada a objetos', "DCO1050": 'Comunicações sem fio', "DCO1030": 'Variaveis aleatorias'}

with open('Dados\Sistema\Disciplina_sistema.txt', 'a') as arq:
    for chave in disc.keys():
        arq.write(chave)
        arq.write('\t')
        arq.write(disc[chave])
        arq.write('\n')
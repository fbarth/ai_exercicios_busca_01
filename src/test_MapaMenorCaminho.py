from Map import *
from aigyminsper.search.SearchAlgorithms import AEstrela
import time

Map.createArea()

testes = [
    ['a','c',2],
    ['c','c',0],
    ['a','g',7],
    ['f','g',1],
    ['c','a',2],
    ['d','c',2],
    ['d','g',5]
]

def test():

    for conf in testes:
        # cidade atual, custo para chegar na cidade, operacao, cidade objetivo
        state = Map(conf[0], 0, '', conf[1])
    result = return_result(state)
    if result != None:
        print(result.show_path())
    else:
        print('Nao achou solucao')
    assert result.g == conf[2]


from aigyminsper.search.SearchAlgorithms import BuscaCustoUniforme, BuscaLargura,BuscaProfundidadeIterativa,BuscaProfundidade,BuscaGananciosa,AEstrela
from U2 import *

#Para bono, edge, adam, larry e lanterna FALSE significa lado esquerdo do rio
#TRUE significa lado direito do rio
#Tem que passar do lado esquerdo pro direito

def test_menor_caminho():
    state = U2State(False, False, False, False, False, ' ')
    result = return_solution(state)
    assert result.g <= 17
    print(result.show_path())

def test_resolvido():
    "Teste em que o problema ja começa resolvido, ou seja, todos já estão do lado certo da ponte então o custo é 0"
    state = U2State(True, True, True, True, True, '')
    result = return_solution(state)
    assert result.g == 0

def test_sem_solucao():
    "Teste em que ninguem consegue atravessar a ponte pois a lanterna está do outro lado"
    state = U2State(False, False, False, False, True, ' ')
    result = return_solution(state)
    assert result == None

def test_larry():
    '''
        Este teste leva em consideração que o integrante mais lento da banda é o unico que se
        encontra do lado da ponte em que esta a lampada, tornando então o tempo de resolução do
        problema maior do que o tempo em que os mesmos tem para chegar ao show.
    '''

    state = U2State(False, False, False, True, True, ' ')
    result = return_solution(state)
    assert result.g > 17



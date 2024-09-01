from aigyminsper.search.SearchAlgorithms import BuscaCustoUniforme, BuscaLargura,BuscaProfundidadeIterativa,BuscaProfundidade,BuscaGananciosa,AEstrela
from Map import Map

def test_partida_eq_chegada():

    # city, cost, op, goal
    state = Map('a', 0, '', 'a')
    assert(state.is_goal())

def test_partida_dif_chegada():

    state = Map('a', 0, '', 'b')
    assert(not state.is_goal())

def test_custo_0():

    state = Map('a', 0, '', 'a')
    assert(state.cost() == 0)

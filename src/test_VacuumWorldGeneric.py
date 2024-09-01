from aigyminsper.search.SearchAlgorithms import BuscaLargura
from aigyminsper.search.SearchAlgorithms import BuscaProfundidade
from aigyminsper.search.SearchAlgorithms import BuscaProfundidadeIterativa
from VacuumWorldGeneric import *

def test_largura_simple_1_path():
    print("\n#### Largura Simples 1 ####")
    file_map_path = "data/vacuum_simple_1.txt"
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, "")
    result = return_solution(state)
    print(f"Solução = {result.show_path()}")
    print("\n")
    assert result.show_path() == " ; limpar"

def test_largura_simple_2_path():
    print("\n#### Largura Simples 2 Path ####")
    file_map_path = "data/vacuum_simple_2.txt"
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, "")
    result = return_solution(state)
    print(f"Solução = {result.show_path()}")
    print("\n")
    assert result.show_path() == " ; dir ; dir ; baixo ; limpar"

def test_largura_simple_3_path():
    print("\n#### Largura Simples 3 ####")
    file_map_path = "data/vacuum_simple_3.txt"
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, "")
    result = return_solution(state)
    print(f"Solução = {result.show_path()}")
    print("\n")
    assert (
    result.show_path()
    == " ; dir ; dir ; baixo ; limpar ; dir ; limpar ; baixo ; limpar"
)

def test_largura_simple_0():
    print('\n#### Largura Simples 0 ####')
    file_map_path = 'data/vacuum_simple_0.txt'
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, '')
    result = return_solution(state)
    print(f'Solução = {result.show_path()}')
    print('\n')
    assert result.show_path() == ""

def test_largura_simple_1():
    print('\n#### Largura Simples 1 ####')
    file_map_path = 'data/vacuum_simple_1.txt'
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, '')
    result = return_solution(state)
    print(f'Solução = {result.show_path()}')
    print('\n')
    assert result.g == 1

def test_largura_simple_2():
    print('\n#### Largura Simples 2 ####')
    file_map_path = 'data/vacuum_simple_2.txt'
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, '')
    result = return_solution(state)
    print(f'Solução = {result.show_path()}')
    print('\n')
    assert result.g == 4

def test_largura_simple_3():
    print('\n#### Largura Simples 3 ####')
    file_map_path = 'data/vacuum_simple_3.txt'
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, '')
    result = return_solution(state)
    print(f'Solução = {result.show_path()}')
    print('\n')
    assert result.g == 8

def test_largura_simple_4():
    print('\n#### Largura Simples 4 ####')
    file_map_path = 'data/vacuum_simple_4.txt'
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, '')
    result = return_solution(state)
    print(f'Solução = {result.show_path()}')
    print('\n')
    assert result.g == 10

def test_largura_simple_6():
    print('\n#### Largura Simples 6 ####')
    file_map_path = 'data/vacuum_simple_6.txt'
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, '')
    result = return_solution(state)
    print(f'Solução = {result.show_path()}')
    print('\n')
    assert result.g == 23

def test_largura_simple_7():
    print('\n#### Largura Simples 7 ####')
    file_map_path = 'data/vacuum_simple_7.txt'
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, '')
    result = return_solution(state)
    print(f'Solução = {result.show_path()}')
    print('\n')
    assert result.g == 16

def test_largura_simple_8():
    print('\n#### Largura Simples 8 ####')
    file_map_path = 'data/vacuum_simple_8.txt'
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, '')
    result = return_solution(state)
    print(f'Solução = {result.show_path()}')
    print('\n')
    assert result.g == 14

def test_largura_simple_9():
    print('\n#### Largura Simples 9 ####')
    file_map_path = 'data/vacuum_simple_9.txt'
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, '')
    result = return_solution(state)
    print(f'Solução = {result.show_path()}')
    print('\n')
    assert result.g == 15

def test_largura_simple_10():
    print('\n#### Largura Simples 10 ####')
    file_map_path = 'data/vacuum_simple_10.txt'
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, '')
    result = return_solution(state)
    print(f'Solução = {result.show_path()}')
    print('\n')
    assert result.g == 5

def test_largura_simple_11():
    print('\n#### Largura Simples 11 ####')
    file_map_path = 'data/vacuum_simple_11.txt'
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, '')
    result = return_solution(state)
    print(f'Solução = {result.show_path()}')
    print('\n')
    assert result.g == 14

def test_largura_simple_12():
    print('\n#### Largura Simples 12 ####')
    file_map_path = 'data/vacuum_simple_12.txt'
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, '')
    result = return_solution(state)
    print(f'Solução = {result.show_path()}')
    print('\n')
    assert result.g == 6

def test_largura_simple_13():
    print('\n#### Largura Simples 13 ####')
    file_map_path = 'data/vacuum_simple_13.txt'
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, '')
    result = return_solution(state)
    print(f'Solução = {result.show_path()}')
    print('\n')
    assert result.g == 8

def test_largura_simple_14():
    print('\n#### Largura Simples 14 ####')
    file_map_path = 'data/vacuum_simple_14.txt'
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, '')
    result = return_solution(state)
    print(f'Solução = {result.show_path()}')
    print('\n')
    assert result.g == 7

def test_largura_simple_15():
    print('\n#### Largura Simples 15 ####')
    file_map_path = 'data/vacuum_simple_15.txt'
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, '')
    result = return_solution(state)
    print(f'Solução = {result.show_path()}')
    print('\n')
    assert result.g == 14

def test_largura_simple_16():
    print('\n#### Largura Simples 16 ####')
    file_map_path = 'data/vacuum_simple_16.txt'
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, '')
    result = return_solution(state)
    print(f'Solução = {result.show_path()}')
    print('\n')
    assert result.g == 10

def test_largura_simple_17():
    print('\n#### Largura Simples 17 ####')
    file_map_path = 'data/vacuum_simple_17.txt'
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, '')
    result = return_solution(state)
    print(f'Solução = {result.show_path()}')
    print('\n')
    assert result.g == 11


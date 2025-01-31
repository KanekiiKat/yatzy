import pytest
from src.yatzy1 import Yatzy

# These unit tests can be run using the py.test framework
# available from http://pytest.org/

@pytest.mark.chance
def test_chance():
    '''
    Se eliminaron las variables innecesarias.
    Se convirtieron los argumentos de entrada a una lista.
    '''
    assert 15 == Yatzy.chance(3, 2, 4, 5, 1)
    assert 16 == Yatzy.chance(3, 3, 4, 5, 1)
    assert 5 == Yatzy.chance(1, 1, 1, 1, 1)

@pytest.mark.yatzy
def test_yatzy():
    '''
    Renombrado para acortar el nombre del test y darle mayor claridad.
    Eliminadas variables redundantes para simplificar los tests.
    Añadidos test adicionales.
    '''
    assert 50 == Yatzy.yatzy(1, 1, 1, 1, 1)
    assert 50 == Yatzy.yatzy(4, 4, 4, 4, 4)
    assert 50 == Yatzy.yatzy(5, 5, 5, 5, 5)
    assert 50 == Yatzy.yatzy(6, 6, 6, 6, 6)
    assert 0 == Yatzy.yatzy(6, 6, 6, 6, 3)
    assert 0 == Yatzy.yatzy(5, 6, 5, 6, 5)

@pytest.mark.ones
def test_ones():
    '''
    Cambiamos el nombre al mismo de la función de la clase.
    Colocamos el resultado del primer assert.
    Convertimos todos los argumentos en una lista.
    '''
    assert 1 == Yatzy.ones(1, 2, 3, 4, 5)
    assert 2 == Yatzy.ones(1, 2, 1, 4, 5)
    assert 0 == Yatzy.ones(6, 2, 2, 4, 5)
    assert 4 == Yatzy.ones(1, 2, 1, 1, 1)

@pytest.mark.twos
def test_twos():
    '''
    Renombrado test.
    Añadido test adicional.
    '''
    assert 0 == Yatzy.twos(1, 4, 5, 3, 4)
    assert 4 == Yatzy.twos(1, 2, 3, 2, 6)
    assert 10 == Yatzy.twos(2, 2, 2, 2, 2)

@pytest.mark.threes
def test_threes():
    '''
    Añadidos tests nuevos
    '''
    assert 0 == Yatzy.threes(1, 4, 5, 2, 4)
    assert 6 == Yatzy.threes(1, 2, 3, 2, 3)
    assert 12 == Yatzy.threes(2, 3, 3, 3, 3)
    assert 15 == Yatzy.threes(3, 3, 3, 3, 3)

@pytest.mark.fours
def test_fours():
    '''
    Añadidos tests nuevos
    '''
    assert 0 == Yatzy.fours(1, 1, 5, 2, 2)
    assert 12 == Yatzy.fours(4, 4, 4, 5, 5)
    assert 8 == Yatzy.fours(4, 4, 5, 5, 5)
    assert 4 == Yatzy.fours(4, 5, 5, 5, 5)

@pytest.mark.fives
def test_fives():
    '''
    Añadidos tests nuevos
    '''
    assert 0 == Yatzy.fives(1, 4, 6, 2, 4)
    assert 10 == Yatzy.fives(4, 4, 4, 5, 5)
    assert 15 == Yatzy.fives(4, 4, 5, 5, 5)
    assert 20 == Yatzy.fives(4, 5, 5, 5, 5)

@pytest.mark.sixes
def test_sixes():
    '''
    Añadidos tests nuevos
    '''
    assert 0 == Yatzy.sixes(4, 4, 4, 5, 5)
    assert 12 == Yatzy.sixes(4, 4, 4, 6, 6)
    assert 6 == Yatzy.sixes(4, 4, 6, 5, 5)
    assert 18 == Yatzy.sixes(6, 5, 6, 6, 5)

@pytest.mark.pair
def test_one_pair():
    '''
    Añadidos tests nuevos
    '''
    assert 0 == Yatzy.score_pair(6, 4, 3, 5, 2)
    assert 2 == Yatzy.score_pair(1, 4, 2, 5, 1)
    assert 6 == Yatzy.score_pair(3, 4, 3, 5, 6)
    assert 10 == Yatzy.score_pair(5, 3, 3, 3, 5)
    assert 12 == Yatzy.score_pair(5, 3, 6, 6, 5)
    assert 6 == Yatzy.score_pair(3, 3, 3, 3, 1)


@pytest.mark.pairs
def test_two_Pair():
    '''
    Añadido test nuevo
    '''
    assert 16 == Yatzy.two_pair(3, 3, 5, 4, 5)
    assert 18 == Yatzy.two_pair(3, 3, 6, 6, 6)
    assert 0 == Yatzy.two_pair(3, 3, 6, 5, 4)
    assert 0 == Yatzy.two_pair(6, 3, 6, 6, 6)

@pytest.mark.three_kind
def test_three_of_a_kind():
    '''
    Añadido test nuevo
    '''
    assert 0 == Yatzy.three_of_a_kind(2, 1, 3, 4, 5)
    assert 9 == Yatzy.three_of_a_kind(3, 3, 3, 4, 5)
    assert 15 == Yatzy.three_of_a_kind(5, 3, 5, 4, 5)
    assert 9 == Yatzy.three_of_a_kind(3, 3, 3, 3, 5)

@pytest.mark.four_kind
def test_four_of_a_kind():
    assert 12 == Yatzy.four_of_a_kind(3, 3, 3, 3, 5)
    assert 20 == Yatzy.four_of_a_kind(5, 5, 5, 4, 5)
    assert 12 == Yatzy.four_of_a_kind(3, 3, 3, 3, 3)
    assert 0 == Yatzy.four_of_a_kind(3, 3, 3, 2, 1)

@pytest.mark.small
def test_smallStraight():
    assert 15 == Yatzy.smallStraight(1, 2, 3, 4, 5)
    assert 15 == Yatzy.smallStraight(2, 3, 4, 5, 1)
    assert 0 == Yatzy.smallStraight(1, 2, 2, 4, 5)

@pytest.mark.large
def test_largeStraight():
    assert 20 == Yatzy.largeStraight(6, 2, 3, 4, 5)
    assert 20 == Yatzy.largeStraight(2, 3, 4, 5, 6)
    assert 0 == Yatzy.largeStraight(1, 2, 2, 4, 5)

@pytest.mark.full
def test_fullHouse():
    '''
    Añadidos tests adicionales
    '''
    assert 0 == Yatzy.fullHouse(5, 5, 5, 5, 5)
    assert 18 == Yatzy.fullHouse(6, 2, 2, 2, 6)
    assert 22 == Yatzy.fullHouse(6, 2, 6, 2, 6)
    assert 0 == Yatzy.fullHouse(2, 3, 4, 5, 6)
    assert 0 == Yatzy.fullHouse(5, 5, 5, 5, 4)

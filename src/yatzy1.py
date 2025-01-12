from src.pips import Pips

class Yatzy:

    ZERO = 0
    FIFTY = 50

    @staticmethod
    def chance(*dice_rolls):
        '''
        Para ahorrar lineas de código, en el propio return se hizo la suma total (Mover todo a una sola línea).
        Se convirtieron los argumentos de entrada a una tupla.
        '''
        return sum(dice_rolls)


    @staticmethod
    def yatzy(*dice_rolls):
        '''
        El cóodigo era innecesariamente complejo para la operación que estaba tratando de devolver.
        Se ha simplificado a una operación más barata y comprensible.
        '''
        return Yatzy.FIFTY if dice_rolls.count(dice_rolls[0]) == 5 else Yatzy.ZERO


    @staticmethod
    def ones(*dice_rolls):
        '''
        Cambiado el argumento de entrada por una tupla.
        Todos los ifs reemplazados por un método count.
        '''
        ONE = Pips.ONE.value
        return dice_rolls.count(ONE)


    @staticmethod
    def twos(*dice_rolls):
        '''
        Cambiado argumento de entrada por una tupla
        Ifs reemplazados por método count a modo de simplificación.
        '''
        TWO = Pips.TWO.value
        return dice_rolls.count(TWO) * TWO


    @staticmethod
    def threes(*dice_rolls):
        '''
        Cambiado argumento de entrada por una tupla
        Ifs reemplazados por método count a modo de simplificación.
        '''
        THREE = Pips.THREE.value
        return dice_rolls.count(THREE) * THREE


    def __init__(self, d1=0, d2=0, d3=0, d4=0, _5=0):
        self.dice = [0] * 5
        self.dice[0] = d1
        self.dice[1] = d2
        self.dice[2] = d3
        self.dice[3] = d4
        self.dice[4] = _5


    @staticmethod
    def fours(*dice_rolls):
        '''
        Dejamos de emplear el self.
        Cambiado el argumento de entrada.
        '''
        FOUR = Pips.FOUR.value
        return dice_rolls.count(FOUR) * FOUR


    @staticmethod
    def fives(*dice_rolls):
        FIVE = Pips.FIVE.value
        return dice_rolls.count(FIVE) * FIVE


    @staticmethod
    def sixes(*dice_rolls):
        SIX = Pips.SIX.value
        return dice_rolls.count(SIX) * SIX


    @staticmethod
    def score_pair(*dice_rolls):
        '''
        Refactorizado en una comprensión.
        Cambiado argumento de entrada.
        '''
        return max([die * 2 for die in dice_rolls if dice_rolls.count(die) >= 2], default=Yatzy.ZERO)


    @staticmethod
    def two_pair(*dice_rolls):
        '''
        Refactorización en comprensiones.
        Cambiado el argumento de entrada a una tupla.
        '''
        pairs = [die * 2 for die in set(dice_rolls) if dice_rolls.count(die) >= 2 and dice_rolls.count(die) < 4]
        return sum(pairs) if len(pairs) == 2 else Yatzy.ZERO


    @staticmethod
    def four_of_a_kind(_1, _2, d3, d4, d5):
        tallies = [0] * 6
        tallies[_1 - 1] += 1
        tallies[_2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        for i in range(6):
            if (tallies[i] >= 4):
                return (i + 1) * 4
        return 0

    @staticmethod
    def three_of_a_kind(d1, d2, d3, d4, d5):
        t = [0] * 6
        t[d1 - 1] += 1
        t[d2 - 1] += 1
        t[d3 - 1] += 1
        t[d4 - 1] += 1
        t[d5 - 1] += 1
        for i in range(6):
            if (t[i] >= 3):
                return (i + 1) * 3
        return 0

    @staticmethod
    def smallStraight(d1, d2, d3, d4, d5):
        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        if (tallies[0] == 1 and
                tallies[1] == 1 and
                tallies[2] == 1 and
                tallies[3] == 1 and
                tallies[4] == 1):
            return 15
        return 0

    @staticmethod
    def largeStraight(d1, d2, d3, d4, d5):
        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        if (tallies[1] == 1 and
                tallies[2] == 1 and
                tallies[3] == 1 and
                tallies[4] == 1
                and tallies[5] == 1):
            return 20
        return 0

    @staticmethod
    def fullHouse(d1, d2, d3, d4, d5):
        tallies = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1

        for i in range(6):
            if (tallies[i] == 2):
                _2 = True
                _2_at = i + 1

        for i in range(6):
            if (tallies[i] == 3):
                _3 = True
                _3_at = i + 1

        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0

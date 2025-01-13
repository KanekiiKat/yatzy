from src.pips import Pips

class Yatzy:

    ZERO = 0
    FIFTY = 50
    FIFTEEN = 15
    TWENTY = 20

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
    def three_of_a_kind(*dice_rolls):
        '''
        Refactorizado a una comprensión de lista,
        Camiado el argumento de entrada.
        '''
        threes = [die * 3 if dice_rolls.count(die) >= 3 else Yatzy.ZERO for die in dice_rolls]
        return threes[0]


    @staticmethod
    def four_of_a_kind(*dice_rolls):
        '''
        Refactorizado a una comprensión de lista
        Camiado el argumento de entrada.
        '''
        four = [die * 4 if dice_rolls.count(die) >= 4 else Yatzy.ZERO for die in dice_rolls]
        return four[0]


    @staticmethod
    def smallStraight(*dice_rolls):
        '''
        Refactorizado a una comprensión.
        Camiado el argumento de entrada.
        '''
        return Yatzy.FIFTEEN if Pips.SIX.value not in set(dice_rolls) and len(set(dice_rolls)) == 5 else Yatzy.ZERO


    @staticmethod
    def largeStraight(*dice_rolls):
        '''
        Refactorizado a una comprensión.
        Camiado el argumento de entrada.
        '''
        return Yatzy.TWENTY if Pips.ONE.value not in set(dice_rolls) and len(set(dice_rolls)) == 5 else Yatzy.ZERO


    @staticmethod
    def fullHouse(*dice_rolls):
        '''
        Refactorizado a una comprensión.
        Camiado el argumento de entrada.
        '''
        return sum(die if dice_rolls.count(die) >= 2 and dice_rolls.count(die) <= 3 else Yatzy.ZERO for die in dice_rolls)
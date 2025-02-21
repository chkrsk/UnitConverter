class UnitConverter():

    @staticmethod
    def convert_weight(weight: float, unit_a: str, unit_b: str) -> str:
        unitsW = {
            'mg': 1000000,
            'g': 1000,
            'dag': 100,
            'kg': 1,
            't': 0.001,
        }
        # if unit_a is the same as unit_b, we don't calculate
        if unit_a != unit_b:
            # unit conversation formula
            return f'{(weight / unitsW[unit_a]) * unitsW[unit_b]} {unit_b}'
        else:
            return str(weight)

    @staticmethod
    def convert_length(length, unit_a, unit_b) -> str:
        unitsL = {
            'mm': 1000,
            'cm': 100,
            'dm': 10,
            'm': 1,
            'km': 0.001,
        }
        # if unit_a is the same as unit_b, we don't calculate
        if unit_a != unit_b:
            # unit conversation formula
            return f'{(length / unitsL[unit_a]) * unitsL[unit_b]} {unit_b}'
        else:
            return str(length)

from airplane import Airplane


class AirbusA380(Airplane):
    @staticmethod
    def get_name():
        return 'Airbus A370'

    @staticmethod
    def seating_plan():
        return range(1, 51), 'ABCDEGHJK'
from airplane import Airplane


class Boeing737Max(Airplane):
    @staticmethod
    def get_name():
        return 'Boeing 737Max'

    @staticmethod
    def seating_plan():
        return range(1, 26), 'ABCDEG'
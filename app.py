class Flight:
    def __init__(self, flight_number, airplane):
        self.airplane = airplane
        self.flight_number = flight_number

    def get_airline(self):
        return self.flight_number[:2]

    def get_number(self):
        return self.flight_number[2:]

    def get_plane(self):
        return self.airplane.get_name()


class Airplane:
    def get_num_seats(self):
        rows, seats = self.seating_plan()
        return len(rows) * len(seats)


class Boeing737Max(Airplane):
    @staticmethod
    def get_name():
        return 'Boeing 737Max'

    @staticmethod
    def seating_plan():
        return range(25), 'ABCDEG'


class AirbusA380(Airplane):
    @staticmethod
    def get_name():
        return 'Airbus A370'

    @staticmethod
    def seating_plan():
        return range(50), 'ABCDEGHJK'


boeing = Boeing737Max()
airbus = AirbusA380()
print(airbus.get_num_seats())
f = Flight('BA128', boeing)
# print(f.get_airline())
# print(f.get_number())
# print(f.get_plane())

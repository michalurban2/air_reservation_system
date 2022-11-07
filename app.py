from pprint import pprint as pp  #import z paczki pprint


class Flight:  # Deklaracja klasy Flight  KamelCase
    def __init__(self, flight_number, airplane): # metoda klasy przyjmuje 2 parametry/
        self.airplane = airplane               # deklaracja funkcji
        # które setuja dla każdej instancji klay
        self.flight_number = flight_number

        rows, letters = self.airplane.seating_plan() # wywołanie metody seating_plan w kontekscie kalsy
        self.seats = [None] + [{letter: None for letter in letters} for _ in rows]
                            # dict comprahention w list comprahention
        # do pola obiktu przypisujemy liste ze słownikami, kontatunacja dwóch list, wiec jest to lista wsłlwników

    def get_airline(self): # metoda klasy get_airplane
        return self.flight_number[:2]  # wraca pierwsze 2 znaki z pola flight_number

    def get_number(self): # metoda klasy get_number
        return self.flight_number[2:] # zwraca od drugiego elementu do konca  z pola flight number

    def get_plane(self): # deklaracja metody
        return self.airplane.get_name() # zwraca wynik pola obiektu air plane, get_name

    def _parse_seats(self, seat):  # deklaracja metody, dostep do modyfikatora pro
        letter = seat[-1]  # deklaracja zmiennej letter
        rows, letters = self.airplane.seating_plan()  # deklarujemy 2 zmienne, za pomoca tuple unpackin przypisujemy wartosci

        if letter not in letters: # instrukcja warunkkowa
            raise ValueError(f'Invalid seat letter: {letter}')

        row_text = seat[:-1]

        try: # za pomocą klauzuli try except
            row = int(row_text)
        except ValueError:
            raise ValueError(f'Invalid row number: {row_text}') #przechwytujemy za pomoco ValueError

        if row not in rows:
            raise ValueError(f'Row: {row} not in rows range') # jeslo True to, na podstawie klasy Value error rzucamy stringa

        return row, letter # zwracamy tuple

    def allocate_passenger(self, seat, passenger): # deklaracja metody
        row, letter = self._parse_seats(seat) #deklaracja metody, wynik metody prase_seats

        if self.seats[row][letter] is not None: # sprawdzamy czy z pola obiektu seats[pobieramy element] is not none
            raise ValueError(f'Seat {seat} is already taken') # podnosimy wyjatek z zawartościa ztringa

        self.seats[row][letter] = passenger # z pola obiektu[pobieramy element][pobieramy element ]

    def relocate_passenger(self, old_seat, new_seat):
        old_row, old_letter = self._parse_seats(old_seat) # tuple packing

        if self.seats[old_row][old_letter] is None:
            raise ValueError(f'Old seat is empty: {old_seat}') # podnosimy wyjatek z f'string'

        new_row, new_letter = self._parse_seats(new_seat)

        if self.seats[new_row][new_letter] is not None:
            raise ValueError(f'New seat {new_seat} is already taken')

        self.seats[new_row][new_letter] = self.seats[old_row][old_letter]
        self.seats[old_row][old_letter] = None

    def count_empty_seats(self): # deklaracja funkcji
        return sum(sum(1 for passenger in row.values() if passenger is None)for row in self.seats if row is not None)
        # dla każdego elementu pola seats
        # ^ to jest generator expresioini i sa tam nawet 2

        # empty_seats = 0
        #
        # for row in self.seats:
        #     if row is not None:
        #         for seat in row.values():
        #             if seat is None:
        #                 empty_seats += 1
        #
        # return empty_seats

    def _get_passengers(self): # deklaracja
        rows, letters = self.airplane.seating_plan()  # deklarujemy 2 zmienne, za pomoca tuple unpackin przypisujemy wartosci
        # seating_plan() zwraca range w klasie Plane

        for row in rows:
            for letter in letters:
                if self.seats[row][letter] is not None:
                    yield f'{row}{letter}', self.seats[row][letter]
                    # yield zwraca wartość, generuje jeden po drugim,
                    # zwraca pasażerów a print_cards je tylko drukuje

    def print_cards(self, card_printer):  # dostaje obiekt funkcji card_printer
        for seat, passenger in self._get_passengers():  # za pomocą pętli for deklarujemy zmienne i sa inicjalizowanie
            card_printer(passenger, seat, self.flight_number, self.get_plane())  # wywołuje deklaracji funkcji
        # self._get_passengers(): <--metoda obiektu

        # for idx, row in enumerate(self.seats):
        #     if row is not None:
        #         for letter, passenger in row.items():
        #             if passenger is not None:
        #                 card_printer(passenger, f'{idx}{letter}', self.flight_number, self.get_plane())


class Airplane: # deklaracja klasy
    def get_num_seats(self): # deklaracja metody
        rows, seats = self.seating_plan() #  tuple  unpacking  metody seting_plan
        return len(rows) * len(seats) # wraca dlugość wynik mnożenia


class Boeing737Max(Airplane): # deklaraca kalsy, która dziedziczy po Airplane
    @staticmethod
    def get_name(): # deklaracja metody
        return 'Boeing 737Max' # zwraca str

    @staticmethod
    def seating_plan(): # deklaracja metody seating plan, która jest static method,
        return range(1, 26), 'ABCDEG' # zwraca tuple 2 elementową, pierwszy jest range a drugi string


class AirbusA380(Airplane):
    @staticmethod
    def get_name():
        return 'Airbus A370'

    @staticmethod
    def seating_plan():
        return range(1, 51), 'ABCDEGHJK'


def printer(passenger, seat, flight_number, airplane):
    text = f'| Passenger: {passenger}, seat: {seat}, {flight_number}/{airplane} |' # deklaracja zmiennych
    border = f'+{"-" * (len(text) - 2)}+'
    line = f'|{" " * (len(text) - 2)}|'

    frame = '\n'.join([border, line, text, line, border]) # do zmiennej frame, przypisujemy wynik wywołania metody na obiekcie klasy string
    print(frame)


boeing = Boeing737Max() # zmienna boeing do której przypisujemy klase
airbus = AirbusA380() # zmenna airbus do której przypisujemy klase Airbus
f = Flight('BA128', boeing) # zmienna f do której przypisujemy wynik klasy flight, w której  przekazujemy parametry str i wartość zmiennej

# print(f.get_airline())
# print(f.get_number())
# print(f.get_plane())
f.allocate_passenger('25G', 'Pawel K')
f.allocate_passenger('1A', 'Lech K')
f.allocate_passenger('1B', 'Jarosław K')
f.relocate_passenger('1A', '12C')

print(boeing.get_num_seats()) # wywolanie metody print do której  wywołujemy metode get)num_seats w kontekscie klasy boeing
print(f.count_empty_seats())
f.print_cards(printer)
# pp(f.seats)

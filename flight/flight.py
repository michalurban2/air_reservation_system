class Flight:
    def __init__(self, flight_number, airplane):
        self.airplane = airplane
        self.flight_number = flight_number

        rows, letters = self.airplane.seating_plan()
        self.seats = [None] + [{letter: None for letter in letters} for _ in rows]

    def get_airline(self):
        return self.flight_number[:2]

    def get_number(self):
        return self.flight_number[2:]

    def get_plane(self):
        return self.airplane.get_name()

    def _parse_seats(self, seat):
        letter = seat[-1]
        rows, letters = self.airplane.seating_plan()

        if letter not in letters:
            raise ValueError(f'Invalid seat letter: {letter}')

        row_text = seat[:-1]

        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f'Invalid row number: {row_text}')

        if row not in rows:
            raise ValueError(f'Row: {row} not in rows range')

        return row, letter

    def allocate_passenger(self, seat, passenger):
        row, letter = self._parse_seats(seat)

        if self.seats[row][letter] is not None:
            raise ValueError(f'Seat {seat} is already taken')

        self.seats[row][letter] = passenger

    def relocate_passenger(self, old_seat, new_seat):
        old_row, old_letter = self._parse_seats(old_seat)

        if self.seats[old_row][old_letter] is None:
            raise ValueError(f'Old seat is empty: {old_seat}')

        new_row, new_letter = self._parse_seats(new_seat)

        if self.seats[new_row][new_letter] is not None:
            raise ValueError(f'New seat {new_seat} is already taken')

        self.seats[new_row][new_letter] = self.seats[old_row][old_letter]
        self.seats[old_row][old_letter] = None

    def count_empty_seats(self):
        return sum(sum(1 for passenger in row.values() if passenger is None)
                   for row in self.seats
                   if row is not None)

    def _get_passengers(self):
        rows, letters = self.airplane.seating_plan()

        for row in rows:
            for letter in letters:
                if self.seats[row][letter] is not None:
                    yield f'{row}{letter}', self.seats[row][letter]

    def print_cards(self, card_printer):
        for seat, passenger in self._get_passengers():
            card_printer(passenger, seat, self.flight_number, self.get_plane())

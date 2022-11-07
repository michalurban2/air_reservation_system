from flight import Flight
from planes import Boeing737Max, AirbusA380


def printer(passenger, seat, flight_number, airplane):
    text = f'| Passenger: {passenger}, seat: {seat}, {flight_number}/{airplane} |'
    border = f'+{"-" * (len(text) - 2)}+'
    line = f'|{" " * (len(text) - 2)}|'

    frame = '\n'.join([border, line, text, line, border])
    print(frame)


def make_flight():
    boeing = Boeing737Max()
    airbus = AirbusA380()
    f = Flight('BA128', boeing)

    # print(f.get_airline())
    # print(f.get_number())
    # print(f.get_plane())
    f.allocate_passenger('25G', 'Pawel K')
    f.allocate_passenger('1A', 'Lech K')
    f.allocate_passenger('1B', 'Jarosław K')
    f.relocate_passenger('1A', '12C')

    print(boeing.get_num_seats())
    print(f.count_empty_seats())
    f.print_cards(printer)
    # pp(f.seats)
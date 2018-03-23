import json
from math import sqrt
import sys


def load_data(filepath):
    with open(filepath, 'r') as file:
        try:
            bars_data = json.loads(file.read())
        except:
            print('Файл НЕ json')
            sys.exit()
    return bars_data


def get_name_seats_coordinates(bars_data):
    name_seats = []
    name_coordinates = []
    for bar in bars_data['features']:
        name_seats.append(
            (bar['properties']['Attributes']['Name'],
             (bar['properties']['Attributes']['SeatsCount']),
             (bar['geometry']['coordinates'])))
    return name_seats


def get_biggest_bar(name_seats):
    biggest_bar = max(name_seats, key=lambda x: x[1])
    return biggest_bar


def get_smallest_bar(name_seats):
    smallest_bar = min(name_seats, key=lambda x: x[1])
    return smallest_bar


def get_closest_bar(name_seat_coordinates, longitude, latitude):
    closest_bar = (
    min(name_seat_coordinates, key=lambda x: sqrt((x[2][0] - longitude) ** 2 + (x[2][1] - latitude) ** 2)))
    return closest_bar[0]


def input_float():
    while True:
        try:
            latitude =  float(input('Введите широту в формате (55.5):\n'))
            longitude = float(input('Введите долготу в формате (55.5):\n'))
            break
        except ValueError:
            print('Неверный формат данных. ')
    return latitude, longitude


if __name__ == '__main__':
    # try:
    #     filepath = sys.argv[1]
    #     os.path.exists(filepath)
    # except:
    #     print('Файл не найден или введен некорректный аргумент')
    #     sys.exit()
    filepath = sys.argv[1]
    bars_data = load_data(filepath)
    name_seat_coordinate = get_name_seats_coordinates(bars_data)
    print('Самый большой бар: ', get_biggest_bar(name_seat_coordinate)[0])
    print('Самый маленький бар: ', get_smallest_bar(name_seat_coordinate)[0])
    #lat = float(input('Введите широту:\n'))
    #lon = float(input('Введите долготу:\n'))
    lat, lon = input_float()
    print(lat, lon)
    print("Самый близкий бар: ", get_closest_bar(name_seat_coordinate, lat, lon))

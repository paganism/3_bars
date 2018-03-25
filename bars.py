import json
from math import sqrt
import sys
import os


def load_data(myjson):
    try:
        with open(filepath, 'r') as file:
            json_object = json.loads(file.read())
    except ValueError:
        return False
    return json_object


def get_biggest_bar_name(bars_data):
    return \
        max(bars_data['features'], key=lambda x: x['properties']['Attributes']['SeatsCount'])[
            'properties'][
            'Attributes'][
            'Name']


def get_smallest_bar_name(bars_data):
    return \
        min(bars_data['features'], key=lambda x: x['properties']['Attributes']['SeatsCount'])[
            'properties'][
            'Attributes'][
            'Name']


def get_closest_bar_name(bars_data, longitude, latitude):
    return min(bars_data['features'], key=lambda x: sqrt(
        (x['geometry']['coordinates'][0] - longitude) ** 2 +
        (x['geometry']['coordinates'][1] - latitude) ** 2))[
        'properties']['Attributes']['Name']


def get_user_coordinates():
    try:
        latitude = float(input('Введите широту в формате (55.5):\n'))
        longitude = float(input('Введите долготу в формате (55.5):\n'))
    except ValueError:
        print('Неверный формат данных. Данные должны быть в формате (55.5)')
        return None, None
    return latitude, longitude


if __name__ == '__main__':
    filepath = sys.argv[1]
    if not os.path.exists(filepath):
        print('Файл .json по указанному пути не суествует')
        sys.exit()
    bars_data = load_data(filepath)
    if bars_data == False:
        print('Файл не в формате json')
        sys.exit()
    print('Самый большой бар: ', get_biggest_bar_name(bars_data))
    print('Самый маленький бар: ', get_smallest_bar_name(bars_data))
    lat, lon = get_user_coordinates()
    if lat is None or lon is None:
        sys.exit()
    print("Самый близкий бар: ", get_closest_bar_name(bars_data, lat, lon))

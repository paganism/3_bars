import json
from math import sqrt
import sys
import os


def load_data(myjson):
    try:
        with open(filepath, 'r') as file:
            decoded_json = json.loads(file.read())
        return decoded_json
    except ValueError:
        return False


def get_bars_features(bars_data):
    return bars_data['features']


def get_biggest_bar(bars_features):
    return max(bars_features, key=lambda x: x['properties']['Attributes']['SeatsCount'])


def get_smallest_bar(bars_data):
    return min(bars_features, key=lambda x: x['properties']['Attributes']['SeatsCount'])


def get_closest_bar(bars_data, longitude, latitude):
    return min(bars_data['features'], key=lambda x: sqrt(
        (x['geometry']['coordinates'][0] - longitude) ** 2 +
        (x['geometry']['coordinates'][1] - latitude) ** 2))


def get_user_coordinates():
    try:
        latitude = float(input('Введите широту в формате (55.5):\n'))
        longitude = float(input('Введите долготу в формате (55.5):\n'))
    except ValueError:
        return None, None
    return latitude, longitude


def check_filepath(filepath):
    try:
        if not (os.path.exists(filepath)):
            return None
        return filepath
    except IndexError:
        return None

def get_bar_name(bar):
    return bar['properties']['Attributes']['Name']


if __name__ == '__main__':
    filepath = check_filepath(sys.argv[1])
    if not filepath:
        sys.exit('Файл не суествует')
    bars_data = load_data(filepath)
    if not bars_data:
        sys.exit('Файл не в формате json')
    bars_features = get_bars_features(bars_data)
    biggest_bar = get_biggest_bar(bars_features)
    print('Самый большой бар: ', get_bar_name(biggest_bar))
    smallest_bar = get_smallest_bar(bars_features)
    print('Самый маленький бар: ', get_bar_name(smallest_bar))
    lat, lon = get_user_coordinates()
    if not all([lat, lon]):
        sys.exit('Неверный формат данных. Данные должны быть в формате (55.5)')
    closest_bar = get_closest_bar(bars_data, lat, lon)
    print('Самый близкий бар: ', get_bar_name(closest_bar))
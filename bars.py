import json
from math import sqrt
import sys


def load_data(filepath):
    with open(filepath, 'r') as file:
        bars_data = json.loads(file.read())
    return bars_data


# print(load_data())

def get_name_seats_coordinates(bars_data):
    name_seats = []
    name_coordinates = []
    for item in bars_data["features"]:
        name_seats.append(
            (item["properties"]["Attributes"]["Name"],
             (item["properties"]["Attributes"]["SeatsCount"]),
             (item["geometry"]["coordinates"])))
        # name_coordinates.append(
        #    (item["properties"]["Attributes"]["Name"], item["geometry"]["coordinates"]))
    return name_seats


# print(get_name_seats_coordinates(load_data()))


def get_biggest_bar(name_seats):
    return max(name_seats, key=lambda x: x[1])


# print(get_biggest_bar(get_name_seats_coordinates(load_data())))


def get_smallest_bar(name_seats):
    return min(name_seats, key=lambda x: x[1])


# print(get_smallest_bar(get_name_seats_coordinates(load_data())))

def get_closest_bar(name_seats, longitude, latitude):
    bars_distance = []
    for bar in name_seat_coordinate:
        # print(bar[2][0], bar[2][1])
        d = sqrt((bar[2][0] - longitude) ** 2 + (bar[2][1] - latitude) ** 2)
        # print(bar[0], d)
        bars_distance.append(
            (bar[0], d)
        )
    closest_bar = (min(bars_distance, key=lambda x: x[1]))
    return closest_bar[0]


if __name__ == '__main__':
    filepath = sys.argv[1]
    bars_data = load_data(filepath)
    name_seat_coordinate = get_name_seats_coordinates(bars_data)
    # print(name_seat_coordinate)
    print("Biggest bar is: ", get_biggest_bar(name_seat_coordinate)[0])
    print("Smallest bar is: ", get_smallest_bar(name_seat_coordinate)[0])
    # print("Biggest bar is: ", get_biggest_bar(name_seat_coordinate))
    # x = 55.5878787
    # y = 43.77497
    lat = float(input('Enter latitude:\n'))
    lon = float(input('Enter longitude:\n'))
    print("Closest bar is: ", get_closest_bar(name_seat_coordinate, lat, lon))
    # √(x2−x1)2+(y2−y1)2

# coding: utf-8
import csv


class BaseCar:
    def __init__(self,  brand, carrying, photo_file_name):
        self.brand = brand
        self.carrying = carrying
        self.photo_file_name = photo_file_name

    def get_photo_file_ext(self):
        return self.photo_file_name.split('.')[-1]


class Car(BaseCar):
    def __init__(self, brand, carrying,  photo_file_name, passenger_seats_count):
        super().__init__(brand, carrying, photo_file_name)
        self.passenger_seats_count = passenger_seats_count


class Truck(BaseCar):
    def __init__(self, brand, carrying, photo_file_name, body_length=None, body_width=None, body_height=None):
        super().__init__(brand, carrying, photo_file_name)
        self.body_length = body_length
        self.body_width = body_width
        self.body_height = body_height

    def get_body_volume(self):
        return self.body_height * self.body_length * self.body_width


class SpecMachine(BaseCar):
    def __init__(self, brand, carrying, photo_file_name, extra):
        super().__init__(brand, carrying, photo_file_name)
        self.extra = extra


def get_car_list(url):
    with open(url, 'r', encoding='utf-8') as csv_f:
        reader = csv.reader(csv_f, delimiter=';')
        next(reader)
        car_list = []
        for row in reader:
            try:
                if row[0] != '':
                    if row[4] != '':
                        row[4] = row[4].split('x')
                    car_list.append(row)
            except IndexError:
                continue
        return car_list


def car_parse(cars):
    for row in cars:
        if row[0] == 'car':
            car = Car(row[1], int(row[2]), row[3], float(row[5]))
        elif row[0] == 'truck':
            try:
                truck = Truck(row[1], row[2], row[3], float(row[4][0]), float(row[4][1]), float(row[4][2]))
            except IndexError:
                truck = Truck(row[1], row[2], row[3])
        elif row[0] == 'spec_machine':
            spec_machine = SpecMachine(row[1], row[3], float(row[5]), row[6])
        else:
            print('Something goes wrong')


cars = get_car_list(r'coursera_week3_cars.csv')

print(cars)
# car_parse(cars)

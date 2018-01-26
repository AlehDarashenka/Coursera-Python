from os import path
import csv

DOCS_PATH = path.join(
    path.join(
        path.join(path.dirname(path.abspath(__file__)), '..'),
        '..'),
    'Docs')

class CarBase:
    #csv row indexes
    ix_car_type = 0
    ix_brand = 1
    ix_passenger_seats_count = 2
    ix_photo_file_name = 3
    ix_body_whl = 4
    ix_carrying = 5
    ix_extra = 6

    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        _, ext = path.splitext(self.photo_file_name)
        return ext

class Car(CarBase):
    car_type = 'car'
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)

    @classmethod
    def from_tuple(cls, row):
        return cls(
            row[cls.ix_brand],
            row[cls.ix_photo_file_name],
            row[cls.ix_carrying],
            row[cls.ix_passenger_seats_count]
        )


class Truck(CarBase):
    car_type = 'truck'

    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self._body_whl = body_whl

    @staticmethod
    def _body_component_splitter(text, delimiter='x'):
        if text:
            return list(map(float, text.split(delimiter)))
        else:
            return [0, 0, 0]  # W x H x L

    @property
    def body_width(self):
        return Truck._body_component_splitter(self._body_whl)[0]

    @property
    def body_height(self):
        return Truck._body_component_splitter(self._body_whl)[1]
    @property
    def body_length(self):
        return Truck._body_component_splitter(self._body_whl)[2]

    @classmethod
    def from_tuple(cls, row):
        return cls(
            row[cls.ix_brand],
            row[cls.ix_photo_file_name],
            row[cls.ix_carrying],
            row[cls.ix_body_whl]
        )

    def get_body_volume(self):
        return self.body_height*self.body_width*self.body_length


class SpecMachine(CarBase):
    car_type = 'spec_machine'
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra

    @classmethod
    def from_tuple(cls, row):
        return cls(
            row[cls.ix_brand],
            row[cls.ix_photo_file_name],
            row[cls.ix_carrying],
            row[cls.ix_extra]
        )



def get_car_list(csv_filename):
    car_list = []
    car_strategy = {car_class.car_type: car_class for car_class in (Car, Truck, SpecMachine)}

    with open(path.join(DOCS_PATH, csv_filename)) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # skip header
        for row in reader:
            try:
                car_list.append(car_strategy[row[CarBase.ix_car_type]].from_tuple(row))
            except (IndexError, ValueError, KeyError):
                continue
            print(row)

    return car_list


if __name__ == '__main__':
    car_list = get_car_list('coursera_week3_cars.csv')
    print(car_list[1].get_body_volume())
    print(car_list[2].get_body_volume())
    for i in car_list:
        print(i.get_photo_file_ext())
from os import path
import csv

DOCS_PATH = path.join(
    path.join(
        path.join(path.dirname(path.abspath(__file__)), '..'),
        '..'),
    'Docs')

class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        return path.splitext(self.photo_file_name)[1]

class Car(CarBase):
    car_type = 'car'
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)


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

    def get_body_volume(self):
        return self.body_height*self.body_width*self.body_length


class SpecMachine(CarBase):
    car_type = 'spec_machine'
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra



def get_car_list(csv_filename):
    car_list = []
    with open(path.join(DOCS_PATH,csv_filename)) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # skip header
        for row in reader:
            try:
                if row[0] == Car.car_type:
                    car_list.append(Car(row[1], row[3], row[5],row[2]))
                elif row[0] == Truck.car_type:
                    car_list.append(Truck(row[1], row[3],row[5], row[4]))
                elif row[0] == SpecMachine.car_type:
                    car_list.append(SpecMachine(row[1], row[3], row[5],row[6]))
            except IndexError:
                pass
            except ValueError:
                pass
            print(row)

        return car_list


if __name__ == '__main__':
    car_list = get_car_list('coursera_week3_cars.csv')
    print(car_list[1].get_body_volume())
    print(car_list[2].get_body_volume())
    for i in car_list:
        print(i.get_photo_file_ext())
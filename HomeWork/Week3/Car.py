import os
class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)

class Car(CarBase):
    car_type = 'car'
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = passenger_seats_count


class Truck(CarBase):
    car_type = 'truck'

    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self._body_whl = body_whl

    @staticmethod
    def _body_component_splitter(text, delimiter='x'):
        if text:
            return map(int, text.split(delimiter))
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
    return car_list


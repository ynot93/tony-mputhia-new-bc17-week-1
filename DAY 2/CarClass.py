class Car(object):
    def __init__(self, name='General', model='GM', vehicle_type=None):
        self.name = name
        self.model = model
        self.vehicle_type = vehicle_type
        self.speed = 0

        if self.name in ['Porshe', 'Koenigsegg']:
            self.num_of_doors = 2
        elif self.vehicle_type == 'trailer':
            self.num_of_wheels = 8
        else:
            self.num_of_wheels = 4

    def is_saloon(self):
        if self.num_of_wheels == 4:
            self.vehicle_type = 'saloon'
        else:
            self.vehicle_type = 'trailer'

    def drive(self, moving_speed):
        if moving_speed == 3:
            self.speed = 1000
        elif moving_speed == 7:
            self.speed = 77

        return self
    

class Vehicle (object):
    wheels = 0

    def __init__(self, make, year_built, wheels, date_sold):
        self.make = str(make)
        self.year_built = year_built
        self.wheels = wheels
        self.date_sold = date_sold

    def selling_price(self):
        if self.date_sold is None:
            return 100000*self.wheels
        else:
            return 'Vehicle has been sold'


class Car(Vehicle):
    wheels = 4


class Motorcycle(Vehicle):
    wheels = 2


class Trailer(Vehicle):
    wheels = 10

Kawasaki = Motorcycle(spider, 2016, 2, None)
print(Kawasaki.selling_price())





from math import sqrt


class City:
    id = 0
    name = ""
    population = 0
    latitude = 0.0
    longitude = 0.0

    def __init__(self, data):
        self.id = int(data[0])
        self.name = data[1]
        self.population = int(data[2])
        self.latitude = float(data[3])
        self.longitude = float(data[4])

    def __str__(self) -> str:
        return self.name

    def distance(self, other):
        return sqrt((self.latitude - other.latitude) ** 2 + (self.longitude - other.longitude) ** 2)

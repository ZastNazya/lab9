from operator import le
from re import L


class figures:
    def init(self, length : int, width :  int , height: int ):
        self.length = length
        self.width = width
        self.height = height

class circle(figures):
    def init(self,length : int, width :  int ,  height: int , radius : int):
        super().init(length, width, height )
        self.radius = radius


class triangle(figures):
    def init(self,length : int, width :  int ,  height: int , square: int):
        super().init(length, width, height)
        self.square = square


class cylinder(figures):
    def init(self,length : int, width :  int ,  height: int , volume: int):
        super().init(length, width, height)
        self.volume = volume


class cone(figures):
    def init(self,length : int, width :  int ,  height: int , creating : int ):
        super().init(length, width, height)
        self.creating = creating


class sphere(figures):
    def init(self,length : int, width :  int ,  height: int , diameter: int):
        super().init(length, width, height)
        self.diameter = diameter
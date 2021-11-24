import sys
import os
from math import pi


class Circle:
    def __init__(self, radius, fill='red', stroke='black'):
        self._radius = radius #private/protected
        self._fill = fill
        self._stroke = stroke

    def calculate_area(self):
        '''Calculate area'''
        return pi * self._radius ** 2

    @property # decorator # Public access for radius - read only
    def rad(self):
        return self._radius # Reflecting private radius publicly

    def __len__(self):
        return int(2 * pi *self._radius)

    def __call__(self):
        return "I am a circle!"

    def __str__(self):
	    return f"Instance of {self.__class__.__qualname__}"
    def __repr__(self):
        return f"Circle{self._radius} , fill={self._fill}, stroke={self._stroke}"

def main():
    circle = Circle(5.0, fill='orange', stroke='red')
    print(f"area = {circle.calculate_area()}")
    #print(circle._radius)
    #circle.radius = 3
    print(circle._radius)# Violating private rule, so use @property
    #print(f"ra = {circle.rad()}")
    print(f"circumference is {len(circle)}")
    print(circle())
    print(repr(circle))

    # stringify the instance
    print(str(circle))
    return 0


if __name__ == '__main__':
    sys.exit(main())

import sys
import os
from math import pi
import yaml

class Circle:
    def __init__(self, radius, fill='red', stroke='black', at =(0,0)):
        self._radius = radius #private/protected
        self._fill = fill
        self._stroke = stroke
        self._at= at

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
        string = yaml.dump({
            'circle': {
                'radius': self._radius,
                'fill': self._fill,
                'stroke': self._stroke,
                'at': self._at
            }
        })
        return string
	    #return f"Instance of {self.__class__.__qualname__}"

    @classmethod
    def from_yaml(cls,string):
        """Create a circle from a yaml STRING"""
        circle_dict = yaml.load(string, Loader=yaml.Loader)['circle']
        print(circle_dict)
        obj = cls(circle_dict['radius'], fill=circle_dict['fill'], stroke =circle_dict['stroke'], at =circle_dict['at'])
        return obj


    def __repr__(self):
        return f"Circle{self._radius} , fill={self._fill}, stroke={self._stroke}"

class Canvas:
    def __init__(self, width, height, bg='blue'):
        self._width = width
        self._height = height
        self._bg = bg


class Text:
    def __init__(self, text, font = 15, color='black'):
        self._text = text
        self._font = font
        self._color = color

class Quadrilateral:
    shape = 'quadrilateral'

    def __init__(self, width, height, fill='green', stroke='yellow'):
        self._width = width
        self._height = height
        self._fill = fill
        self._stroke = stroke

    def calculate_qarea(self):
        '''Calculate area'''
        return self._width * self._height


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
    print(circle)

    yaml_circle = """\
circle:
  at: !!python/tuple
  - 0
  - 0
  fill: orange
  radius: 5.0
  stroke: red"""
    my_circle = Circle.from_yaml(yaml_circle)

    quad = Quadrilateral(5.0, 7.0, fill='orange', stroke='red')

    my_dict ={
        'key':{
            'inside_dict': [5,6,7,8]
        }
    }

    my_yaml = yaml.dump(my_dict) # yaml format from dictionary
    print(my_yaml)
    print(my_circle)
    return 0





































































if __name__ == '__main__':
    sys.exit(main())

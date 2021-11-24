import sys
import os
import turtle
from math import pi
import yaml

turtle.tracer(False)
class Circle:
    def __init__(self, radius, fill='red', stroke='black', at=(0, 0)):
        self._radius = radius #private/protected
        self._fill = fill
        self._stroke = stroke
        self._at = at

    def calculate_area(self):
        """Calculate area"""
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

    def draw(self, pen):
        """Draw a circle"""
        if pen.isdown():
            pen.up()
        pen.goto(*self._at)
        pen.down()
        pen.begin_fill()
        pen.pencolor(self._stroke)
        pen.fillcolor(self._fill)
        pen.circle(self._radius) ##*args, **kwargs
        pen.end_fill()
        pen.up()

    @classmethod
    def from_yaml(cls, string):
        """Create a circle from a yaml STRING"""
        circle_dict = yaml.load(string, Loader=yaml.Loader)['circle']
        print(circle_dict)
        obj = cls(circle_dict['radius'], fill=circle_dict['fill'], stroke =circle_dict['stroke'], at =circle_dict['at'])
        return obj


    def __repr__(self):
        return f"Circle{self._radius} , fill={self._fill}, stroke={self._stroke}"

# class Canvas:
#     def __init__(self, width, height, bg='blue'):
#         self._width = width
#         self._height = height
#         self._bg = bg

class Canvas(turtle.TurtleScreen):
    def __init__(self, width, height, bg='#ffffff'):
        self._cv = turtle.getcanvas()
        super().__init__(self._cv)
        self.screensize(width, height, bg=bg)
        self._width = width
        self._height = height
        self._pen = turtle.Turtle()
        self._pen.hideturtle()
        # self._pen.speed(0)
        # self.bgpic('funny.gif')
        # self.onclick(self._report)

    def draw_axes(self):
        # self._pen.speed(0)
        self._pen.up()
        self._pen.goto(0, self._height / 2)
        self._pen.down()
        self._pen.goto(0, -self._height / 2)
        self._pen.up()
        self._pen.goto(-self._width / 2, 0)
        self._pen.down()
        self._pen.goto(self._width / 2, 0)
        self._pen.up()
        self._pen.goto(-self._width / 2, -self._height / 2)

    def draw_grid(self, colour='#00ff99', hstep=50, vstep=50):
        # self._pen.speed(0)
        original_pen_colour = self._pen.pencolor()
        self._pen.color(colour)
        # vertical grids
        self._pen.up()
        for hpos in range(-500, 500 + hstep, hstep):
            self._pen.goto(hpos, 350)
            self._pen.down()
            self._pen.goto(hpos, -350)
            self._pen.up()
        # horizontal grids
        for vpos in range(-350, 350 + vstep, vstep):
            self._pen.goto(-500, vpos)
            self._pen.down()
            self._pen.goto(500, vpos)
            self._pen.up()
        # reset
        self._pen.pencolor(original_pen_colour)

    def write(self, text, *args, **kwargs):
        text.write(self._pen, *args, **kwargs)

    def draw(self, shape):
        """Draw the given shape"""
        shape.draw(self._pen)

class Text:
    def __init__(self, text, at=(0, 0)):
        self._text = text
        self._at = at

    def write(self, pen, *args, **kwargs):
        pen.up()
        pen.goto(self._at)
        pen.down()
        pen.write(self._text, *args, **kwargs)
        pen.up()





class Quadrilateral:
    shape = 'quadrilateral'

    def __init__(self, width, height, fill='green', stroke='yellow', at=(0, 0)):
        self._width = width
        self._height = height
        self._fill = fill
        self._stroke = stroke
        self._at = at

    def calculate_qarea(self):
        """Calculate area"""
        return self._width * self._height

    @property
    def left(self):
        return self._at[0] -self._width/2

    @property
    def top(self):
        return self._at[1] + self._height / 2

    @property
    def right(self):
        return self._at[0] + self._width / 2

    @property
    def bottom(self):
        return self._at[1] - self._height / 2
    @property
    def vertices(self):
        """ Starting from the top left counter clockwise"""
        return [
            (self.left, self.top),
            (self.left, self.bottom),
            (self.right, self.bottom),
            (self.right, self.top)
        ]
    def draw(self, pen, *args, **kwargs):
        """Draw a Quadrilateral"""

        pen.up()
        pen.goto(self.left, self.top)
        pen.down()
        pen.goto(self.left, self.bottom)
        pen.goto(self.right, self.bottom)
        pen.goto(self.right, self.top)
        pen.goto(self.left, self.top)
        pen.begin_fill()
        pen.pencolor(self._stroke)
        pen.fillcolor(self._fill)
        pen.end_fill()
        pen.up()



def main():
    circle = Circle(15.0, fill='orange', stroke='red')
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
    pen = turtle.Turtle()
    text= Text("This was written by a Turtle")
    print(text)
    text.write(pen, font=('Arial', 30, 'bold'))

    circle.draw(pen)

    quad = Quadrilateral(200.0, 60.0, at=(15, -5))
    print(f"vertices = {quad.vertices}")
    quad.draw(pen)


    # canvas = Canvas(1000,700)#'magenta'
    # canvas.draw_axes()
    # canvas.draw_grid()
    # canvas.write(text)
    #
    # canvas.draw(circle)

    canvas = Canvas(1000, 700)  # 'magenta'
    gquad = Quadrilateral(
        200, 300, fill ='#009a44', stroke='white', at=(-200, 0)
            )
    wquad = Quadrilateral(
        200, 300, fill='white', stroke='#dddddd', at=(0, 0)
    )
    oquad = Quadrilateral(
        200, 300, fill='#ff8200', stroke='white', at=(200, 0)
    )
    text = Text('IRELAND', at=(0, -250))
    canvas.draw(gquad)
    canvas.draw(wquad)
    canvas.draw(oquad)
    canvas.write(text, align='center', font= ('Arial', 60, 'bold'))
    turtle.done()

    my_dict = {
        'key': {
            'inside_dict': [5, 6, 7, 8]
        }
    }

    my_yaml = yaml.dump(my_dict) # yaml format from dictionary
    print(my_yaml)
    print(my_circle)
    return 0



if __name__ == '__main__':
    sys.exit(main())

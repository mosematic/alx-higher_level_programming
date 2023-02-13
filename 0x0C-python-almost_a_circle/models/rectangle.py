#!/usr/bin/python3
'''
class Rectangle module
'''
from models.base import Base


class Rectangle(Base):
    ''' Class Rectangle which inherits from Base class'''
    def __init__(self, width, height, x=0, y=0, id=None):
        ''' Rectangle class initialization '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        ''' width value getter '''
        return self.__width

    @width.setter
    def width(self, value):
        ''' width value setter '''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        ''' height value getter '''
        return self.__height

    @height.setter
    def height(self, value):
        ''' height value setter '''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        ''' x value getter '''
        return self.__x

    @x.setter
    def x(self, value):
        ''' x value setter '''
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        ''' y value getter '''
        return self.__y

    @y.setter
    def y(self, value):
        ''' y value setter '''
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        ''' calculates the area of the rectangle '''
        return (self.height * self.width)

    def display(self):
        ''' prints out the Rectangle instance with the char # '''
        for row in range(self.y):
            print()
        for row in range(self.__height):
            print('{}{}'.format(' ' * self.x, '#' * self.width))

    def __str__(self):
        ''' prints rectangle info in a different format '''
        return ("[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"
                .format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        ''' updates the class Rectangle '''
        if args:
            keys = ['id', 'width', 'height', 'x', 'y']
            for key, value in zip(keys, args):
                setattr(self, key, value)
            return
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        ''' returns the dictionary representation of a Rectangle class '''
        return {'id': self.id, 'width': self.width,
                'height': self.height, 'x': self.x, 'y': self.y}

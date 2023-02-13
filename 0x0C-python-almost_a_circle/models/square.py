

#!/usr/bin/python3
'''
class Square module
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    ''' Square class which inherits from Rectangle class '''
    def __init__(self, size, x=0, y=0, id=None):
        ''' initialize Square class '''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        ''' prints to stdout the rectangle info in a different format '''
        return ("[Square] ({:d}) {:d}/{:d} - {:d}"
                .format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        ''' size value getter '''
        return self.width

    @size.setter
    def size(self, value):
        ''' size value setter '''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        ''' updates the class Square '''
        if args:
            keys = ['id', 'size', 'x', 'y']
            for key, value in zip(keys, args):
                setattr(self, key, value)
            return
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        ''' returns the dictionary representation of a Square '''
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}

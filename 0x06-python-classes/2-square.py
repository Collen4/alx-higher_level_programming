#!/usr/bin/python3
""" class Square """


class Square:
    """ defines a square"""

    def __init__(self, size=0):
        """ Initialize
        Args:
            size (init): size of square
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

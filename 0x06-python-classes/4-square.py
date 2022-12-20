#!/usr/bin/python3
""" Class square that defines a square"""


class Square:
    """ Define a square"""
    def __init__(self, size=0):
        """ initialize square"""
	self.size = size


    def size(self):
        """Init private size."""
	return self.size


    def size(self, value):
        if type(value) is not int:
	    raise TypeError('size must be an integer')
	elif value < 0:
	    raise ValueError('size must be >= 0')
	else:
	    self.__size = value


    def area(self):
        """returns the current square area."""
	return self.__size**2

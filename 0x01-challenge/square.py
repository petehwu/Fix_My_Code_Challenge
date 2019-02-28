#!/usr/bin/python3
""" square class """


class square():
    """square class definition"""

    def __init__(self, *args, **kwargs):
        """init method"""
        h = kwargs.get('height')
        w = kwargs.get('width')
        if (h is None or w is None or h != w):
            self.height = 0
            self.width = 0
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """returns perimeter"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """format object for printing"""
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())

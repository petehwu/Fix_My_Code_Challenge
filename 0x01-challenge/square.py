#!/usr/bin/python3


class square():

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        if (self.width >= self.height):
            return self.height * self.height
        else:
            return self.width * self.width

    def PermiterOfMySquare(self):
        if (self.width >= self.height):
            return (self.height * 4)
        else:
            return (self.width * 4)

    def __str__(self):
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())

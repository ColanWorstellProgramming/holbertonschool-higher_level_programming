#!/usr/bin/python3
"""square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square is rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get size"""
        return self.width

    @size.setter
    def size(self, value):
        """set size"""
        self.width = value
        self.height = value

    def __str__(self):
        """str"""
        tangles = "[Square] " + "({}) ".format(self.id)
        tangles = tangles + "{}/{} - ".format(self.x, self.y)
        tangles = tangles + "{}".format(self.width)
        return (tangles)

    def update(self, *args, **kwargs):
        """Quick Update"""
        if (args is None or args == ()) and kwargs is not None:
            args = [kwargs.get("id"), kwargs.get("size"), kwargs.get("x"),
                    kwargs.get("y")]
        try:
            self.id = args[0] or self.id
            self.size = args[1] or self.size
            self.x = args[2] or self.x
            self.y = args[3] or self.y
        except IndexError:
            return

    def to_dictionary(self):
        """moby"""
        moby = {"id": self.id,
                "size": self.width, "x": self.x, "y": self.y}
        return moby

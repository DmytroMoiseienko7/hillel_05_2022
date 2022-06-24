from abc import ABC, abstractclassmethod
from random import choice


class Shape(ABC):
    @abstractclassmethod
    def draw(self):
        pass


class Rectangle(Shape):
    def draw():
        print(" ---- \n |  | \n ----")


class Circle(Shape):
    def draw():
        print("  -- \n -  - \n  --")


def get_shape() -> Shape:
    """
    This function should return any instance of a Shape class
    In our example it is Rectangle or Circle
    """
    options = [Circle, Rectangle]
    return choice(options)


def main():
    """
    If Rectangle is used I'd like to see:

    ----
    |  |
    ----

    If Circle is used:
      --
     -  -
      --
    """

    shape: Shape = get_shape()
    shape.draw()


if __name__ == "__main__":
    main()

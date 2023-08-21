from abc import ABC, abstractmethod
import math


class Figure(ABC):

    def __init__(self, side_1, height, radius):
        self.side_1 = side_1
        self.radius = radius
        self.height = height

    @abstractmethod
    def square(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Triangle(Figure):

    def __init__(self, side_1, height, side_2, side_3):
        super().__init__(side_1, height, 0)
        self.side_2 = side_2
        self.side_3 = side_3

    def square(self):
        return (self.side_1 * self.height) * 0.5

    def perimeter(self):
        return self.side_1 + self.side_2 + self.side_3


triangle = Triangle(5, 4, 6, 7)


class Round(Figure):
    def __init__(self, radius):
        super().__init__(0, 0, radius)

    def square(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


round_figure = Round(6)

list_figures = [triangle, round_figure]
for figure in list_figures:
    print(f"Figure type: {type(figure).__name__}")
    print(f"Figure square is: {figure.square()} cm2")
    print(f"Figure perimeter is: {figure.perimeter()} cm")

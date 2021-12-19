import math


class Shape:
    center = (0, 0)

    def __init__(self, center):
        self.center = center

    def get_distance(figure_1, figure_2):
        return math.sqrt(
                (figure2.center[0] - figure1.center[0])**2 +
                (figure2.center[1] - figure1.center[1])**2
                )


class Circle(Shape):
    def __init__(self, center=(0, 0), radius=1):
        self.radius = radius
        super().__init__(center)

    def get_center(self):
        return self.center

    def get_area(self):
        return math.pi*self.radius**2


class Square(Shape):
    def __init__(self, center=(0, 0), side=1):
        self.side = side
        super().__init__(center)

    def get_center(self):
        return self.center

    def get_area(self):
        return self.side**2

    def get_vertex(self):
        return (self.center[0] - self.side/2, self.center[1] - self.side/2),\
               (self.center[0] - self.side/2, self.center[1] + self.side/2),\
               (self.center[0] + self.side/2, self.center[1] + self.side/2),\
               (self.center[0] + self.side/2, self.center[1] - self.side/2)


class Triangle(Shape):
    def __init__(self, center=(0, 0), side=1):
        self.side = side
        super().__init__(center)

    def get_center(self):
        return self.center

    def get_area(self):
        return (self.side**2 * math.sqrt(3))/4

    def get_vertex(self):
        h = math.sqrt(3)/2 * self.side
        return (self.center[0] - self.side/2, self.center[1] - h * 1/3),\
               (self.center[0], self.center[1] + h * 2/3),\
               (self.center[0] + self.side/2, self.center[1] - h * 1/3)




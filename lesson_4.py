import math


class Shape:
    def __init__(self, center=(0, 0)):
        self.center = center

    def get_distance(self, figure1, figure2):
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
    
    def move(self, x,y):
        center = (x, y)

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
    def move(self, x,y):
        center = (x, y)

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

    def move(self, x,y):
        center = (x, y)


shape = Shape()
c1 = Circle()
s1 = Square((3, 3), 3)
t1 = Triangle((1, 0), 2)


c1.get_center()
c1.get_area()

s1.get_center()
s1.get_area()
s1.get_vertex()
s1.move(10, 13)

t1.get_center()
t1.get_area()
t1.get_vertex()
t1.move(-42, 69)

shape.get_distance(s1, t1)

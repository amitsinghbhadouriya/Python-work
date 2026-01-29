class Shape:
    def draw(self):
        print("Drawing Shape")

class Circle(Shape):
    def draw_circle(self):
        print("Drawing Circle")

class Square(Shape):
    def draw_square(self):
        print("Drawing Square")

c = Circle()
s = Square()

c.draw()
c.draw_circle()

s.draw()
s.draw_square()

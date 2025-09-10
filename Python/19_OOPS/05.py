class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sum(self, p):
        return Point((self.x + p.x), (self.y + p.y))

    def print_point(self):
        return f"x is {self.x} and y is {self.y}"

    def __add__(self,p):
       return Point((self.x + p.x), (self.y + p.y))

p1 = Point(3, 2)
p2 = Point(6, 3)

p = p1+p2 # Returns a new Point which is sum of p1 and p2
print(p.print_point())

""" Other useful magic methods: (You don't need to memorize them all, but be aware they exist!)

__sub__ (-), __mul__ (*), __truediv__ (/), __eq__ (==), __ne__ (!=), __lt__ (<), __gt__ (>), __len__ (len()), __getitem__, __setitem__, __delitem__ (for list/dictionary-like behavior – allowing you to use [] with your objects). """

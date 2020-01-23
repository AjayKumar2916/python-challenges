'''
Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area. 

Hints:

Use def methodName(self) to define a method.
'''

class Rectangle(object):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        a = self.length * self.width
        print('Area of a Rectangle is ',a)

if __name__ == '__main__':
    r = Rectangle(5, 4)
    r.area()

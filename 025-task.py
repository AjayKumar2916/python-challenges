'''
Question:
    Define a class, which have a class parameter and have a same instance parameter.

Hints:
    Define a instance parameter, need add it in __init__ method
    You can init a object with construct parameter or set the value later
'''

class MyClass(object):
    name = 'Jerry'
    def __init__(self, name=None):
        self.name = name

if __name__ == '__main__':
    mc1 = MyClass()
    mc1.name = 'Tom'
    print(mc1.name)

    mc2 = MyClass('Spike')
    print(mc2.name)
'''
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters
'''

class Sample(object):
    def __init__(self):
        self.value = ''

    def getString(self):
        self.value = input('Enter the string: ')

    def printString(self):
        print(self.value.upper())


if __name__ == '__main__':
    s = Sample()
    s.getString()
    s.printString()
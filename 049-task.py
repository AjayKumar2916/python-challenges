'''
Define a class named American which has a static method called printNationality.

Hints:

Use @staticmethod decorator to define class static method.
'''

class American(object):
    @staticmethod
    def printNationality():
        print('America')

if __name__ == '__main__':
    a = American()
    a.printNationality()
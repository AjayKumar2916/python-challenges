'''
Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) and the values are square of keys.

Hints:

Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.
'''

def key_value():
    data = {}
    data[1] = 1 ** 2
    data[2] = 2 ** 2
    data[3] = 3 ** 2
    print(data)
        

key_value()

        
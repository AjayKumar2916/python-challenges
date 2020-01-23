'''
Define a function that can accept two strings as input and print the string with maximum length in console. 
If two strings have the same length, then the function should print al l strings line by line.

Hints:

Use len() function to get the length of a string
'''

def max_len(a, b):
    a_len = len(a)
    b_len = len(b)
    if a_len == b_len:
        print(a)
        print(b)
    elif a_len > b_len:
        print(a)
    elif b_len > a_len:
        print(b)

max_len('Tom', 'Jerry')
'''
Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).

Hints:

Use map() to generate a list.
Use lambda to define anonymous functions.
'''

li = range(1, 21)
s = map(lambda x: x ** 2, li)
print(list(s))
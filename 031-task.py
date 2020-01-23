'''
Define a function that can accept an integer number as input and print the "It is an even number" if the number is even, otherwise print "It is an odd number".

Hints:

Use % operator to check if a number is even or odd.
'''

def even_or_odd(n):
    if n%2==0:
        print("%s is an even number"%(n))
    else:
        print("%s is an odd number"%(n))

even_or_odd(8)
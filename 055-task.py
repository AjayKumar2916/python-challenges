'''
Write a function to compute 5/0 and use try/except to catch the exceptions.

Hints:

Use try/except to catch exceptions.
'''

try:
    a = 5/0
    print(a)
except ZeroDivisionError as e:
    print(str(e))
except Exception as e:
    print(str(e))
finally:
    print('Finally Block')
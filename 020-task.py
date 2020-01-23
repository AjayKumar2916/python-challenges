'''
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

Hints:
Consider use yield
'''


def generator():
    myList = range(100)
    for l in myList:
        if l % 7 == 0:
            yield l

print(generator())
for g in generator():
    print(g)





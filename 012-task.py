'''
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''

even_digits = []
for i in range(1000, 3001):
    if int(str(i)[0]) % 2  == 0 and int(str(i)[1]) % 2  == 0 and int(str(i)[2]) % 2  == 0 and int(str(i)[3]) % 2  == 0:
        even_digits.append(str(i))
print(','.join(even_digits))


'''
Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No". 

Hints:

Use if statement to judge condition.
'''

s = 'yes'
c = ['YES', 'Yes', 'yes']
if s in c:
    print('Yes')
else:
    print('No')

'''
Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''
bal = 0
while True:
    v = input('Enter transaction : ')
    if v != '':
        t = v.split(' ')
        if t[0] == 'D':
            bal += int(t[1])
        elif t[0] == 'W':
            bal -= int(t[1])
    else:
        break

print('Current Balance', bal)

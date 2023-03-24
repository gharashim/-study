#####################################
# .0 if

'''
if condition:
    write the code to run
'''

if 10 > 5:
    print('Correct!')

#####################################
# .1 else & elif

'''
if condition1:
    write the code to run
elif condition2:
    write the code to run
else:
    write the code to run
'''

password_correct = True

if password_correct:
    print('Correct!')
else:
    print('Wrong')

winner = 10

if winner > 10:
    print('Winner is greater than 10')
elif winner < 10:
    print('Winner is less than 10')
else:
    print('Winner is 0')

#####################################
# .2 recap
winner = 50

if winner <= 10:
    print('if')
elif winner <= 25:
    print('elif1')
elif winner <= 0:
    print('elif2')
else:
    print('else')
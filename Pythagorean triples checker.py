# pythagorean triples checker
# functions, if-elif-else statements,

print('Welcome to Pyhtagorean Triples Checker!')

def ptc():
    prompt = '\nEnter the sides of a triangle:'
    print(prompt)
    side_1 = int(input('\nSide 1: '))
    side_2 = int(input('Side 2: '))
    side_3 = int(input('Side 3: '))
    ptriple(side_1, side_2, side_3)
    

def ptriple(side_1, side_2, side_3):
    s1 = side_1**2 + side_2**2
    s2  = side_1**2 + side_3**2
    s3 = side_2**2 + side_3**2
    if s1 == side_3**2:
        print('\nThis is a Pythagorean triple!')
        replay()
    elif s2 == side_2**2:
        print('\nThis is a Pythagorean triple!')
        replay()
    elif s3 == side_1**2:
        print('\nThis is a Pythagorean triple!')
        replay()
    else:
        print('\nThis is NOT a Pythagorean triple :(')
        replay()
         

def replay():
    print ('\nDo you want to try again? Y/N')
    reply = input()
    if reply == 'Y':
        ptc()
    elif reply == 'N':
        print('Have a great day!')
        exit()
    else:
        print('My apologies, I did not catch that. Please repeat.')
        Replay()
    
ptc()






def age():

    age = 22
    name = 'Andrew'
    driving = True

    # print(age > 22)
    # print(age < 22)
    # print(age >= 22)
    # print(age <= 22)
    # print(age == 22)
    # print(age != 22)
    # print(age == 22 and name == 'Andrew')
    # print(age == 22 or name == 'Henry')
    # print(not age == 22)

    if age > 18:
        if driving == True:
            print('Take a diet coke on me.')
        else:
            print('Take a beer on me.')
    else:
        print('Take a fanta on me.')
    print('Thanks.')

def grade():
    grade = input('Input your grade: ')

    if grade == 'A':
        print('You got an A, yay!')
    elif grade == 'B':
        print('You got a B, good job!')
    elif grade == 'C':
        print("You got a C, that's okay.")
    elif grade == 'D':
        print("You got a D, don't beat yourself up.")
    else:
        print("That's impossible!")

#age()
grade()
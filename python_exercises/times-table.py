number = int(input("Input a number: "))
numbers = []
for i in range(number):
    for j in range(number):
        calc = (i+1)*(j+1)
        numbers.append(str(calc))
    print(' '.join(numbers))
    numbers=[]
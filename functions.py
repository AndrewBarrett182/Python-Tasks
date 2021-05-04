def hi_user(first_name, last_name):
    print("Hello" + " " + first_name + " " + last_name)

#hi_user("Bill", "Steves")

def add_calc(number1, number2):
    answer = number1 + number2
    return answer

# added_number = add_calc(5,5)

# print(added_number + 20)

def absolute(num):
    if num >= 0:
        return num
    else:
        return -num

print(absolute(-4))
print(absolute(5))
#Strings
word1 = "Good"
word2 = "Day"
word3 = "Andrew"
sentence = word1 + " " + word2 + " " + word3
print(sentence)

#Integers and Floats
number1 = input("Enter a whole number: ")
number2 = input("Enter a decimal number: ")

integer_number = int(number1)
float_number = float(number2)
round_number = int(round(float_number))

print(number1)
print(number2)
print(round_number)

#Boolean
name = "Sam"
age = 3
bark = True
tweet = False

#print("My pet is called " + name + ", He is", age, "years old.")
print(f'My pet is called {name}, He is {age} years old.')
print("Statement:", name, "barks =", bark)
print("Statement:", name, "tweets =", tweet)
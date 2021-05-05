# import math

# number = float(input("Enter a number: "))
# answer = math.sqrt(number)

# print(answer)

#--------------------------------------------------

# import math
# import random

# def multiply_pi():
#     return random.randint(1,10) * math.pi

# for i in range(5):
#     print(multiply_pi())

#--------------------------------------------------

from math import pi
from random import randint

def multiply_pi():
    return randint(1,10) * pi

for i in range(5):
    print(multiply_pi())
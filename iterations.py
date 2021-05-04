# Iterations

## I want Shane to do 1000 push ups

### How do I show him how to do 1000 push ups?

### Loops

## While

number = 1
print(number)

while number < 5:
    number = number + 1
    if number == 3:
        continue # continue while loop without performing next code
        #break # break out of the loop completely
    print(number)

# For Loops

# for i in [0, 1, 2, 3, 4, 5]:
#     print(i)

# print(list(range(1,100)))

for i in range(10):
    for j in range(5):
        print(f"First Loop: {i}, Second Loop: {j}")
math = int(input('What was your maths mark? '))
chem = int(input('What was your chemistry mark? '))
phys = int(input('What was your physics mark? '))

total = (math + chem + phys) / 3

print(f"Overall percentage = {total}%")

if total < 40:
    print("You failed")
elif (total >= 40) and (total < 50):
    print("D")
elif (total >= 50) and (total < 60):
    print("C")
elif (total >= 60) and (total < 70):
    print("B")
elif (total >= 70):
    print("A")
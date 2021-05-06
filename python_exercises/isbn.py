isbn = "978-0-306-40615-?"
temp = isbn.replace("-", "")
temp = temp.replace("?", "")

digits = list(temp)
for i in range(len(digits)):
    digits[i] = int(digits[i])

last_digit = 10 - (( digits[0] + (3 * digits[1]) + digits[2] + (3 * digits[3]) + digits[4] + (3 * digits[5]) + digits[6] + (3 * digits[7]) + digits[8] + (3 * digits[9]) + digits[10] + (3 * digits[11]) ) % 10)
output = isbn.replace("?",str(last_digit))
print(output)
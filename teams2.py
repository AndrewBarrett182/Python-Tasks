file = open("teams.txt", "r")
lines = file.readlines()
final = ""
for i in range(len(lines)):
    if i == 0:
        final = final + "This is a new line \n"
    else:
        final = final + lines[i]

file.close()
file = open("teams.txt", "w")
file.write(final)
file.close()
file = open("teams.txt", "r")
lines = file.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", "")
for i in range(len(lines)):
    print(lines[i])
file.close()
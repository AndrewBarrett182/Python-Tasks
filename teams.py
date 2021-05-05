file = open("teams.txt", "w")
for i in range(5):
    teams = input("Input a name of a sports team: ")
    line = teams + "\n"
    file.write(line)
file.close()
file = open("teams.txt", "r")
lines = file.readlines()
print(f"This is the 1st line: {lines[0]}")
print(f"This is the 5th line: {lines[4]}")
# file = open("filename.txt", "w")

# for n in range(1,11):
#     newline = "This is line " + str(n) + "\n"
#     file.write(newline)

# file.close()

#------------------------------------------------

file = open("filename.txt", "r")

outfile = ""

for line in range(1, 10):
    if line % 2 == 0:
        outfile += file.readline()
    else:
        file.readline()

file = open("filename.txt", "w")
file.write(outfile)
file.close()
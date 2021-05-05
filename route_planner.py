#incomplete
peaks = input("Enter your peaks: ")
peaks = peaks.split()
for i in range(len(peaks)):
    peaks[i] = int(peaks[i])

best = [peaks[0]]
element = 1
while element < len(peaks):
    temp = [peaks[0]]
    current = 0
    current_position = 0
    for i in range(element, len(peaks)):
        pos = i
        for j in range(pos, len(peaks)-1):
            if (peaks[pos] < peaks[j+1]) and (peaks[j] > current):
                if peaks[j] > peaks[j+1]:
                    pos = j + 1
                    break
                else:
                    pos = j
                    break
        #print(pos)
        #print(current)
        if (peaks[pos] > current) and (pos > current_position):
            temp.append(peaks[pos])
            current = peaks[pos]
            current_position = pos
        #print(current, " 2")
    if len(temp) > len(best):
        best = temp
    print(temp)
    element = element + 1
#print(best)
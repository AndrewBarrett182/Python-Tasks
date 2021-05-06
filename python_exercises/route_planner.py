#incomplete
peaks = input("Enter your peaks: ")
peaks = peaks.split()
for i in range(len(peaks)):
    peaks[i] = int(peaks[i])

best = []
length = 0
element = 1
while element < len(peaks):
    temp = [peaks[0]]
    current = 0
    current_position = 0
    for i in range(element, len(peaks)):
        pos = i
        for j in range(pos, len(peaks)-1):
            #if (peaks[pos] < peaks[j+1]) and (peaks[j] > current):
            if peaks[j] > current:
                if (peaks[j] > peaks[j+1]) and peaks[j+1] > current:
                    pos = j + 1
                    break
                else:
                    counter = j
                    longest_path = []
                    #print("this is current", current)
                    while counter < len(peaks) - 1:
                        biggest = current
                        longest = []
                        for k in range(counter, len(peaks) - 1):
                            if (peaks[k] > biggest) and (current < peaks[k]):
                                biggest = peaks[k]
                                longest.append(biggest)
                        if len(longest) > len(longest_path):
                            longest_path = longest
                        counter = counter + 1
                    #print("this is long", longest_path)
                    pos = longest_path.pop(0)
                    #pos = j
                    break
        #print(pos)
        #print(current)
        if (peaks[pos] > current) and (pos > current_position):
            temp.append(peaks[pos])
            current = peaks[pos]
            current_position = pos
        #print(current, " 2")
    if len(temp) >= length:
        best.append(temp)
        length = len(temp)
    #print(temp)
    element = element + 1
print(best)
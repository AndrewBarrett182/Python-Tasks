peaks = input("Enter your peaks: ")
peaks = peaks.split()
for i in range(len(peaks)):
    peaks[i] = int(peaks[i])

start = peaks.pop(0)
last = peaks.pop()
temp = peaks
route = []
route.append(start)
while len(temp) > 0:

    smallest = min(temp)
    
    if temp[0] == smallest:
        route.append(smallest)
        temp.pop(0)
    else:
        while temp[0] != smallest:
            temp.pop(0)
route.append(last)
print(route)















# Smallest increase in altitudes:

# peaks = input("Enter your peaks: ")
# peaks = peaks.split()
# for i in range(len(peaks)):
#     peaks[i] = int(peaks[i])


# temp = peaks
# route = []

# while len(temp) > 0:

#     smallest = min(temp)
    
#     if temp[0] == smallest:
#         route.append(smallest)
#         temp.pop(0)
#     else:
#         while temp[0] != smallest:
#             temp.pop(0)
# print(route)
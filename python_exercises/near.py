def near(string1, string2):
    string1_list = list(string1)
    string2_list = list(string2)
    for i in range(len(string1_list)):
        temp = string1_list.pop(i)
        if string1_list == string2_list:
            return True
        string1_list = list(string1)
    return False

print(near("reset", "rest"))
print(near("dragoon", "dragon"))
print(near("eave", "leave"))
print(near("sleet", "lets"))
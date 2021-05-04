# Collections

## Grouping data

### List

#### Ordered group of data

list_1 = [10, 0.1, 'hello', True]

#          0       1       2      3
names = ['Ben', 'Luke', 'Nick', 'Jay']
towns = ['Bolton', 'Chorley']
animals = ["Dog", "Cat", "Dog"]

all_things = [names, towns, animals]

print(names[1])
print(all_things[1][1])

animals.append("Horse")
print(animals)

animals.remove("Cat")
print(animals)

animals.reverse()
print(animals)

print(animals.count("Dog"))

print(len(animals))

new_string = " and ".join(animals)
print(new_string)

print(names)
names.sort()
print(names)

### Tuples

#### Collection of data, immutable, CANNOT BE CHANGED

my_new_tuple = ("Ben", 0, 4, False, 0.6)
print(my_new_tuple[0])

### Dictionaries

#### Key-value pair, UNORDERED

my_dict = {
    "name": "Andrew",
    "age": "22",
    "Hungry": True,
    "Favourite_Foods": ["Bagels", "Water"]
}

my_dict["Ready_for_the_weekend"] = True
my_dict.pop("name")

print(my_dict["age"])
print(my_dict["Favourite_Foods"][0])
print(my_dict)
print(my_dict.keys())
print(my_dict.values())

people = [
    {"name": "Andrew", "age": "22"}, 
    {"name": "Ben", "age": "18"}
]

print(people[0]["age"])
# class Dog:
#     energy = "high"

#     def speak(self):
#         print("woof")

# bilbo_waggins = Dog()
# print(bilbo_waggins.energy)
# bilbo_waggins.speak()

# chewbarka = Dog()
# chewbarka.energy = "low"
# print(chewbarka.energy)
# chewbarka.speak()

#---------------------------------

class Dog:
    def __init__(self, name, breed, energy):
        self.name = name
        self.breed = breed
        self.energy = energy

dog1 = Dog("Ross Barkley", "Jack Russel", "High")
dog1.sleep = True
print(f"Name: {dog1.name}, Breed: {dog1.breed}, Energy: {dog1.energy}")
print(dog1.sleep)


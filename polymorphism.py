# class Bird:
#     def __init__(self, wingspan):
#         self.wingspan = wingspan

#     def __len__(self):
#         return self.wingspan

# eagle = Bird(104)

# print(len(eagle))

#--------------------------------------

class Animal:
    babies = 0 

    def reproduce(self):
        self.babies += 1

class dog(Animal):
    def reproduce(self):
        self.babies += 6

john = dog()
john.reproduce()
print(john.babies)
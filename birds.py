from abc import abstractmethod

class Bird:
    fly = True

    def noise(self):
        return("Birdnoise")

    babies = 0

    def reproduce(self):
        self.babies += 1

    @abstractmethod
    def eat(self):
        pass

    extinct = False

class Owl(Bird):

    def reproduce(self):
        self.babies += 6

    def eat(self):
        return("Peck Peck")

class Dodo(Bird):
    Fly = False
    extinct = True

    def eat(self):
        return("Nom Nom")

    def reproduce(self):
        if self.extinct == False:
            self.babies += 1
        else:
            return("No more dodos")

#changed print statements in functions to return so I can print the
#string outside of the class
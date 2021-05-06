class Students:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.class_ = "student"
    
    def average(self, test_score1, test_score2, test_score3):
        print((int(test_score1) + int(test_score2) + int(test_score3)) / 3)

student = Students("Andrew", 22)
average = student.average(88, 90, 65)
class firstClass:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
    #myName = "Lesley"
        print("Hello World " + self.firstName + " " + self.lastName)


newClass = firstClass("Lesley", "Bonyo")
print(newClass)

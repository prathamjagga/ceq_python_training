# the following file contains the solution for assignment 7

## (1) which attribute will get preference ? instance or class
# the instance attribute will get preference


class Employee:
    company = "hello"
    id = 589
    designation = "Software Trainee"

    def __init__(self, company=None):
        self.company = company

    # @staticmethod
    def hello(self):
        print(self.designation)


akash = Employee("Google")

akash.company = "Amazon"  ## instance attribute

Employee.company = "McKisney & Co."  ## class attribute

print(akash.company)  ## prints Godrej

akash.hello()


## (2)  Create a class with an constructor and 2 functions
## create 3 objects with different props and call the functions
## for them


class VisualModel:
    def __init__(self, model=None, trainingSize=None, accuracy=None):
        self.model = model
        self.trainingSize = trainingSize
        self.accuracy = accuracy

    def getDetails(self):
        return self.model, self.trainingSize, self.accuracy

    def updateAccuracy(self, accuracy):
        self.accuracy = accuracy


# object 1
visObj1 = VisualModel(model="XGBoost", trainingSize=30000, accuracy=90)
print(visObj1.getDetails())
visObj1.updateAccuracy(30)  ## updating data
print(visObj1.accuracy)


# object2
visObj2 = VisualModel()
print(visObj2.getDetails())

## object3
visObj3 = VisualModel(model="RandomForest", trainingSize=50000, accuracy=95)
visObj3.model = "SGD"
print(visObj3.getDetails())


## (3) Class method and super keyword?

## Class method: These methods are bound to a class rather than an object.
##  Class methods can be called by both class and object.

## Super Keyword: The super keyword is used to access the
## attributes of the parent class

## this file contains the solution with code for the assignment 1

## (1) Type casting

## What is type casting? Type casting is nothing but casting objects to different types 
## as per the requirements. But what do we mean by casting? casting is nothing but changing,
## like casting int to float refers to changing integer value to a float value
## there will be situations where we need the answer in float format but due to the use 
## of int data type or the number in the form of int will lead to the overall ans in the form of
## integer only and vice versa. So, in those scenarios type casting is used. Let us see some 
## examples below

## note: we have different functions such as int(), float() and str() which take 
## a value as an argument and returns the result in the form of a different data type
## which is indicated by their name

discount = 7.5

actual_price = 100

discounted_price = actual_price  - (actual_price*discount)/100

print(discounted_price)  ## result : 92.5 which is float

## now suppose we want this price in the form of int only, we can then type cast it as int

print(int(discounted_price))  ## result: 92 this will round off the result to 92 only and 
                              ## remit the values after the decimal point

## let us now convert the discounted price to a string using str()

discounted_price = str(discounted_price)

print(type(discounted_price)) ## will print <class 'str'>

## now discounted price can be used as a string, thanks to type casting it makes 
## working with different types of values flawless 




## (2) Examples of tuples, list and dictionary

## Tuples are immutable so definitely we can use them where we need some kind of 
## a list which is constant throughout the execution of a program, let us have a 
## tuple which is a group of strings representing all the four quarters of an year,
## Q1,Q2,Q3,Q4. These will be constant throughout and whenever we need the representation
## of a quarter we can definitely refer to the value of this tuple at the position i-1
## for the i-th quarter

quarterTuple = ("CEQ-Q1","CEQ-Q2","CEQ-Q3","CEQ-Q4")

## let us print the third quarter

print(quarterTuple[3-1])  ## result: CEQ-Q3


## List is simply a group of values, possibly of different data types, different sizes,
## extendable, reducible and flexible

## suppose we want to also add the top employee for each quarter then we can also add that in our list 
## and after every cycle we can change the top employee of the quarter, because lists are mutable
## huh definitely that is why they are so flexible, so let us add that

quarterList = ["CEQ-Q1","CEQ-Q2","CEQ-Q3","CEQ-Q4","Moiza Shafiq", "Naveen Singh", "Ronak Singh", "Sakshi Sharma"]
print("For quarter", quarterList[1-1], ", the best employee is ", quarterList[4+1-1], ".")



## Dictionaries come into play when we need to store the data as key value pairs like I want to store
## some info about the employees as the employee name as the key and value as their info as a string
## then we can use the dict, it is similar as hashmap in other languages

employeeInfoDict = {"Moiza Shafiq":"Python trainer at CEQ.", "Naveen Singh":"Some random employee","Ronak Singh":"Batch 8 Software Trainee at CEQ",
    "Pratham":"Batch 8 Software Trainee at CEQ"
}

print("For quarter", quarterList[1-1], ", the best employee is ", quarterList[4+1-1], ". Info about the employee: ", employeeInfoDict[quarterList[4+1-1]])

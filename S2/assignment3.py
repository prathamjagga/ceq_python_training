## this file contains the solution of assignment 3

import math

## (1) Diff between '==' and '===' operator?
## Well there is no '===' operator in python. But we can compare the 'is' and '==' operator 
## as we have discussed in the class. Actually the 'is' operator returns True or False on the 
## basis of whether any two objects are equal in terms of the reference or whether they are actually
## the same object in the memory. For example, a=1, b=1 these numbers have their value equal to 1 
## but they are not the same as they must be having assigned to a different part of the memory
## if one changes the other one is not affected
## so if we write a is b, it will definitely return False and so we can use the == operator to 
## compare them in terms of the value

a = 1
b = 1
print(a is b)  # False
print(a == b)  # True


## (2) use of if-else, pass and continue

## if else is used for conditional programming

num = int(input("enter a number\n"))
if(num<0):  ## to check for a condition
    print("number is negative")
elif(num==0):   #3 to check for another condition if the first is false, note that we can use multiple elif(s)
    print("number is zero")
else:           # what to do if every rearward condition was False
    print("number is positive")


## use of pass, their might be situations where we just want to keep and empty block but that is not allowed in python
## so we just write the pass keyword there and that acts as a placeholder there so that now we have an indented block but empty

if(num<0):
    pass ## we cant find the square root of num
else:
    print(math.sqrt(num))


## The continue keyword is used to skip an iteration in a loop
## jack likes only fresh fruit to eat, he will skip the rotten fruits while eating

fruits = {"fresh guava", "rotten pineapple", "fresh kiwi"}

for fruit in fruits:
    print(fruit)
    if fruit.__contains__("rotten"):
        continue
    else:
        print("Jack will eat it")


## the range functions can be used with one, two or three arguments
## variation 1: range(stop_value)
## variation 2: range(start, stop) this has the default step size of 1
## variation 3: range(start, stop, step_size) ## we can pass a step size here

## suppose we want only those numbers which are a multiple of 10 within range 0 to 50 then we use a step size of 10

print(list(range(0,51,10)))




## Use of break: now in our example of jack eating fruits suppose jack does not skip the rotten fruit but still he eats 
## a rotten fruit then jack dies and thus stops eating any subsequent fruits, here we can use a break statement so that
## the loop will end right there and jack is unable to eat fruits in next iterations as he dies


for fruit in fruits:
    print(fruit)
    if fruit.__contains__("rotten"):
        print("Jack will eat it")
        print("Oh he eats a rotten fruit, jack dies")
        break
    else:
        print("Jack will eat it")

## after eating  a rotten pineapple he dies and cannot proceed to eating kiwi

# What is start, stop and step in range function?
# start is nothing but from where the range begins, stop is nothing but the next value to the last value of the range,
# step is nothing but the difference between two subsequent elements in a range, if step is greater than 1 then definitely
# the elements are not continuous, yet discrete in that range.
# range(start=0, stop=51, step=10)


print(list(range(0,51,10)))  ## taking the previous example here
open('assignment1.py','r')

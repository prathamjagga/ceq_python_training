## this file contains the solution to the 4th assignment

import os

## (1) Implementation of recursion: let us implement a range
## fuction with recursion


def rangeImplementation(l,r,step=1):
    if l>=r:
        if l==r:
            print(l)
        return
    else:
        print(l)
        rangeImplementation(l+step, r,step)

rangeImplementation(1,5,2)  ## prints: 1 3 5, basically 1 to 5 with step of 2
rangeImplementation(1,5)  ## prints 1 to 5





## Lambda functions: anonymous functions with one return statement
## let us take an example where the lambda function returns the cube of a number

cube = lambda x: x*x*x

print(cube(3))





## (2) Using lamda inside another function. It can be done in 2 ways:

## (i) function which returns a lambda function

def square():
    return (lambda x: x*x)

## thie above function returns a lambda function which return the square of the input


## (ii) The second variation is :using the lambda functions as parameters 
## to some another function

sq = lambda x: x*x
cube = lambda x: x*x*x

def doMaths(num, sq,cube, operation):
    if(operation=='square'):
        return sq(num)
    elif(operation=='cube'):
        return cube(num)
    else:
        return "invalid operation"


## let us pass the sq and cube lamda functions to doMaths and call it with both 
## the two variations

print(doMaths(5, sq, cube, "square"))  ## 25
print(doMaths(5, sq, cube, "cube"))    ## 125
print(doMaths(5, sq, cube, "sqrt"))    ## invalid operation





## (3) File IO
## Note that we will be doing everything using 'with open' instead of 'open'
## so that the file will automatically be closed at the end

# (i) Creating a new file

with open('newTextFile.txt', 'w') as f:
    pass

# (ii) Writing to the file

with open('newTextFile.txt', 'w') as f:
    f.write("Hello world this is Pratham\nHow are you doing?\nI am doing fine!")

# (iii) Appending to the file

with open('newTextFile.txt', 'a') as f:
    f.write("\nThis is the new line that I have appended")

# (iv) Reading one line at a time, reading the whole file, reading a specific 
# amount of characters

with open('newTextFile.txt', 'r') as f:
    data = f.read(5)  ## read first 5 chars
    print(data)
    data = f.read()  ## read the whole file
    print(data)
    data = f.readline()   ## reading the first line
    print(data)
    data = f.readline()   ## reading the second line
    print(data)

    
    
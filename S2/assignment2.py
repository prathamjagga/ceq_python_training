## this file contains the solution for assignment 2

## (1) Accessing an element in a set

my_set = {"radio", "smartphone", "laptop", "laptop", "TV", 30, 20 ,10}

## accessing either means:
## (i) accessing each element one by one

for element in my_set:   ## we can just use a for loop to iterate, note that dup. elems are ignored
    print(element)

## (ii) checking the existence of an element

print("TV" in my_set)  # True
print("refrigeratier" in my_set)  # False
print(30 in my_set)  # True




## (2) Discard vs Remove
## Both of them serve a same purpose, but the difference is remove will raise an error if the entity too remove does not exists
## where as discard will work flawlessly, either it exists or not. Both of them have different use cases. For the cases where we need
## to have a strict rule that the element to be removed must be existing, remove is used. Discard can be used otherwise.

my_set.remove("TV") ## no error

my_set.discard("TV") ## no error

# my_set.remove("TV") ## raises an error



## (3) Intersection Update: This function is used to get an intersection of some set with another set.

x = {"A", "B", "C"}
y = {"C", "B", "D", "E"}

x.intersection_update(y)

print(x)




## (4) Symmetric Difference Update: This function is used to get an inverse of intersection of some set with another set.

x.symmetric_difference_update(y)

print(x)



## (5) dict(): It is a method to create a dictionary. Returns an object of class 'dict', takes named arguments as key and value pairs.

my_dict = dict(name="Pratham", year=2)
print(my_dict)

## note that the arguments names are converted to strings and values remain as it is.
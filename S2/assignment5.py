## this file contains the solution of assignment 5

import json


## (1) (i) The JSON.dumps function and its parameters:
## This function converts a variety of python onjects to
## json strings..

# obj: Serialize obj as a JSON formatted stream
# skipkeys: If skipkeys is True (default: False), then dict keys that are not of a basic type (str, int, float, bool, None) will be skipped instead of raising a TypeError.
# ensure_ascii: If ensure_ascii is True (the default), the output is guaranteed to have all incoming non-ASCII characters escaped. If ensure_ascii is False, these characters will be output as-is.
# check_circular: If check_circular is False (default: True), then the circular reference check for container types will be skipped and a circular reference will result in an OverflowError (or worse).
# allow_nan: If allow_nan is False (default: True), then it will be a ValueError to serialize out of range float values (nan, inf, -inf) in strict compliance of the JSON specification. If allow_nan is True, their JavaScript equivalents (NaN, Infinity, -Infinity) will be used.
# indent: If indent is a non-negative integer or string, then JSON array elements and object members will be pretty-printed with that indent level. An indent level of 0, negative, or “” will only insert newlines. None (the default) selects the most compact representation. Using a positive integer indent indents that many spaces per level. If indent is a string (such as “\t”), that string is used to indent each level.
# separators: If specified, separators should be an (item_separator, key_separator) tuple. The default is (‘, ‘, ‘: ‘) if indent is None and (‘, ‘, ‘: ‘) otherwise. To get the most compact JSON representation, you should specify (‘, ‘, ‘:’) to eliminate whitespace.
# default: If specified, default should be a function that gets called for objects that can’t otherwise be serialized. It should return a JSON encodable version of the object or raise a TypeError. If not specified, TypeError is raised.
# sort_keys: If sort_keys is True (default: False), then the output of dictionaries will be sorted by key.


myDict = {("a"): "Hey", 2: "3", "a": "b", "number": float("nan")}

serialized_to_json_str = json.dumps(
    myDict,
    skipkeys=True,  ## skips non basic keys like lists, tuple, dict
    allow_nan=True,  ## to allow nan values
    indent=6,  ## for formatting
    separators=(", ", "--"),  ## you can see them in the output
    sort_keys=False,  ## to sort the result based on the keys
)

## note that as we have taken a dictionary having keys of diff data types
## we cant use the sort keys as true


print(serialized_to_json_str)


## (2) Simple program to illustrate the use of raise Keyword

try:
    n = int(input("enter a number"))
    if n == 1:
        raise IndexError()
    if n == 2:
        raise KeyError()
    else:
        print("No error")

except IndexError:
    print("index error")
except KeyError:
    print("key error")


## (3) List Comprehension
## it is a shorter way of creating another list
## from some list based on some condition or rule


# (i) condition less
mylistodd = [1, 3, 5, 7, 9]

mylisteven = [x + 1 for x in mylistodd]

print(mylisteven)

# (ii) conditional

mylist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

mylisteven = [x for x in mylist if x % 2 == 0]

print(mylisteven)

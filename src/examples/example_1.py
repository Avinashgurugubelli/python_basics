

# To print to console
print("Hello world!")

# Global variable
title = "Welcome to programming"


def print_title():
    """
        Multi line comment:
        Prints the title to the console.
    """
    global title, name
    title = "Welcome to python programming"
    # TO create a global variable inside a function, you can use the global keyword in function.
    name = "Martin"
    print(title)


print('Global variable: '+title)
print_title()
print('Global variable after fun call: '+title)
print("Name: " + name)

"""
Python Data types:
String  ->   v = "some text"
int     ->   n = 30
float   ->   f = 30.5
list   ->    a = ["A", "B", "C"]
tuple   ->   t = ("A", "B", "C)
set     ->   s = {"Jack", 30}
dict    ->   d = {"Name": "Jack", "Age": 30}
range   ->   r = range(6) -> 0 to 6

n = 30
# type is a predefined function in python to return data type of a variable
print(type(n)) #int

"""

# Casting

# n = 40
# n1 = str(n)
# print(type(n1)) #str

"""
LIST:
- Allows duplicates, since the lists are indexed.
- Access an element -> name_of_list[index] e.g. list1[0]
- When you are trying to access the element beyond the range it will throw 'IndexError: list index out of range'
- length of the list: len(list1)
- Can store multiple data type values e.g. ["A", 30, "B"]
- Ordered

list1 = ["A", 'B', 'C', "A", 60]
list1[0] = "XYZ"
Accessing the list element
print(list1[0])
list1.append("D")
print(list1)
print(type(list1))
"""


"""
Tuple
- Allows duplicates, since the tuples are indexed.
- Access an element -> name_of_tuple[index] e.g. t[0]
- When you are trying to access the element beyond the range it will throw 'IndexError: list index out of range'
- Can store multiple data type values e.g. ["A", 30, "B"]
- Ordered

t = ("A", "B", "C", "A")
t1 = ("X", "Y")
t2 = "x", "y", "z"
print(type(t))  # tuple
print(t[len(t) - 1])
print(len(t))
t[0] = "Foo" # TypeError: 'tuple' object does not support item assignment

Slicing variable_name[start_index: end_index] -> start_index -> end_index - 1
t[0:2]  # A, B
Tuple joining
t3 = t+t1
print(t3)

print(t.count("a"))
"""
# s = {"Jack", 30, 30}
# print(s)

# d = [{"name": "Avi", "age": 20}]

"""
if --- else
"""
a = 30
b = 30
if (a > b):
    print("true")
elif (a == b):
    print("equals")
else:
    print("false")


# For LOOP
# list1 = ["A", 'B', 'C', "A", 60]

# for ele in list1:
#     print(ele)

# for ele in name:
#     print(ele)


num = 1
while num < 6:
    print(num)
    num = num+1

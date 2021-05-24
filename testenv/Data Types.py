children = "Tommy"
_yutes = ["Kim", "Tim", "Amanda"]



print(children)
print("These are my kids: ", _yutes )

for kids in ["Caleb", "Sydney", "Savannah"]:
    print("Clean your room,", kids, "!")

# This is a comment.
''' This is also a comment.'''
""" This is also a comment, 
    using 3 strings 
    of Quatations."""

print(2 * 2 * 2 * 2 * 2 * 2 * 2 * 2)

# 0b or 0B to specify binary
# 0o or 0O to specify Octal
# 0x or 0X to specify hex

print(0xbadbeef)
print(hex(195935983))
print(bin(195935983))

children = "Tommy"
print(children[0:2])
print("Jack" + children * 5)

# To initialize a "list" variable in an empty state.
emptylist = []
emptylist2 = list()

print(_yutes[1])
print(_yutes[2])
print(_yutes[0])

_yutes[2] = "Samantha"
print(_yutes[2])

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
print(c[1:4])
print(c[ :-4])
print(c[:])

#This is a "Tuple" data type. It is immutable, unlike a "List" or "String". Made using () and not [] like with "Lists"
person = (2012, 'Mike', "CCNA")
print(person)
print(type(person))
print(person[0])
#Because a Tuple is immutable, you cannot make changes to the assigned variable indexes.
""" person[0] = 2015 """
#However it can be used to assign a set variables quickly
(x, y, z) = (12, 'Fred', 18)
print(z)

#A "Dictionary" provides another way of creating a collection of items.
cabinet = { "scores": (98,76,95), "name":"Crhis", "company" : "Cisco"}
print(type(cabinet))
print(cabinet)
print(cabinet["scores"])

#Adding more Keys and Values to a Dictionary.
cabinet["address"] = {"street":"123 Anywhere Dr", "city":"Franklin"}
print(cabinet)

#Sets : These are mutable data types that can be made immutable using "Frozen Sets"
numbs = {1,2,4,5,6,8,10}
odds = {1,3,5,7,9}
print(type(numbs))
print(type(odds))

#You can use "|" operator to show a combined set with no duplicates.
print(numbs | odds)

# You can use "&" operator to show an intersection of two sets and what numbers are in both sets
print(numbs & odds)

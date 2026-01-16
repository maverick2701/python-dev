# Python Collections (Arrays)
# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# The primary difference between a Python list and a tuple is that a list is mutable (changeable), while a tuple is immutable (unchangeable) after creation. 
# Set is a collection which is unordered, unchangeable, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members
#-------------------------------------------------------------------------------------------

# List
# Lists are used to store multiple items in a single variable.
# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
print(thislist[3])
thislist.append("mango") #append element to the end of the list
print(thislist)
thislist.append(10)
print(thislist)
print(f"""The number of occurences of banana in the list is {thislist.count("banana")}""") #Use triple quotes if you need to use double quotes inside f-string
thislist.pop()
print(thislist)
#-------------------------------------------------------------------------------------------

# Tuple
# Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.

thistuple = ("Tom", "Dick", "Harry")
print(thistuple)

print(f"Harry is at index {thistuple.index('Harry')}")

#--------------------------------------------------------------------------------------------
# Set
# Sets are used to store multiple items in a single variable.
# A set is a collection which is unordered, unchangeable*, and unindexed.
# Set items are unchangeable, but you can remove items and add new items.
# Set items are unordered, unchangeable, and do not allow duplicate values.
myset = {"apple", "banana", "cherry", "apple"}
print(myset)

# A set can contain different data types
set1 = {"abc", 34, True, 40, "male"}
set1.add(5)
print(set1)

set1.remove('abc') #removes a specific element from a set
print(set1)
print(f"The length of set1 is {len(set1)}")

set1.pop() #removes any random element from a set
print(set1)
print(f"The length of set1 is {len(set1)}")

print(type(myset))
#-------------------------------------------------------------------------------------------

# Dictionary
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
# Dictionaries are written with curly brackets, and have keys and values:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict["model"])
print(thisdict)
print(thisdict.keys())
print(thisdict.values())

print(type(thisdict))
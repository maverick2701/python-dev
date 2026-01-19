num1 = 5
num2 = num1

print("Before num2 is updated")
print("num1 = ", num1)
print("num2 = ", num2)

print("\nnum1 points to ", id(num1))
print("num2 points to ", id(num2))

num2 = 7
print("\nAfter num2 is updated")
print("num1 = ", num1)
print("num2 = ", num2)
print("\nnum1 now points to ", id(num1))
print("num2 now points to ", id(num2))

dict1 = {
         'value': 11
        }

dict2 = dict1 

print("\n\nBefore value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2)) 

dict2['value'] = 16

print("\nAfter value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2) 

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))
def greet():
    print("Hello World!")

greet()

def greet(name="John"):
    print("Hello, " + name)

greet()

x = 17
y = 25
def add_numbers(a,b):
    return a + b

print(f"The sum of {x} & {y} is {add_numbers(x,y)}")

sum = add_numbers(6,5)
result = 2 * sum
print(result)

# Function simulating overloading
def greet_revised(name, age=None):
    if age:
        return f"Hello {name}, your age is {age}"
    else:
        return f"Hello {name}"

print(greet_revised("Vinod", 52))
print(greet_revised("James"))


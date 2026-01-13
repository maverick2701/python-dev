# Big O: n, 2n, n squared, 1, log(n)

# O(n)
def print_items_order_n(n):
        for i in range(n):
             print(i)

# O(2n) - drop constants
def print_items_order_2n(n):
    for i in range(n):
        print(i)
    for j in range(n):
        print(j)

# O(n squared)
def print_items_order_n_squared(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
     
# O(n squared + n) - drop non-dominants
def print_items_order_n_squared_plus_n(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
    
    for k in range(n):
        print(k)

# O(1)
def add_items(n):
    print(n + n)


print_items_order_n(10)    
print_items_order_2n(10)
print_items_order_n_squared(10)
print_items_order_n_squared_plus_n(10)
add_items(10)
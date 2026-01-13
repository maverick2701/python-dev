#Big O: n, 2n, n squared, log(n)

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
     

print_items_order_n(10)    
print_items_order_2n(10)
print_items_order_n_squared(10)
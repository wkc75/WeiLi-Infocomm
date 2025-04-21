# option 1
# here, a variable called "cart" is decalred
# and it is a list
cart = [10, 20, 30, 40, 50]

# here, another variable called "total_cost" is declared
# and it has a value of 0
# it is a int
total_cost = 0

# for loop
for item in cart:
    # total_cost = total_cost + item
    total_cost += item 

# only prints "Total cost: "
print("Total cost: ", total_cost)

# option
cart = [10, 20, 30, 40, 50]

# len(cart) = 5
# range(5)
for i in range(len(cart)):
    total_cost += cart[i]

x = input("Enter a number: ")
if type(x) != int:
    print("Only Numbers!!!")

y = int(input("Enter another number: "))
z = int(input("Enter the last number: "))



# finding the largest number
if x > y and x > z:
    print("x is the greatest")
elif y > x and y > z:
    print("y is the greatest")
else:
    print("z is the greatest")

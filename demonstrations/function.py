# BMI Calculator
def calculate_BMI(weight, height):
    BMI = weight / (height * height)
    return BMI

weight = input("Enter your weight in kg: ")
height = input("Enter your height in meter: ")

BMI = calculate_BMI(float(weight), float(height))

if BMI >= 27.5:
    print("High Risk")
elif 23.0 < BMI and BMI < 27.4:
    print("Moderate Risk")
else:
    print("low risk")

# checks whether a number is even or not
# if the input number is true, the function returns true
# otherwise, returns false
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
    
print(is_even(932))

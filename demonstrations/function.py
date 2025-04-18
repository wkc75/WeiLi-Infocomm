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
''' This is a simple program to that interprets the Body Mass Index (BMI)
    based on a user's weight and height.
    Based on the BMI values:
        Under 18.5 is considered underweight
        Equal to or over 18.5 but under 25 is normal weight
        Equal to or over 25 but below 30 is slightly overweight 
        Equal to or over 30 but below 35 is considered obese
        Equal to or over 35 is clinically obese. '''

import math
# Height (meters m)
m = float(input("Height (in m): "))

# weight (kilograms kg) 
kg = float(input("Weight (in Kg): "))

bmi = round(kg / (pow(m,2)), 2)


if(bmi < 18.5):
    print(f'Your BMI is {bmi}, you are underweight.')
elif(bmi >= 18.5 and bmi < 25):
    print(f'Your BMI is {bmi}, you are normal weight.')
elif(bmi >= 25 and bmi < 30):
    print(f'Your BMI is {bmi}, you are slightly overweight.')
elif(bmi >= 30 and bmi < 35):
    print(f'Your BMI is {bmi}, you are obese.')
else:
    print(f'Your BMI is {bmi}, you are clinically obese.')


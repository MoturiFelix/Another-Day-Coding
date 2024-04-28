# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())

BMI = weight / (height * height)
print (f"your BMI is {BMI} and ")

if BMI < 18.5 :
  print ("You are underweight")
elif BMI < 25:
  print("You have a normal weight!")
elif BMI < 30:
  print("You are slightly Overweight!")
elif BMI < 35:
  print ("You are obese!")
else:
  print ("You are clinically Obese")
    


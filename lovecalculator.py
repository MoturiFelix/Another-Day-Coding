# python Love Calculator

print("The Love Calculator is calculating your score...")
name1 = input("What is your name? ")  
name2 = input("What is their name? ") 

combined_names = name1 + name2

#make lower case
lower_names = combined_names.lower()

#check the number of times a letter appears in the names
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")

first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")

second_digit = l + o + v + e

#add to get score and remember to change to string before adding

score = int(str(first_digit) + str(second_digit))

if  (score < 10) or (score > 90):
  print(f"Your Score is {score}, You go to gether like coke and Mentos.")
elif (score >= 40) and (score <= 50):
  print( f"Your Score is {score}, You are alright together")
else: 
  print(f"Your Score is {score}. ")

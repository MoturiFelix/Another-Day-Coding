print('welcome to the rollercoaster!')

height = int(input("what is your height in cm? "))
bill = 0

if height >= 120:
    print ("You can ride the rollercoaster! ")
    age = int(input("what is your age? "))
    if age < 12:
        bill = 5
        print("Child ticket is $5")
        
    elif age <= 18:
        bill = 7
        print("Youth tickets is $7")
    else:
        bill = 12
        print ("Adult ticket is $12.")   
    
    wants_photo = input("Do you want a photo taken? y or n. ")
    if wants_photo == "y" :
        bill +=3 

    print(f"Your final bill is {bill}")

else:
    print("sorry, you have to grow taller before you can ride. ")
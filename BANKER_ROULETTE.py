names =["Angela", "Ben", "Jenny", "Michael", "Chloe" ]
#ignore names_string which is not defined. 
import random

num_items = len(names)
random_name = random.randint(0,num_items -1)
person_who_will_pay = names[random_name]
print (person_who_will_pay + " is going to buy the meal today!")
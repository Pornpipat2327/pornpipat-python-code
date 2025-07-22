 # Complete this program to classify people by age
# age = int(input("Enter age: "))

# Add your if-elif-else statements here
# 0-12: Child
# 13-19: Teenager  
# 20-59: Adult
# 60+: Senior

# Your code here:

age = int(input("enter you age:"))
if age >= 0 and age <= 12:
    print("you are Child")
if age >= 13 and age <= 19:
    print("You are Teenager")
if age >= 20 and age <= 59:
    print("You are Adult")
if age >= 60:
    print("Your are Senior")            


import random
a=random.randint(1,5)
attempt=3
while attempt>=1:
    user=int(input("Enter the number 1 to 5 :" ))
    if(user==a):
        print(f"yeah the number {user} is correct")
    elif(user>a):
        print("you enterd the big number :")
    elif(user<a):
        print("you enterd the small number :")
    else:
        print("enter the valid number")
    attempt-=1
    if attempt==0:
        print("sorry you crossed the attempts limit , Try again")
    else:
        print(f"you have {attempt} attempts left")
        print("")
    if(attempt==0 or user==a):
        inp=input("continue(c) or exit(e)")
        if inp=="e":
            break
        else:
            attempt=3
        
        
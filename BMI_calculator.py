
print("Welcome to BMI calculator")
height=float(input("Enter your height in meter :"))
weight=int(input("Enter your weight :"))
def calc():
    bm1=(weight/height**2)
    bm2=float(format(bm1,".1f"))
    print("your bmi value is",bm2)
    return bm2
def check():
    bmi=calc()
    if(bmi<=18.4):
        print("You are under weight  because your Bmi is",bmi)
    elif(bmi>=18.5 and bmi<=24.9):
        print("You are Normal because your Bmi is",bmi)
    elif(bmi>=25.0 and bmi<=39.9):
        print("You are overweight because your Bmi is",bmi)
    elif(bmi>=40.0):
        print("You are obesity because your Bmi is",bmi)
check()

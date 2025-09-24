def add(a,b):#addition function
    print("addition value of a and b is ",a+b)

def sub(a,b):#subraction function
    print("subraction value of a and b is",a-b)
      

def mul(a,b):#multiplication function
    print("multiplication value of a and b is",a*b)
        

def divide(a,b):#subraction function
    c=0
    while(b==0):
         print("Enter the number above zero !!")
         c=int(input("Enter b value :"))
         b=c
    else:
        print("division value of a and b is",a/b)
lp=""
while(lp!="again"):
    a=int(input("Enter a value :"))
    b=int(input("Enter b value :"))            
    choice=input("Enter the operation (+,-,/,*) : ")
    if (choice=="+"):
        add(a,b)
    elif(choice=="-"):
        sub(a,b)
    elif(choice=="/"):
        divide(a,b)
    elif(choice=="*"):
        mul(a,b)
    else:
        print("Enter valid operation !!")
    lp=input("Enter again or quit :")

  


    
    
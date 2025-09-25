
ct = {
    1: "Hello!",
    2: "How can I help?",
    3: "Yes, that's correct.",
    4: "No problem!",
    5: "You're welcome.",
    6: "amazon ,flipkart",
    7: "tamil is the oldest language",
    8: "red",
    9: "puttin",
    10: "narendra modi"
}
print("hi , how can i help you today")
while True:
    user=input("bot : ")
    if user.lower() in ["bye","exit","quit"]:
        print("bot : goodbye!")
        break
    elif user.lower() in ["good morning"]:
        print("bot :good morning my friend") 
    
    elif user.lower() in ["tell me trending topics today"]:
        print("donald trump /n russian festivals /nindian cultures")
    elif user.lower() in ["you are my friend"]:
        print(ct[3])
    elif user.lower() in ["tell me ecommerce platform"]:
        print(ct[6])
    elif user.lower() in ["oldest language in the world"]:
        print(ct[7])
    elif user.lower() in ["colour of apple"]:
        print(ct[8])
    elif user.lower() in ["russian president name"]:
        print(ct[9])
    elif user.lower() in ["indian president name"]:
        print(ct[10])
    else:
        print("i can't understand what you told")
    
    
    
        
    
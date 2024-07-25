import random
x=int(input("enter the first limit = "))
y=int(input("enter the last limit = "))
l=0
key=random.randint(x,y)
def choose(): 
    user=int(input("your chance ... choose a no = "))
    global l
    l+=1
    return user
while(1):
    user=choose() 
    if(user<key):
        print("your prediction is less than the no ")
        print("next turn")
    elif(user>key):
        print("your prediction is greater than the no ")
        print("next turn\n\n") 
    elif(user==key):
        print("you rocked \nYou won!")    
        print(f"total chance you were taken is {l}")
        break
2
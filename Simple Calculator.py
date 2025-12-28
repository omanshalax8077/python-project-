# 1️⃣ Simple Calculator
# Concepts: functions, if-elif, operators
# Operations:
# Addition
# Subtraction
# Multiplication
# Division

def aad(x,y):
    return x+y

def mul(x,y):
    return x*y

def sub(x,y):
    return x-y

def div(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def main():
    while True:
        print("\n======== Simple Calculator ========")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        
        choice=int(input("Enter the choice "))
        
        if choice==5:  
            print("Thank you for using the system!")   
            break
    
        x=float(input("Enter the first number = "))
        y=float(input("Enter the second number = "))
        
        if choice==1:
            print("Addition = ",aad(x,y))
            
        elif choice==2:
           print("Subtraction = " ,sub(x,y))
            
        elif choice==3:
            print("Multiplication = ",mul(x,y))
            
        elif choice==4:
            print("Division = ",div(x,y))   
                 
        else:
            print("something is worring.....")
main()
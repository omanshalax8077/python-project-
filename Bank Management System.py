import random
print("====== Welcome To Bank Interface =====")

balance=100

def new_acount():
    global balance
    #personal information 
    name=input("Enter a name of costumer =")
    adhar=(input("Enter a Adhara number of costumar = "))
    pan=(input("Enter a PAN number of costumar = "))
    #chacking 
    print("Plz. Waiting....... ",)
    print("chacking Know Your Customer (KYC) verification........ ")
    print("Acount Opening successfully ✅")
    #account number 
    acount_number=" ".join(random.sample("0123456789",8))
    print("Your account number = ",acount_number)
    #file saving 
    print("file saving..... ")
    balance=100
    with open("Acount.txt ","a")as file :
        file.write("Name = " + name + "\n")
        file.write("Adhara = " + adhar + "\n")
        file.write("PAN= " + pan + "\n")
        file.write("Account Number = " + acount_number + "\n")
        file.write("Balance = " + str(balance) + "\n" )
        file.close() 
        print("file saving succesfully ✅ ") 

#update balance 
def update_balance_file(new_balance):
    with open("Acount.txt", "r") as file:
        lines = file.readlines()

    with open("Acount.txt", "w") as file:
        for line in lines:
            if line.startswith("Balance ="):
                file.write("Balance = " + str(new_balance) + "\n")
            else:
                file.write(line)


#deposit 
def deposit():
    global balance
    amount=int(input("Enter amount your costumar are deposit = "))
    if amount > 0:
        balance+=amount
        update_balance_file(balance)
        print("Amount deposited successfully ✅")
        print("Current Balance =", balance)
    else:
        print("Invalid deposit amount ❌")
    
    
#withdraw     
def withdraw():
    global balance
    amount = int(input("Enter amount to withdraw = "))

    if amount <= balance:
        balance -= amount
        update_balance_file(balance)
        print("Withdraw successful ✅")
        print("Remaining Balance =", balance)
    else:
        print("Insufficient balance ❌")
       
        
#main 
def main():
    while True:
        print("\n====== Bank Menu ======")
        print("1. Open New Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Enter your choice = ")

        if choice == "1":
            new_acount()

        elif choice == "2":
            deposit()

        elif choice == "3":
            withdraw()

        elif choice == "4":
            print("Current Balance =", balance)

        elif choice == "5":
            print("Thank you for using Bank System 🙏")
            break

        else:
            print("Invalid choice ❌")
            
main()

        
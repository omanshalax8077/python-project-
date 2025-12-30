
psw=1122334455

name=input("Enter your name = ")
login=int(input("Enter your id = "))
def main():
    global psw
    
    paw=int(input("Enter your password = "))
    
    for i in range(3):
        
        if  paw==psw:
            print("Open your system ..... ✅")
            return
            
        
        elif paw!=psw:
            # for i in range(3):
                print("Password is not correct ❌")        
                paw=int(input("Enter your password = "))
                
    print("System locked 🔒")
    choice = input("Do you want to update password? (yes/no) = ").lower()
    choice == "yes"
    if choice=="yes":
        update()
        
def update():
    
                # choice = input("Do you want to update password? (yes/no) = ").lower()
                # choice == "yes"
                new_psw = int(input("Enter new password = "))
                confirm_psw = int(input("Confirm new password = "))

                if new_psw == confirm_psw:
                    psw = new_psw
                    print("Password updated successfully 🔐")
                    
                elif new_psw != confirm_psw:
                    print("Password not matched ❌")

                else:
                    print("Password not changed")

main()

        
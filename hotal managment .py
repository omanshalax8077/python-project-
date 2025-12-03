# Simple Hotel Management Project
hotal_rooms={
101: "Available",
102: "Available",
103: "Available",
104: "Available",
105: "Available"
}


customer_details = {}


def show_rooms():
    print("\n -----Room Status------")
    for room,status in hotal_rooms.items():
        print(f"Room{room}:{status}")


def book_rooms():
    show_rooms()
    
    room =int(input("Enter the Room Number to Book = "))

    if room in hotal_rooms and hotal_rooms[room]=="Available" :
        name=input("Enter the customer name =") 
        aadhar=int(input("Enter the aadhara Number ="))
        days=int(input("Enter the days when costomer stay he our hotal =  "))
        bils=days*1000
 
        hotal_rooms[room]="booked"
        customer_details [room]={
        "Name": name,
        "Aadhar": aadhar,
        "Days": days,
        "Bill": bils
        }
        print(f"\nRoom {room} booked successfully!")
        print("===Customer Details==")
        print(f"Customer Name : {name}")
        print(f"Aadhar Number : {aadhar}")
        print(f"Days Stayed   : {days}")
        print(f"Bill Amount   : {bils}")
    else:
     print("Sorry, Room is not available or not found.")

def book_again():
    book_rooms()
    
def bill():  
    room =int(input("Enter the Room number to generate bill:"))
    
    if room in customer_details:
        details=customer_details[room]
        
        print("======Customer bill=====")
        print(f"Customer Name : {details['Name']}")
        print(f"Aadhar Number : {details['Aadhar']}")
        print(f"Days Stayed   : {details['Days']}")
        print(f"Total Bill    : {details['Bill']}")
    else:
        print("Bill not found. Room was not booked.")
        
def main():
    while True:
        print("\n===== Hotel Management System =====")
        print("1. Show Rooms")
        print("2. Book Room")
        print("3. book room again ")
        print("4. Generate Bill")
        print("5. Exit")
        
        choice = int(input("Enter your choice: "))
        if choice == 1:
            show_rooms()
        elif choice == 2:
            book_rooms()
        elif choice==3:
            book_again()
        elif choice == 4:
            bill()
        elif choice == 5:
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice! Try again.")
main()
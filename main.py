from validator import validate_user_data
from addressbook import AddressBook
from contact import Contact

print("------------------------WELCOME TO ADDRESS BOOK-----------------------------")

def main():
    """
    Description:
        Main function that takes in input from the user and adds contact to address book
    Parameters:
        None
    Return:s
        None
    """
    address_book = AddressBook()
    while True:
        choice = int(input("\n1.Add Contact\n2.Display Contact\n3.Edit Contact\n4.Exit\nEnter choice: "))
        match choice:
            case 1:
                user_details = {
                    "first_name": input("Enter First Name: "),
                    "last_name": input("Enter Last Name: "),
                    "address": input("Enter Address: "),
                    "city": input("Enter City: "),
                    "state": input("Enter State: "),
                    "zipcode": input("Enter Zipcode: "),
                    "phone_num": input("Enter Phone Number: "),
                    "email": input("Enter Email ID: ")
                }
            
                if validate_user_data(user_details):
                    contact = Contact(**user_details)
                    address_book.add_contact(contact)
            case 2:
                address_book.print_contacts()
            case 3:
                address_book.edit_contact()
            case _:
                print("Exiting....")
                break

if __name__ == "__main__":
    main()

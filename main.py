from validator import validation_wrapper
from addressbook import AddressBook
from contact import Contact

print("------------------------WELCOME TO ADDRESS BOOK-----------------------------")

@validation_wrapper
def create_contact(user_details):
    """
    Description:
        Function that uses validation wrapper to check if user details are correct and to create contact object
    Parameters:
        Dictionary containing user details
    Return:
        Contact object
    """
    contact = Contact(**user_details)
    print("Contact has been created successfully")
    return contact

def main():
    """
    Description:
        Main function that takes in input from the user and adds contact to address book
    Parameters:
        None
    Return:
        None
    """
    while True:
        choice = int(input("Enter choice:\n1.Add Contact\n2.Exit\n"))
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
            
                contact = create_contact(user_details)
                if contact:
                    address_book = AddressBook()
                    address_book.add_contact(contact)
            case _:
                print("Exiting....")
                break

if __name__ == "__main__":
    main()

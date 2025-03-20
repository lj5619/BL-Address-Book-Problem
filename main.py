from validator import validate_user_data
from addressbook import AddressBook
from contact import Contact
from addressbookmain import *

print("------------------------WELCOME TO ADDRESS BOOK-----------------------------")

def main():
    """
    Description:
        Main function that takes in input from the user and adds contact to address book
    Parameters:
        None
    Return:
        None
    """
    address_book_main = AddressBookMain()

    address_book = None
    
    while True:
        ch = int(input("Select option u want to create:\n1.Create new addressbook\n2.Manage existing addressbook\n3.Search Contact\n4.Exit\n"))
        if ch == 1:
            
            address_book_name = input("Enter name for the new address book: ")
            address_book = address_book_main.add_address_book_to_main(address_book_name)
             
        
        elif ch == 2:
            address_book_existing_name = input("Enter name of the address book to use: ")
            address_book = address_book_main.get_address_book_from_main(address_book_existing_name)
            if not address_book:
                print("Address book not found!")
                continue
        elif ch == 3:
            option=int(input('Enter 1 for City or 2 for State: '))
            if option == 1:
                city = input('Enter name of the city: ')
                searcher = SearchAddressBookByCity(address_book_main, city)
                searcher.search_contact_by_city()
            elif option == 2:
                state = input('Enter name of the state: ')
                searcher = SearchAddressBookByState(address_book_main, state)
                searcher.search_contact_by_state()
            else:
                print('Invalid option')
            continue
        else:
            print('Thankyou for using Address Book')
            break
        
        while True:
            choice = int(input("\n1.Add Contact\n2.Display Contact\n3.Edit Contact\n4.Delete Contact\n5.Sorting by person's name alphabetically\n6.Go back\nEnter choice: "))
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
                case 4:
                    address_book.delete_contact()
                case 5:
                    address_book.sort_by_name()
                case _:
                    print("Going back....")
                    break

if __name__ == "__main__":
    main()

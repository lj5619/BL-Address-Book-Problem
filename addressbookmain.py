from addressbook import AddressBook
from contact import Contact
class AddressBookMain:

    def __init__(self):
        """
        Description:
            Constructor to initialize address books dictionary
        Parameters:
            self
        Return:
            None
        """
        self.address_books = {}

    def add_address_book_to_main(self, name):
        """
        Description:
            Function to add new address books to dictionary
        Parameters:
            self, address_book_id, address_book
        Return:
            None
        """
        if name in self.address_books.keys():
            print('Address Book with this name is already present')
        else:
            address_book = AddressBook(name)
            self.address_books[name] = address_book
            return address_book        
    

    def get_address_book_from_main(self, address_book_name):
        """
        Description:
            Function to check if address book id is present or not
        Parameters:
            self, address_book_id
        Return:
            address_book_id
        """
        return self.address_books.get(address_book_name)
    

class SearchAddressBookByCity(AddressBookMain):
    """
    Description:
        Child class that is used to search the contact based on city
    
    """

    def __init__(self,address_book_main, city):
        super().__init__()
        self.address_books = address_book_main.address_books
        self.city = city
        self.citycontacts = {}

    def search_contact_by_city(self,choice):
        """
        Description:
            Function used to search contact by city
        Parameters:
            self
        Return:
            None
        """

        for address_book in self.address_books.values():
            for contact in address_book.contacts:
                if contact.city.lower() == self.city.lower():
                    if self.city not in self.citycontacts:
                        self.citycontacts[self.city] = [] 
                    self.citycontacts[self.city].append(vars(contact))
        if not self.citycontacts:
            print('No contacts found in this city.')
        
        if choice == 1:
            print("Contacts Found -->",self.citycontacts)
        elif choice == 2:
            for k,v in self.citycontacts.items():
                print(f'In {k} there are {len(v)} people')
        else:
            print('Invalid Input')
 

class SearchAddressBookByState(AddressBookMain):
    """
    Description:
        Child class that is used to search the contact based on state
    
    """
        
    def __init__(self,address_book_main, state):
        super().__init__()
        self.address_books = address_book_main.address_books
        self.state = state
        self.statecontacts = {}
        
    def search_contact_by_state(self,choice):
        """
        Description:
            Function used to search contact by state
        Parameters:
            self
        Return:
            None
        """
        for address_book in self.address_books.values():
            for contact in address_book.contacts:
                if contact.state.lower() == self.state.lower():
                    if self.state not in self.statecontacts:
                        self.statecontacts[self.state] = [] 
                    self.statecontacts[self.state].append(vars(contact))
                    
        if not self.statecontacts:
            print('No contacts found in this state.')
        if choice == 1:
            print("Contacts Found -->",self.statecontacts)
        elif choice == 2:
            for k,v in self.statecontacts.items():
                print(f'In {k} there are {len(v)} people')
        else:
            print('Invalid Input')
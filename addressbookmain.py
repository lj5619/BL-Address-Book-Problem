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

    def __init__(self,address_book_main, city):
        super().__init__()
        self.address_books = address_book_main.address_books
        self.city = city

    def search_contact_by_city(self):

        found_contacts = []
        for address_book in self.address_books.values():
            print(address_book.contacts)
            for contact in address_book.contacts:
                if contact.city.lower() == self.city.lower():
                    found_contacts.append(vars(contact))
        if not found_contacts:
            print('No contacts found in this city.')
        
        print("Contacts Found -->",found_contacts)

class SearchAddressBookByState(AddressBookMain):
        
    def __init__(self,address_book_main, state):
        super().__init__()
        self.address_books = address_book_main.address_books
        self.state = state
        
    def search_contact_by_state(self):
        found_contacts = []
        for address_book in self.address_books.values():
            for contact in address_book.contacts:
                if contact.state.lower() == self.state.lower():
                    found_contacts.append(vars(contact))
                    
        if not found_contacts:
            print('No contacts found in this state.')
        
        print("Contacts Found -->",found_contacts)

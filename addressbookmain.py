from addressbook import AddressBook

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
from contact import Contact

class AddressBook:
    """
    Description:
        Class which stores set of contacts
    Parameters:
        None
    Return:
        None
    """
    def __init__(self,name):
        """
        Description:
            Constructor to initialize contacts list
        Paramters:
            self
        Return:
            None
        """
        self.address_book_name = name
        self.contacts = []


    def check_duplicate(self,firstname,lastname):
        for contact in self.contacts:
            if contact.first_name.lower() == firstname.lower() and contact.last_name.lower() == lastname.lower():
                return True
        return False

    def add_contact(self, contact):
        """
        Description:
            Function to add contacts to list
        Parameters:
            self,contact
        Return :
            None
        """
        if not self.check_duplicate(contact.first_name,contact.last_name):
            self.contacts.append(contact)
        else:
            print('Duplicate contact added')        

    def edit_contact(self):
        """
        Description:
            Function to edit contact
        Parameters:
            self
        Return:
            None
        """
        search_firstname,search_lastname = input("Enter the full name of the contact to delete: ").split()
        for contact in self.contacts:
            if contact.first_name.lower() == search_firstname.lower() and contact.last_name.lower() == search_lastname.lower():
                contact.update_contact()
                return
        print("Contact not found")

    def delete_contact(self):
        """
        Description:
            Function that deletes a contact by first name
        Parameters:
            None
        Return:
            None
        """
        search_firstname,search_lastname = input("Enter the full name of the contact to delete: ").split()
        for i, contact in enumerate(self.contacts):
            if contact.first_name.lower() == search_firstname.lower() and contact.last_name.lower() == search_lastname.lower():
                del self.contacts[i]
                print(f"Contact '{contact.first_name} {contact.last_name}' has been deleted")
                return
        print("Contact not found")

    def sort_by_name(self):
        """
        Description:
            Function to sort contacts alphabetically on first name
        Parameters:
            self
        Return:
            None
        """
        self.contacts.sort(key = lambda con : con.first_name)
        print('Sorted Name List')
        for contact in self.contacts:
            print(contact)

    def sorting(self,key):
        return self.contacts.sort(key = lambda con : getattr(con,key))
    
    def sort_by_location(self,choice):
        """
        Description:
            Function to sort contact on basis of city, state or zipcode
        Parameters:
            self,choice
        Return:
            none
        """
        if choice == 1:
            self.sorting('city')
        elif choice == 2:
            self.sorting('state')
        elif choice == 3:
            self.sorting('zipcode')
        else:
            print('Invalid input')
            return
            
        for contact in self.contacts:
            print(contact)
            
    def print_contacts(self):
        """
        Description:
            Function to print the contacts
        Parameters:
            self
        Return:
            none
        """
        if self.contacts:
            for contact in self.contacts:
                print(contact)
        else:
            print("No contacts found")
    
    def __str__(self):
        return self.address_book_name



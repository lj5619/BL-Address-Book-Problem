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
    def __init__(self):
        """
        Description:
            Constructor to initialize contacts list
        Paramters:
            self
        Return:
            None
        """
        self.contacts = []

    def add_contact(self, contact):
        """
        Description:
            Function to add contacts to list
        Parameters:
            self,contact
        Return :
            None
        """
        self.contacts.append(contact)

    def edit_contact(self):
        """
        Description:
            Function to edit contact
        Parameters:
            self
        Return:
            None
        """
        found = False
        search_name = input("Enter the first name of the contact to edit: ")
        for contact in self.contacts:
            if contact.first_name.lower() == search_name.lower():
                contact.update_contact()
                found = True
        if not found:
            print("Contact not found")

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



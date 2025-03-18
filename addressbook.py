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



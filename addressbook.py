
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

    def print_contacts(self):
        if self.contacts:
            for contact in self.contacts:
                print(contact)
        else:
            print("No contacts found")



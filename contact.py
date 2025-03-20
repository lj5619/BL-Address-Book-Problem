from validator import validate_user_data
from addressbook import AddressBook
class Contact:
    def __init__(self, **kwargs):
        """
        Description:
            Constructor to initialize contact with the attributes
        Parameters:
            self, **kwargs (attributes which are first name,last name, address, city, state, phone num and email)
        Return:
            None
        """
        for k,v in kwargs.items():
            setattr(self,k,v)
        
    def update_contact(self):
        """
        Description:
            Allows user to select an attribute to edit.
        Parameters:
            self
        Return:
            None
        """
        while True:
            choice = int(input('Enter integer for the attribute you want to change:\n1-Address\n2-Phone Number\n3-email\n4-Exit:'))
            match choice:
                case 1:
                    self.address = input('Enter new address: ')
                    self.city = input('Enter city: ')
                    self.state = input('Enter State: ')
                    self.zipcode = input('Enter zipcode: ')
                case 2:
                    self.phone_num= input('Enter new phone number: ')
                case 3:
                    self.email= input('Enter new email: ')
                case _:
                    print('Exiting...')
                    break

        validate_user_data(self.__dict__)
        
    def __str__(self):
        return (f"{self.first_name} {self.last_name}\n"
                f"Address: {self.address}, {self.city}, {self.state} {self.zipcode}\n"
                f"Phone: {self.phone_num}\nEmail: {self.email}")
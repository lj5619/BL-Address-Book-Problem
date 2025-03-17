class Contact:
    def __init__(self, **kwargs):
        for k,v in kwargs.items():
            setattr(self,k,v)

    def __str__(self):
        return (f"{self.first_name} {self.last_name}\n"
                f"Address: {self.address}, {self.city}, {self.state} {self.zipcode}\n"
                f"Phone: {self.phone_num}\nEmail: {self.email}")

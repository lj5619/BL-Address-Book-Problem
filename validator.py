import re

def validate_data(data_dict):
    """
    Description:
        Function to validate"""
    validated_data = {}
    
    for key, value in data_dict.items():
        if key.endswith("first_name"):
            if re.fullmatch(r'^[A-Z][a-z]{2,}$', value):  
                validated_data[key] = value
            else:
                raise ValueError("Invalid first name. It must start with a capital letter and have at least 2 lowercase letters.")
        
        elif key.endswith("last_name"):
            if re.fullmatch(r'^[A-Z][a-z]{2,}$', value): 
                validated_data[key] = value
            else:
                raise ValueError("Invalid last name. It must start with a capital letter and have at least 2 lowercase letters.")
            
        elif key.endswith("zipcode"):
            if re.fullmatch(r'^\d{6}', value):  
                validated_data[key] = value
            else:
                raise ValueError("Invalid zipcode. It must be exactly 6 digits.")
            
        elif key.endswith("phone_num"):
            if re.fullmatch(r'^\d{10}$', value): 
                validated_data[key] = value
            else:
                raise ValueError("Invalid phone number. It must be exactly 10 digits.")

        elif key.endswith("email"):
            if re.fullmatch(r'^[A-Za-z\d._+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$', value):  
                validated_data[key] = value
            else:
                raise ValueError("Invalid email format.")
        
        else:
            validated_data[key] = value  
    
    return validated_data


def validation_wrapper(func):
    def wrapper(data_dict):
        try:
            validated_data = validate_data(data_dict)
            return func(validated_data)
        except ValueError as e:
            print(f"Validation error: {e}")
            return None
    return wrapper
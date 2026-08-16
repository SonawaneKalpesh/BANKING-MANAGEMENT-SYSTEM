

class Customer:
    def __init__(self ,customer_id, name, email, phone,address):
        self.__customer_id = customer_id
        self.__name = name
        self.__email = email
        self.__phone = phone
        self.__address = address

    def get_customer_details(self):
        return {
            "customer_id": self.__customer_id,
            "name": self.__name,
            "email": self.__email,
            "phone": self.__phone,
            "address": self.__address
        }
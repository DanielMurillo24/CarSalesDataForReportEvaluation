from models.address import Address


# Class Client
class Client:
    def __init__(self, client_id, address_id, client_name, client_type,
                 client_size, is_credit_worthy, is_dealer):
        self.__client_id = client_id
        self.__address_id = address_id
        self.__client_name = client_name
        self.__client_type = client_type
        self.__client_size = client_size
        self.__is_credit_worthy = is_credit_worthy
        self.__is_dealer = is_dealer

    # Getters
    def get_client_id(self):
        return self.__client_id

    def get_address_information(self):
        address_info = Address.get_address_info(self.__address_id)
        return address_info

    def get_client_name(self):
        return self.__client_name

    def get_client_type(self):
        return self.__client_type

    def get_client_size(self):
        return self.__client_size

    def get_is_credit_worthy(self):
        return self.__is_credit_worthy

    def get_is_dealer(self):
        return self.__is_dealer

    def get_client_info(self, client_id):
        if self.__client_id == client_id:
            return "Name: " + self.__client_name + "\n" +\
                   "Client Type" + self.__client_type
        else:
            return "Client ID Invalid"

    # Setters

    def set_client_name(self, client_name):
        self.__client_name = client_name

    def set_client_type(self, client_type):
        self.__client_type = client_type

    def set_client_size(self, client_size):
        self.__client_size = client_size

    def set_is_credit_worthy(self, is_credit_worthy):
        self.__is_credit_worthy = is_credit_worthy

    def set_region(self, is_dealer):
        self.__is_dealer = is_dealer

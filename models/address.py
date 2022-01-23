# Class address related wit a client
from models.country import Country


class Address:
    def __init__(self, address_id, country_id, address1, address2, town,
                 county, region, postcode, outer_postcode):
        self.__address_id = address_id
        self.__country_id = country_id
        self.__address1 = address1
        self.__address2 = address2
        self.__town = town
        self.__county = county
        self.__region = region
        self.__postcode = postcode
        self.__outer_postcode = outer_postcode

    # Getters
    def get_address1(self):
        return self.__address1

    def get_address2(self):
        return self.__address2

    def get_town(self):
        return self.__town

    def get___county(self):
        return self.__county

    def get_region(self):
        return self.__region

    def get_postcode(self):
        return self.__postcode

    def get_outer_postcode(self):
        return self.__outer_postcode

    # Setters

    def set_address1(self, address1):
        self.__address1 = address1

    def set_address2(self, address2):
        self.__address2 = address2

    def set_town(self, town):
        self.__town = town

    def set_county(self, county):
        self.__county = county

    def set_region(self, region):
        self.__region = region

    def set_postcode(self, postcode):
        self.__postcode = postcode

    def set_outer_postcode(self, outer_postcode):
        self.__outer_postcode = outer_postcode

    # return the address information
    def get_address_info(self, address_id):
        if address_id == self.__address_id:
            return "Town: " + self.__town + "\n" + \
                   "county: " + self.__county + "\n" + \
                   "Region: " + self.__region + "\n" + \
                   "postcode: " + str(self.__postcode) + "\n" + \
                   "Country :" + Country.get_country_name(self.__country_id) + "\n" + \
                   "Address description" + self.__address1
        else:
            return "Address country no valid"


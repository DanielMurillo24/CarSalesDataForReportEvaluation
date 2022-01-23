# Class of country
class Country:
    def __init__(self, country_id, country_name, country_iso_code):
        self.__country_id = country_id
        self.__country_name = country_name
        self.__country_iso_code = country_iso_code

    # Getters
    def get_country_iso_code(self):
        return self.__country_iso_code

    # return the country name if the country id is valid
    def get_country_name(self, country_id):
        if self.__country_id == country_id:
            return self.__country_name
        else:
            "Code no valid"

    # Setters

    def set_country_name(self, country_name):
        self.__country_name = country_name

    def set_country_iso_code(self, iso_code):
        self.__country_iso_code = iso_code

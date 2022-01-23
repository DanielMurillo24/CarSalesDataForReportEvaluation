from models.color import Color


# Class Vehicle
class Vehicle:
    def __init__(self, vehicle_id, make, model, color_id, vehicle_type,
                 vehicle_age_in_year, labor_cost, spare_parts, registration_date):
        self.__vehicleID = vehicle_id
        self.__make = make
        self.__model = model
        self.__color_id = color_id
        self.__vehicle_type = vehicle_type
        self.__vehicle_age_in_year = vehicle_age_in_year
        self.__labor_cost = labor_cost
        self.__spare_parts = spare_parts
        self.__registration_date = registration_date

    # Getters

    def get_vehicle_id(self):
        return self.__vehicleID

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_vehicle_type(self):
        return self.__vehicle_type

    def get_vehicle_age_in_year(self):
        return self.__vehicle_age_in_year

    def get_labor_cost(self):
        return self.__labor_cost

    def get_spare_parts(self):
        return self.__spare_parts

    def get_registration_date(self):
        return self.__registration_date

    def get_color(self):
        return Color.get_color(self.__color_id)

    # Setters

    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_color_id(self, color_id):
        self.__color_id = color_id

    def set_vehicle_type(self, vehicle_type):
        self.__vehicle_type = vehicle_type

    def set_labor_cost(self, labor_cost):
        self.__labor_cost = labor_cost

    def set_spare_parts(self, spare_parts):
        self.__labor_cost = spare_parts

    def set_registration_date(self, registration_date):
        self.__registration_date = registration_date

    # Method the add a new vehicle
    def add_new_vehicle(self):
        return "Vehicle added successfully" + "\n" + "Vehicle ID: " + str(self.__vehicleID)

    # Method that show all information about the vehicle
    def to_string(self):
        return "Vehicle ID: " + str(self.__vehicleID) + "\n" + \
               "Make: " + self.__make + "\n" + "Model: " + self.__model + "\n" + \
               "Vehicle Type: " + self.__vehicle_type + "\n" + \
               "Age in years: " + str(self.__vehicle_age_in_year) + "\n" + \
               "Labor Cost: " + str(self.__labor_cost) + "\n" + \
               "Spare Part: " + str(self.__spare_parts) + "\n" + \
               "Registration Date: " + self.__registration_date

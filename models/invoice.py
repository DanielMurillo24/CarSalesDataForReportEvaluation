from models.client import Client


class Invoice:
    def __init__(self, invoice_id, invoice_number, client_id, invoice_date, total_discount,
                 delivery_charge, invoice_date_key):
        self.__invoice_id = invoice_id
        self.__invoice_number = invoice_number
        self.__client_id = client_id
        self.__invoice_date = invoice_date
        self.__total_discount = total_discount
        self.__delivery_charge = delivery_charge
        self.__invoice_date_key = invoice_date_key

    # Getters

    def get_invoice_id(self):
        return self.__invoice_id

    def get_invoice_number(self):
        return self.__invoice_number

    def get_invoice_date(self):
        return self.__invoice_date

    def get_total_discount(self):
        return self.__total_discount

    def get_delivery_charge(self):
        return self.__delivery_charge

    def get_invoice_date_key(self):
        return self.__invoice_date_key

    def get_client_id(self):
        return Client.get_client_info(self.__client_id)

    # Setters

    def set_client_id(self, client_id):
        self.__client_id = client_id

    def set_invoice_date(self, invoice_date):
        self.__invoice_date= invoice_date

    def set_total_discount(self, total_discount):
        self.__total_discount = total_discount

    def set_delivery_charge(self, delivery_charge):
        self.__delivery_charge = delivery_charge

    # Method that allow see the information about of the invoice
    def view_invoice_info(self, invoice_id):
        if self.__invoice_id == invoice_id:
            return "Invoice Number" + str(self.__invoice_number) + "\n" + \
                   "Client ID: " + self.__client_id + "\n" + \
                   "Invoice Date: " + self.__invoice_date + "\n" + \
                   "Total Discount: " + str(self.__total_discount) + "\n" + \
                   "Delivery Charge: " + str(self.__delivery_charge)
        else:
            return "Invoice ID Invalid"


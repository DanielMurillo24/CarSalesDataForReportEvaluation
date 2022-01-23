class Stock:
    def __init__(self, stock_id, vehicle_id, cost_price, purchase_date, stock, currency_type):
        self.__stock_id = stock_id
        self.__vehicle_id = vehicle_id
        self.__cost_price = cost_price
        self.__purchase_date = purchase_date
        self.__stock = stock
        self.__currency_type = currency_type

    # Getters

    def get_stock_id(self):
        return self.__stock_id

    def get_vehicle_id(self):
        return self.vehicle_id

    def get_cost_price(self):
        return self.__cost_price

    def get_purchase_date(self):
        return self.__purchase_date

    def get_stock(self):
        return self.__stock

    def get_currency_type(self):
        return self.__currency_type

    # Setters

    def set_stock(self, stock):
        self.__stock = stock

    def set_currency_type(self, currency_type):
        self.__currency_type = currency_type

    def set_purchase_date(self, purchase_date):
        self.__purchase_date = purchase_date

    def set_cost_price(self, cost_price):
        self.__cost_price = cost_price

    # This method return the stock info of a particular vehicle
    def search_vehicle_stock(self, vehicle_id):
        if self.__vehicle_id == vehicle_id:
            return "Stock: " + str(self.__stock) + "\n" + \
                   "Cost Price: " + str(self.__cost_price) + "\n" + \
                   "Currency_type" + self.__currency_type + "\n" + \
                   "Purchase Date" + self.__purchase_date
        else:
            return "Vehicle ID Invalid"

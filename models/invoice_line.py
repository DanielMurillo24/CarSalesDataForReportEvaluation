class InvoiceLine:
    def __init__(self, invoice_line_id, invoice_id, stock_id, sale_price, line_item):
        self.__invoice_line_id = invoice_line_id
        self.__invoice_id = invoice_id
        self.__stock_id = stock_id
        self.__sale_price = sale_price
        self.__line_item = line_item

    # Getters
    def get_line_item(self):
        return self.__line_item

    def get_sale_price(self):
        return str(self.__sale_price)

    # Setters

    def set_sale_price(self, sale_price):
        self.__sale_price = sale_price

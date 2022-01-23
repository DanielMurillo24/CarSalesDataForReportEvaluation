class Color:
    def __init__(self, color_id, color):
        self.__color_id = color_id
        self.__color = color

    # Getters

    def get_color(self, color_id):
        if self.__color_id == color_id:
            return self.__color
        else:
            "Invalid ID color"

    def get_color_id(self):
        return self.__color_id

    # Setters

    def set_color(self, color):
        self.__color = color

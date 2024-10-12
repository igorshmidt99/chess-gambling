class PlayerGetDto:
    __first_name: str
    __last_name: str

    def __init__(self, first_name: str, last_name: str):
        self.__first_name = first_name
        self.__last_name = last_name

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

class Player:
    __first_name: str
    __last_name: str
    __wins: int
    __loses: int

    def __init__(self, first_name: str, last_name: str):
        self.__first_name = first_name
        self.__last_name = last_name

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_wins(self):
        return self.__wins

    def set_wins(self, wins: int):
        self.__wins = wins

    def get_loses(self):
        return self.__loses

    def set_loses(self, loses: int):
        self.__loses = loses

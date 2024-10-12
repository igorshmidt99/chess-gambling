from random import randrange

from main.player.model.player import Player


class PairGeneratorService:

    # Если list.size % 2 != 0, то тогда игроки удаляются до тех пор, пока не будет равенства
    # Сначала игрок случайный, а потом с наибольшим кол-вом поражений, что-то отправить ему
    def generate_pairs(self, players: list):
        players_amount = len(players)
        pairs = {}
        if players_amount < 1:
            return pairs
        players = self.__limit_players_count(players)
        pairs = self.__initialize_pairs(pairs, players)

        return pairs

    def __initialize_pairs(self, pairs: dict[int, list[Player]], players: list):
        players_amount = len(players)
        players_amount //= 2
        for i in range(players_amount):
            first_player = self.__get_random_player(players)
            second_player = self.__get_random_player(players)
            pairs[i] = [first_player, second_player]
        return pairs

    def __limit_players_count(self, players: list):
        if self.__check_is_power_of_two(len(players)):
            return players
        players_amount: int = len(players)
        while not self.__check_is_power_of_two(players_amount):
            players_amount -= 1
        return players[:players_amount]

    def __check_is_power_of_two(self, player_amount: int):
        return bin(player_amount).count('1') == 1

    def __get_random_player(self, players: list):
        players_amount = len(players)
        index = randrange(players_amount)
        player: Player = players[index]
        players.remove(player)
        return player

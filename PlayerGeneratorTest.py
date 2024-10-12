import unittest

from main.pair.generator import PairGeneratorService
from main.player.model.player import Player


class MyTestCase(unittest.TestCase):
    service = PairGeneratorService()

    def test_four_players_produceses_list_with_unique_pairs(self):
        players = self.__init_data(127)
        pairs = self.service.generate_pairs(players)
        items = pairs.items()
        players_as_set: set = set()
        for pair in items:
            for player in pair[1]:
                players_as_set.add(player)
        self.assertEqual(len(players_as_set), 64)

    def test_four_players_produceses_list_with_len_2(self):
        players = self.__init_data(127)
        pairs = self.service.generate_pairs(players)
        self.assertEqual(len(pairs), 32)  # add assertion here

    def test_when_only_player(self):
        players = self.__init_data(1)
        pairs = self.service.generate_pairs(players)
        self.assertEqual(len(pairs), 0)

    def test_when_no_players(self):
        players = []
        pairs = self.service.generate_pairs(players)
        self.assertEqual(len(pairs), 0)

    def __init_data(self, players_amount: int):
        players: list = []
        for i in range(players_amount):
            players.append(Player(str(i), str(i)))
        return players


if __name__ == '__main__':
    unittest.main()

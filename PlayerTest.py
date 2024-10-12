import unittest

from main.player.model import Player


class MyTestCase(unittest.TestCase):
    def test_something(self):
        inst: Player = Player("Igor", "Shmidt")
        self.assertEqual(inst.get_first_name(), "Igor")  # add assertion here

    def test_last_name(self):
        inst: Player = Player("Igor", "Shmidt")
        self.assertEqual(inst.get_last_name(), "Shmidt")


if __name__ == '__main__':
    unittest.main()
from main.player.dto.player_dto_create import PlayerCreateDto
from main.player.model.player import Player
from main.player.repository.playerRepository import PlayerRepository


class PlayerService:
    __player_repository: PlayerRepository

    def __init__(self, player_repository: PlayerRepository):
        self.__player_repository = player_repository
        super().__init__()

    def create_player(self, dto: PlayerCreateDto):
        player: Player = Player(dto.get_first_name(), dto.get_last_name())
        self.__player_repository.save_player(player)

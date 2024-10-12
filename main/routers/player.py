from fastapi import APIRouter

from main.player.dto.player_dto_create import PlayerCreateDto

router = APIRouter()


@router.get("/create")
async def create_player():
    return ""

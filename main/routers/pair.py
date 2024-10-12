from fastapi import APIRouter

router = APIRouter(prefix="/pairs")


@router.get("/")
async def get_pairs():
    return "Pair need for pairs implementation"

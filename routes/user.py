from fastapi import APIRouter, Depends
from auth.dependencies import get_current_user
from models.user import User

router = APIRouter(prefix="/users")

@router.get("/me")
def get_my_info(current_user: User = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "email": current_user.email,
        "nickname": current_user.nickname
    }

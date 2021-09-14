from fastapi import APIRouter
from . import controller 

router = APIRouter(
    prefix="/session",
    tags = ["session"], 
    dependencies = []
)


@router.get('')
def get_users():
    return controller.get_users()

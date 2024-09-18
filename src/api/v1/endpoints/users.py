from fastapi import APIRouter

from src.controllers.users import UserController
from src.schemas.users import UserCreateSchema

router = APIRouter()


@router.get("")
async def get_users():
    return await UserController().get_all_users()


@router.post("")
async def create_user(data: UserCreateSchema):
    # print(data)
    # data = UserCreateSchema().load(data)
    # print(data)
    return await UserController().create_user(data.model_dump())

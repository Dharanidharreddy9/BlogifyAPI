
from fastapi import APIRouter, Depends
from starlette import status
from .schema import users, updateUserModel
from Global.Responses import no_response
from Global.validate import decodeJWT
from .model import createUser, updateUser, deleteUser


router = APIRouter(tags=['User Registration'], prefix="/web/v1/Registration")




@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_user(userData: users):
    try:
        return createUser(userData)
    except Exception as e:
        return no_response


@router.put("/update")
async def update_user(userCode: str, updatedUser: updateUserModel, token: users = Depends(decodeJWT)):
    try:
        response = updateUser(userCode, updatedUser)
        return response
    except Exception as e:
        return no_response
    

@router.delete("/delete", response_model=dict)
async def delete_user(userCode: str, token: users = Depends(decodeJWT)):
    try:
        response = deleteUser(userCode)
        return response
    except Exception as e:
        return no_response
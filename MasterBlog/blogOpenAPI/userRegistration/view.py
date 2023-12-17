
from fastapi import APIRouter, Depends
from starlette import status
from .schema import users
from Global.Responses import no_response
from Global.validate import decodeJWT
from .model import createUser, updateUser, deleteUser


router = APIRouter(tags=['User Registration'], prefix="/web/v1/Registration")




@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_user(create_user_req: users):
    try:
        return createUser(create_user_req)
    except Exception as e:
        return no_response


@router.put("/update", response_model=dict)
async def update_user(updated_user: users, current_user: users = Depends(decodeJWT)):
    try:
        response = updateUser(updated_user)
        return response
    except Exception as e:
        return no_response
    

@router.delete("/delete", response_model=dict)
async def delete_user(username: str, password: str, current_user: users = Depends(decodeJWT)):
    try:
        response = deleteUser(username, password)
        return response
    except Exception as e:
        return no_response
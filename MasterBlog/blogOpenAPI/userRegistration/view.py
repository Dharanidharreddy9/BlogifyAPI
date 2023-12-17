
from fastapi import APIRouter, Depends
from starlette import status
from .schema import users, updateUserModel, createResp, updateResp, deleteResp
from Global.Responses import no_response
from Global.validate import decodeJWT
from .model import createUser, updateUser, deleteUser


router = APIRouter(tags=['User Registration'], prefix="/web/v1/Registration")



# This route will create the users.
@router.post("/create", responses=createResp)
async def create_user(userData: users):
    try:
        return createUser(dict(userData))
    except Exception as e:
        print(e, "reg")
        return no_response


# This route to update user information.
@router.put("/update", responses=updateResp)
async def update_user(userCode: str, updatedUser: updateUserModel, token: users = Depends(decodeJWT)):
    try:
        response = updateUser(userCode, updatedUser)
        return response
    except Exception as e:
        return no_response
    

# This route to delete a user.
@router.delete("/delete", responses=deleteResp)
async def delete_user(userCode: str, token: users = Depends(decodeJWT)):
    try:
        response = deleteUser(userCode)
        return response
    except Exception as e:
        return no_response
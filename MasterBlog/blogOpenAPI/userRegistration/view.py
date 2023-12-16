
from fastapi import APIRouter, Depends
from config import users_collection
from bson import ObjectId
from starlette import status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from .model import users
from pymongo import MongoClient
from config import client
from typing import Annotated
from Global.Responses import no_response, success_created
from .model import createUser


router = APIRouter(tags=['User Registration'], prefix="/web/v1/Registration")





@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_user(create_user_req: users):
    try:
        return createUser(create_user_req)
    except Exception as e:
        return no_response


# I need to build the update delet methods also here
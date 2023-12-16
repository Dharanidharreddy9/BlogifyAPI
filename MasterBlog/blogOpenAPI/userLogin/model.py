
from pydantic import BaseModel
from typing import List
from datetime import datetime



class UserCredentials(BaseModel):
    username: str
    password: str


class JWTToken(BaseModel):
    access_token: str


class UserModel(BaseModel):
    username: str
    hashed_password: str

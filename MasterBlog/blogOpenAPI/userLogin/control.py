
from fastapi import HTTPException, status
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
from config import SECRET_KEY, ALGORITHM
from .model import UserCredentials, JWTToken, UserModel
from Global.Responses import no_response, authentication_failed
from config import users_collection


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")



def create_jwt_token(data: dict):
    try:
        to_encode = data.copy()
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    except Exception as e:
        return no_response

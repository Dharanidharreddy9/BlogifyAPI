
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


def verify_password(plain_password, hashed_password):
    try:
        is_psw = pwd_context.verify(plain_password, hashed_password)
        return is_psw
    except Exception as e:
        return no_response


def get_user_from_db(username: str) -> UserModel:
    try:
        user = users_collection.find_one({"username": username})
        return user if user else None
    except Exception as e:
        return no_response
    

def validate_user_credentials(credentials: UserCredentials) -> UserModel:
    try:
        user = get_user_from_db(credentials.username)
        if user:
            verify_psw = verify_password(credentials.password, user.get('hashed_password'))
            if not user or not verify_psw:
                return False
            return user
        else:
            return False
    except Exception as e:
        return no_response

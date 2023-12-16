
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from datetime import timedelta
from .control import validate_user_credentials, create_jwt_token
from .model import UserCredentials, JWTToken
from Global.Responses import no_response, authentication_failed
from config import users_collection


router = APIRouter(tags=['User Login'], prefix="/web/v1/user")


# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/login", response_model=JWTToken)
async def login(credentials: UserCredentials):
    try:
        user = validate_user_credentials(credentials)
        if not user or user.get('username') is None:
            return authentication_failed

        access_token = create_jwt_token(data={"sub": user.get('username')})

        return {"access_token": access_token}
    except Exception as e:
        return no_response
    

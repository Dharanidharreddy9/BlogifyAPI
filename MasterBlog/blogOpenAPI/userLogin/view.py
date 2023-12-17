
from fastapi import APIRouter
from.model import create_jwt_token
from .model import UserCredentials, JWTToken
from Global.Responses import no_response, authentication_failed, required_fields
from ..userRegistration.model import verify_user_credentials
# from .userRegistration.model import verify_user_credentials


router = APIRouter(tags=['User Login'], prefix="/web/v1/user")




@router.post("/login", response_model=JWTToken)
async def login(credentials: UserCredentials):
    try:
        if credentials.username is None or credentials.password is None:
            return required_fields
        user = verify_user_credentials(credentials.username, credentials.password)
        if not user or user.get('username') is None:
            return authentication_failed
        access_token = create_jwt_token(data={"sub": user.get('username')})

        return {"access_token": access_token}
    except Exception as e:
        return no_response
    




from jose import jwt
from pydantic import BaseModel, Field
from passlib.context import CryptContext
from config import SECRET_KEY, ALGORITHM
from Global.Responses import no_response


class UserCredentials(BaseModel):
    username: str = Field(..., description="The username is required")
    password: str = Field(..., description="The password is required")
    
    

class JWTToken(BaseModel):
    access_token: str = Field(default="eyJhbGciOiJIUz6IkpXVCJ9.eyJzdWIiOiJzaHJpc29tIn0.l7yme7fNhpfWcu9wkN7TPrFJFuhH0E", 
                              description="The JWT access token")


class UserModel(BaseModel):
    username: str
    hashed_password: str




pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")



def create_jwt_token(data: dict):
    try:
        to_encode = data.copy()
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    except Exception as e:
        return no_response

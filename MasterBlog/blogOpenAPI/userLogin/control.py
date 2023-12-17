

from passlib.context import CryptContext
from jose import jwt
from config import SECRET_KEY, ALGORITHM
from Global.Responses import no_response





pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")



def create_jwt_token(data: dict):
    try:
        to_encode = data.copy()
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    except Exception as e:
        return no_response

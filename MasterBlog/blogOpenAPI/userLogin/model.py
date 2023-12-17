


from jose import jwt
from passlib.context import CryptContext
from config import SECRET_KEY, ALGORITHM
from Global.Responses import no_response




pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")



# This function Create a JWT token for the provided data.
def create_jwt_token(data: dict):
    try:
        to_encode = data.copy()
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    except Exception as e:
        return no_response

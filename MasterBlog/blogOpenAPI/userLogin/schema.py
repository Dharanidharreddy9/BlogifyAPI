



from pydantic import BaseModel, Field
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
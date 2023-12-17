from pydantic import BaseModel, Field, StrictStr, validate_email, EmailStr
from typing import Optional



class users(BaseModel):
    userCode: Optional[StrictStr] = Field(title="User Code",description="provide user code,this is not a mandatory field")
    email: EmailStr = Field(title="Email", description="Provide Email,this is a mandatory field")
    username: StrictStr = Field(title="Username", description="Provide username, this is a mandatory field")
    password: StrictStr = Field(title="Password", description="Provide password, this is a mandatory field")



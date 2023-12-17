from pydantic import BaseModel, Field, StrictStr, validate_email, EmailStr
from typing import Optional



class users(BaseModel):
    userCode: Optional[StrictStr] = Field(default="ur_cd34rt", title="User Code",description="provide user code,this is not a mandatory field")
    email: EmailStr = Field(title="Email", description="Provide Email,this is a mandatory field")
    username: StrictStr = Field(default="Robin", title="Username", description="Provide username, this is a mandatory field")
    password: StrictStr = Field(default="Robin@123", title="Password", description="Provide password, this is a mandatory field")


class updateUserModel(BaseModel):
    username: StrictStr
    password: StrictStr


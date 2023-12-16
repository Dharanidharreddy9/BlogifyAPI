from typing import List
from datetime import datetime
from pydantic import BaseModel
from config import users_collection
from passlib.context import CryptContext
from Global.Responses import success_created, invalid_input


class users(BaseModel):
    username: str
    password: str





def createUser(userData):
    try:
        print(userData, "userData")
        if userData:    
            bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
            hashed_password = bcrypt_context.hash(userData.password)

            users_collection.insert_one({"username": userData.username,
                                        "hashed_password": hashed_password,
                                    })            
            return success_created             
        else:
            return invalid_input
    except Exception as e:
        return {"Unsuccesfull": "Server Not responding"}, 500
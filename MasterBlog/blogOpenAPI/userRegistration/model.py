from typing import List
from datetime import datetime
from bson import ObjectId
from config import users_collection
from passlib.context import CryptContext
from Global.Responses import success_created, invalid_input, no_response, success_ok
from .schema import users



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
        return no_response


def verify_user_credentials(username: str, password: str):
    try:
        user = users_collection.find_one({"username": username})
        if user:
            hashed_password = user.get("hashed_password", "")
            bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
            if bcrypt_context.verify(password, hashed_password):
                return user
        return None
    except Exception as e:
        return no_response


def updateUser(user_id: str, updated_user: users):
    try:
        existing_user = verify_user_credentials(updated_user.username, updated_user.password)
        if existing_user:
            result = users_collection.update_one(
                {"_id": ObjectId(user_id)},
                {"$set": {"username": updated_user.username, "password": updated_user.password}}
            )
            if result.matched_count:
                return success_ok
            else:
                return {"message": "User not found"}, 404
        else:
            return {"message": "Invalid credentials for updating user"}, 401
    except Exception as e:
        return no_response


def deleteUser(user_id: str, username: str, password: str):
    try:
        existing_user = verify_user_credentials(username, password)
        if existing_user:
            result = users_collection.delete_one({"_id": ObjectId(user_id)})
            if result.deleted_count:
                return success_ok
            else:
                return {"message": "User not found"}, 404
        else:
            return {"message": "Invalid credentials for deleting user"}, 401
    except Exception as e:
        return no_response
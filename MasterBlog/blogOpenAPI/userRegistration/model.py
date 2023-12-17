
import random
import string
from .schema import users, updateUserModel
from typing import List
from datetime import datetime
from bson import ObjectId
from config import users_collection
from passlib.context import CryptContext
from Global.Responses import success_created, invalid_input, no_response, success_ok, \
                            user_exists, no_data, code_exists





def generateCode(range_, prefix):
    """
    Generate a random code based on the specified range and prefix.

    Args:
        range_ (int): The length of the code.
        prefix (str): The prefix to be added to the code.

    Returns:
        str: The generated code.
    """
    if range_ == 6 and prefix:
        res = prefix +'_'+''.join(random.choices(string.ascii_uppercase + string.digits, k=range_))
        return res
    else: 
        res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
        return res



def createUser(userData):
    """
    Creates user in the user section.

    Args:
        userData (dict): User data containing information like 'userCode', 'email', 'username', and 'password'.

    Returns:
        dict: A response indicating the success or failure of the user creation.
    """
    try:
        if 'userCode' not in userData or userData['userCode'] is None or userData['userCode'] == "":
                userData['userCode'] = generateCode(range_=6, prefix='pt')

        if 'userCode' in userData:
            if not userData['userCode'].lower().startswith('ur_'):
                userData['userCode'] = 'ur_' + userData['userCode']

        is_user_code = users_collection.find_one({"userCode": userData['userCode']})
        if is_user_code:
            return code_exists
    
        usernm = users_collection.find_one({"username": userData['username']})
        useremail = users_collection.find_one({"email": userData['email']})
        if usernm or useremail:
            return user_exists

        if userData:    
            bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
            hashed_password = bcrypt_context.hash(userData['password'])

            users_collection.insert_one({
                "userCode": userData['userCode'],
                "email": userData['email'],
                "username": userData['username'],
                "Password": hashed_password,
            })            
            return success_created             
        else:
            return invalid_input
    except Exception as e:
        print(e, "model")
        return no_response


def verify_user_credentials(username: str, password: str):
    """
    Verify user credentials.

    Args:
        username (str): The username.
        password (str): The password.

    Returns:
        dict: The user information if credentials are valid, else None.
    """
    try:
        user = users_collection.find_one({"username": username})
        if user:
            hashed_password = user.get("Password", "")
            bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
            if bcrypt_context.verify(password, hashed_password):
                return user
        return None
    except Exception as e:
        return no_response


def updateUser(userCode: str, updatedUser: updateUserModel):
    """
    Update user information.

    Args:
        userCode (str): The user code to identify the user.
        updatedUser (updateUserModel): The updated user data.

    Returns:
        dict: A response indicating the success or failure of the user update.
    """
    try:
        # existing_user = verify_user_credentials(updatedUser.username, updatedUser.password)
        # if existing_user:
        bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
        hashed_password = bcrypt_context.hash(updatedUser.password)
        result = users_collection.update_one({"userCode": userCode},
                                            {"$set": {"username": updatedUser.username, "password": hashed_password}}
                                            )
        if result.matched_count:
            return success_ok
        else:
            return no_data
        # else:
        #     return {"message": "Invalid credentials for updating user"}, 401
    except Exception as e:
        return no_response


def deleteUser(userCode: str):
    """
    Delete a user.

    Args:
        userCode (str): The user code to identify the user.

    Returns:
        dict: A response indicating the success or failure of the user deletion.
    """
    try:
        result = users_collection.delete_one({"userCode": userCode})
        if result.deleted_count:
            return success_ok
        else:
            return no_data
    except Exception as e:
        return no_response